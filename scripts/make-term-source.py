#!/usr/bin/env python3
"""Derive a strictly monospaced "Paper Mono Term" source for terminals.

The scripts applies the following changes:
- Removes double width and narrow alternative letter glyphs.
- Scales uniformly arrows, keyboard symbols, etc.
- Renames the family.
- Set isFixedPitch to true.

Usage: python3 scripts/make-term-source.py SOURCE.glyphspackage OUTPUT.glyphs
"""

import argparse

from fontTools.misc.transform import Transform
from glyphsLib import GSFont
from glyphsLib.types import Transform as GSTransform

FAMILY_NAME = "Paper Mono Term"
REMOVED_FEATURES = {"ss02", "ss03"}
REMOVED_SUFFIXES = tuple("." + tag for tag in REMOVED_FEATURES)


def master_layers(glyph, font):
    """Master and brace/bracket layers; backup layers are ignored by the build."""
    master_ids = {m.id for m in font.masters}
    for layer in glyph.layers:
        if (
            layer.layerId in master_ids
            or layer._is_brace_layer()
            or layer._is_bracket_layer()
        ):
            yield layer


def remove_glyphs(font, names):
    for name in names:
        del font.glyphs[name]

    def strip(code):
        return " ".join(n for n in code.split() if n not in names)

    for cls in font.classes:
        cls.code = strip(cls.code)
    for feature in list(font.features):
        if feature.name in REMOVED_FEATURES:
            font.features.remove(feature)
        elif feature.name == "aalt":
            feature.code = "".join(
                line
                for line in feature.code.splitlines(keepends=True)
                if line.strip() not in {f"feature {t};" for t in REMOVED_FEATURES}
            )
    for feature in font.features:
        if any(n in feature.code for n in names):
            raise SystemExit(f"Feature {feature.name} still references a removed glyph")

    param = font.customParameters["glyphOrder"]
    if param:
        font.customParameters["glyphOrder"] = [n for n in param if n not in names]


def scaling_transform(old_width, new_width, y_center):
    scale = new_width / old_width
    return (
        Transform()
        .translate(new_width / 2, y_center)
        .scale(scale)
        .translate(-old_width / 2, -y_center)
    )


def apply_transform(layer, t, transforms):
    for path in layer.paths:
        for node in path.nodes:
            node.position = t.transformPoint(node.position)
    for anchor in layer.anchors:
        anchor.position = t.transformPoint(anchor.position)
    for component in layer.components:
        inner = Transform(*component.transform.value)
        base = transforms.get(component.name)
        # A component of a glyph that is itself rescaled must be conjugated,
        # otherwise the base glyph's own scaling would be applied twice.
        new = t.transform(inner)
        if base is not None:
            new = new.transform(base.inverse())
        component.transform = GSTransform([round(v, 4) for v in new])


def fit_wide_glyphs(font, width):
    default_master = font.masters[0].id

    transforms = {}
    for glyph in font.glyphs:
        if not glyph.export:
            continue
        widths = {round(layer.width) for layer in master_layers(glyph, font)}
        widths.discard(width)
        if not widths:
            continue
        if widths == {0}:
            continue  # combining marks stay zero-width
        if len(widths) != 1:
            raise SystemExit(f"{glyph.name}: inconsistent widths {widths}")
        old_width = widths.pop()
        if old_width < width:
            raise SystemExit(f"{glyph.name}: narrower than {width}, handle manually")
        # Scale around the vertical center of the default master's bounds so
        # the shape keeps its position relative to the text.
        bounds = glyph.layers[default_master].bounds
        y_center = bounds.origin.y + bounds.size.height / 2 if bounds else 0
        transforms[glyph.name] = scaling_transform(old_width, width, y_center)

    for name, t in transforms.items():
        for layer in master_layers(font.glyphs[name], font):
            apply_transform(layer, t, transforms)
            layer.width = width
        print(f"  scaled {name} to {width}")


def get_glyph_width(font, glyphName):
    return round(font.glyphs[glyphName].layers[font.masters[0].id].width)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("source")
    parser.add_argument("output")
    args = parser.parse_args()

    font = GSFont(args.source)

    removed = [g.name for g in font.glyphs if g.name.endswith(REMOVED_SUFFIXES)]
    remove_glyphs(font, set(removed))
    print(f"  removed {len(removed)} glyphs: {' '.join(removed)}")

    width = get_glyph_width(font, "space")
    fit_wide_glyphs(font, width)

    font.familyName = FAMILY_NAME
    font.customParameters["isFixedPitch"] = 1

    font.save(args.output)
    print(f"Wrote {args.output} ({FAMILY_NAME}, advance {width})")


if __name__ == "__main__":
    main()
