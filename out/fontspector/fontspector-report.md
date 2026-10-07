## FontSpector report

fontspector version: 1.4.0






## Check results




<details><summary>[12] fonts/variable/PaperMono[wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. (opentype/monospace)</summary>
    <div>








- ⚠️ **WARN** The OpenType spec recommends at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 799 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
  
  


- ⚠️ **WARN** Font is monospaced (common width = 606) but 41 glyphs (5.12%) have a different width. You should check the widths of:

* uniF8FF (417), width: 758
* uni21E4 (482), width: 758
* uni21E5 (483), width: 758
* uni21A9 (484), width: 758
* uni21AA (485), width: 758
* uni21B0 (486), width: 758
* uni21B1 (487), width: 758
* uni21B3 (488), width: 758
* uni21B4 (489), width: 758
* carriagereturn (490), width: 758
* uni21E7 (491), width: 758
* uni21B9 (492), width: 758
* uni21C6 (493), width: 758
* AE.ss02 (608), width: 758
* M.ss02 (609), width: 758
* OE.ss02 (610), width: 758
* W.ss02 (611), width: 758
* Wacute.ss02 (612), width: 758
* Wcircumflex.ss02 (613), width: 758
* Wdieresis.ss02 (614), width: 758
* Wgrave.ss02 (615), width: 758
* ae.ss02 (616), width: 758
* m.ss02 (617), width: 758
* oe.ss02 (618), width: 758
* w.ss02 (619), width: 758
* wacute.ss02 (620), width: 758
* wcircumflex.ss02 (621), width: 758
* wdieresis.ss02 (622), width: 758
* wgrave.ss02 (623), width: 758
* space.ss03 (624), width: 454
* uni00A0.ss03 (625), width: 454
* uni238B (786), width: 758
* uni2303 (787), width: 758
* uni21EA (788), width: 758
* uni2327 (789), width: 758
* uni232B (790), width: 758
* uni2326 (791), width: 758
* uni2325 (792), width: 758
* uni2318 (793), width: 758
* uni23CE (794), width: 758
* openbullet (797), width: 600 [code: mono-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? (gpos_kerning_info)</summary>
    <div>








- ⚠️ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* blackCircled [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? (valid_glyphnames)</summary>
    <div>








- ⚠️ **WARN** The following glyph names are too long: "asciitilde_asciitilde_greater.liga" [code: legacy-long-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages           |
|-------------------------------------------------------------------|---------------------|
| Auxiliary orthography codepoints:                                 | * en_Latn (English) |
|   The following auxiliary characters are missing from the font: ʻ |                     |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish) |
|   The following auxiliary characters are missing from the font: Ʒ |                     |
|   The following auxiliary characters are missing from the font: Ǯ |                     |
|   The following auxiliary characters are missing from the font: ʒ |                     |
|   The following auxiliary characters are missing from the font: ǯ |                     |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)  |
|   The following auxiliary characters are missing from the font: ſ | * fr_Latn (French)  | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. (dotted_circle)</summary>
    <div>








- ⚠️ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* į̂
* į̄
* į́
* į̀
* į̌
* į̃The dot of soft dotted characters _should_ disappear in other cases, for example:

* į̶̋
* į̶̒
* į̶̂
* į̶̄
* į̶́
* į̶̇
* į̶̀
* į̶̌
* į̶̈
* į̶̊
* į̶̆
* į̶̃
* į̷̒
* į̨̋
* į̨̒
* į̨̂
* į̨̄
* į̨́
* į̨̇
* į̨̀
* į̨̌
* į̨̈
* į̨̊
* į̨̆
* į̨̃
* į̵̒
* į̸̒
* į̦̋
* į̦̒
* į̦̂
* į̦̄
* į̦́
* į̦̇
* į̦̀
* į̦̌
* į̦̈
* į̦̊
* į̦̆
* į̦̃
* į̧̋
* į̧̒
* į̧̂
* į̧̄
* į̧́
* į̧̇
* į̧̀
* į̧̌
* į̧̈
* į̧̊
* į̧̆
* į̧̃
* į̋
* į̒
* į̇
* į̈
* į̊
* į̆ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - aring (U+00E5): X=314,Y=711 (should be at cap-height 710?)
* - dcaron (U+010F): X=272,Y=1.5 (should be at baseline 0?)
* - l (U+006C): X=262,Y=711 (should be at cap-height 710?)
* - lacute (U+013A): X=262,Y=711 (should be at cap-height 710?)
* - lcaron (U+013E): X=262,Y=711 (should be at cap-height 710?)
* - uni013C (U+013C): X=262,Y=711 (should be at cap-height 710?)
* - ldot (U+0140): X=262,Y=711 (should be at cap-height 710?)
* - lslash (U+0142): X=262,Y=711 (should be at cap-height 710?)
* - germandbls (U+00DF): X=227,Y=-2 (should be at baseline 0?)
* - t (U+0074): X=522,Y=-2 (should be at baseline 0?)
* - tbar (U+0167): X=522,Y=-2 (should be at baseline 0?)
* - tcaron (U+0165): X=522,Y=-2 (should be at baseline 0?)
* - uni0163 (U+0163): X=522,Y=-2 (should be at baseline 0?)
* - uni021B (U+021B): X=522,Y=-2 (should be at baseline 0?)
* - uring (U+016F): X=302,Y=711 (should be at cap-height 710?)
* - uni013C.loclMAH: X=262,Y=711 (should be at cap-height 710?)
* - aring.cv01: X=292,Y=711 (should be at cap-height 710?)
* - fi (U+FB01): X=137,Y=712 (should be at cap-height 710?)
* - fl (U+FB02): X=141,Y=712 (should be at cap-height 710?)
* - lambda (U+03BB): X=502,Y=-1 (should be at baseline 0?)
* - lambda (U+03BB): X=546,Y=-1 (should be at baseline 0?)
* - seven.dnom: X=222,Y=1 (should be at baseline 0?)
* - seven.dnom: X=293,Y=1 (should be at baseline 0?)
* - one.numr: X=330,Y=711 (should be at cap-height 710?)
* - one.numr: X=390,Y=711 (should be at cap-height 710?)
* - four.numr: X=288,Y=711 (should be at cap-height 710?)
* - four.numr: X=361,Y=711 (should be at cap-height 710?)
* - five.numr: X=190,Y=711 (should be at cap-height 710?)
* - five.numr: X=409,Y=711 (should be at cap-height 710?)
* - six.numr: X=289,Y=711 (should be at cap-height 710?)
* - six.numr: X=363,Y=711 (should be at cap-height 710?)
* - seven.numr: X=171,Y=711 (should be at cap-height 710?)
* - seven.numr: X=434,Y=711 (should be at cap-height 710?)
* - onehalf (U+00BD): X=157,Y=711 (should be at cap-height 710?)
* - onehalf (U+00BD): X=217,Y=711 (should be at cap-height 710?)
* - uni2153 (U+2153): X=157,Y=711 (should be at cap-height 710?)
* - uni2153 (U+2153): X=217,Y=711 (should be at cap-height 710?)
* - onequarter (U+00BC): X=157,Y=711 (should be at cap-height 710?)
* - onequarter (U+00BC): X=217,Y=711 (should be at cap-height 710?)
* - uni2155 (U+2155): X=157,Y=711 (should be at cap-height 710?)
* - uni2155 (U+2155): X=217,Y=711 (should be at cap-height 710?)
* - oneeighth (U+215B): X=157,Y=711 (should be at cap-height 710?)
* - oneeighth (U+215B): X=217,Y=711 (should be at cap-height 710?)
* - fiveeighths (U+215D): X=49,Y=711 (should be at cap-height 710?)
* - fiveeighths (U+215D): X=268,Y=711 (should be at cap-height 710?)
* - seveneighths (U+215E): X=23,Y=711 (should be at cap-height 710?)
* - seveneighths (U+215E): X=286,Y=711 (should be at cap-height 710?)
* - uni2088 (U+2088): X=374,Y=1 (should be at baseline 0?)
* - uni2088 (U+2088): X=231,Y=1 (should be at baseline 0?)
* - questiondown (U+00BF): X=173,Y=1 (should be at baseline 0?)
* - braceleft (U+007B): X=307.5,Y=1 (should be at baseline 0?)
* - braceright (U+007D): X=298.5,Y=1 (should be at baseline 0?)
* - at (U+0040): X=101.5,Y=2 (should be at baseline 0?)
* - at (U+0040): X=211,Y=1 (should be at baseline 0?)
* - ampersand (U+0026): X=310.5,Y=-2 (should be at baseline 0?)
* - Euro (U+20AC): X=545,Y=708 (should be at cap-height 710?)
* - Euro (U+20AC): X=545,Y=2 (should be at baseline 0?)
* - greaterequal (U+2265): X=80,Y=1 (should be at baseline 0?)
* - greaterequal (U+2265): X=526,Y=1 (should be at baseline 0?)
* - lessequal (U+2264): X=526,Y=1 (should be at baseline 0?)
* - lessequal (U+2264): X=80,Y=1 (should be at baseline 0?)
* - plusminus (U+00B1): X=50,Y=1 (should be at baseline 0?)
* - plusminus (U+00B1): X=556,Y=1 (should be at baseline 0?)
* - integral (U+222B): X=230,Y=-2 (should be at baseline 0?)
* - uni030A (U+030A): X=303,Y=711 (should be at cap-height 710?)
* - ring (U+02DA): X=303,Y=711 (should be at cap-height 710?)
* - uni25CF (U+25CF): X=303,Y=1 (should be at baseline 0?)
* - uni25CF (U+25CF): X=303,Y=1 (should be at baseline 0?)
* - circle (U+25CB): X=303,Y=1 (should be at baseline 0?)
* - circle (U+25CB): X=303,Y=1 (should be at baseline 0?) [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* dkshade (U+2593): Line(Line { p0: (603.0, -104.0), p1: (553.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, -104.0), p1: (253.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, -104.0), p1: (353.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, -104.0), p1: (153.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, -104.0), p1: (453.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, -104.0), p1: (53.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, -50.0), p1: (553.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, -104.0), p1: (503.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, -50.0), p1: (453.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, -104.0), p1: (403.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, -50.0), p1: (353.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, -104.0), p1: (303.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, -50.0), p1: (253.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, -104.0), p1: (203.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, -50.0), p1: (53.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, -50.0), p1: (153.0, -104.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, -104.0), p1: (103.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, -50.0), p1: (503.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, -50.0), p1: (403.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, -50.0), p1: (303.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, -50.0), p1: (203.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, -50.0), p1: (3.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, -50.0), p1: (103.0, -50.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 58.0), p1: (553.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 4.0), p1: (503.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 4.0), p1: (503.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 58.0), p1: (453.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 4.0), p1: (403.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 4.0), p1: (403.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 58.0), p1: (353.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 4.0), p1: (303.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 4.0), p1: (303.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 58.0), p1: (253.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 4.0), p1: (203.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 4.0), p1: (203.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 58.0), p1: (53.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 4.0), p1: (3.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 58.0), p1: (153.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 4.0), p1: (103.0, 4.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 4.0), p1: (103.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 58.0), p1: (553.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 58.0), p1: (253.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 58.0), p1: (353.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 58.0), p1: (153.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 58.0), p1: (453.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 58.0), p1: (53.0, 58.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 112.0), p1: (553.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 112.0), p1: (253.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 112.0), p1: (353.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 112.0), p1: (153.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 112.0), p1: (453.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 112.0), p1: (53.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 166.0), p1: (553.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 112.0), p1: (503.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 166.0), p1: (453.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 112.0), p1: (403.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 166.0), p1: (353.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 112.0), p1: (303.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 166.0), p1: (253.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 112.0), p1: (203.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 166.0), p1: (53.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 166.0), p1: (153.0, 112.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 112.0), p1: (103.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 166.0), p1: (503.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 166.0), p1: (403.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 166.0), p1: (303.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 166.0), p1: (203.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 166.0), p1: (3.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 166.0), p1: (103.0, 166.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 274.0), p1: (553.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 220.0), p1: (503.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 220.0), p1: (503.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 274.0), p1: (453.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 220.0), p1: (403.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 220.0), p1: (403.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 274.0), p1: (353.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 220.0), p1: (303.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 220.0), p1: (303.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 274.0), p1: (253.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 220.0), p1: (203.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 220.0), p1: (203.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 274.0), p1: (53.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 220.0), p1: (3.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 274.0), p1: (153.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 220.0), p1: (103.0, 220.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 220.0), p1: (103.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 274.0), p1: (553.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 274.0), p1: (253.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 274.0), p1: (353.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 274.0), p1: (153.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 274.0), p1: (453.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 274.0), p1: (53.0, 274.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 328.0), p1: (553.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 328.0), p1: (253.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 328.0), p1: (353.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 328.0), p1: (153.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 328.0), p1: (453.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 328.0), p1: (53.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 382.0), p1: (553.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 328.0), p1: (503.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 382.0), p1: (453.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 328.0), p1: (403.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 382.0), p1: (353.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 328.0), p1: (303.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 382.0), p1: (253.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 328.0), p1: (203.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 382.0), p1: (53.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 382.0), p1: (153.0, 328.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 328.0), p1: (103.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 382.0), p1: (503.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 382.0), p1: (403.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 382.0), p1: (303.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 382.0), p1: (203.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 382.0), p1: (3.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 382.0), p1: (103.0, 382.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 490.0), p1: (553.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 436.0), p1: (503.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 436.0), p1: (503.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 490.0), p1: (453.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 436.0), p1: (403.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 436.0), p1: (403.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 490.0), p1: (353.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 436.0), p1: (303.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 436.0), p1: (303.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 490.0), p1: (253.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 436.0), p1: (203.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 436.0), p1: (203.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 490.0), p1: (53.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 436.0), p1: (3.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 490.0), p1: (153.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 436.0), p1: (103.0, 436.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 436.0), p1: (103.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 490.0), p1: (253.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 490.0), p1: (153.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 490.0), p1: (53.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 490.0), p1: (553.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 490.0), p1: (453.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 490.0), p1: (353.0, 490.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 544.0), p1: (553.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 544.0), p1: (253.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 544.0), p1: (353.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 544.0), p1: (153.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 544.0), p1: (453.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 544.0), p1: (53.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 598.0), p1: (553.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 544.0), p1: (503.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 598.0), p1: (453.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 544.0), p1: (403.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 598.0), p1: (353.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 544.0), p1: (303.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 598.0), p1: (253.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 544.0), p1: (203.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 598.0), p1: (53.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 598.0), p1: (153.0, 544.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 544.0), p1: (103.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 598.0), p1: (503.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 598.0), p1: (403.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 598.0), p1: (303.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 598.0), p1: (203.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 598.0), p1: (3.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 598.0), p1: (103.0, 598.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 706.0), p1: (553.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 652.0), p1: (503.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 652.0), p1: (503.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 706.0), p1: (453.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 652.0), p1: (403.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 652.0), p1: (403.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 706.0), p1: (353.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 652.0), p1: (303.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 652.0), p1: (303.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 706.0), p1: (253.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 652.0), p1: (203.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 652.0), p1: (203.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 706.0), p1: (53.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 652.0), p1: (3.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 706.0), p1: (153.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 652.0), p1: (103.0, 652.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 652.0), p1: (103.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 706.0), p1: (553.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 706.0), p1: (253.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 706.0), p1: (353.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 706.0), p1: (153.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 706.0), p1: (453.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 706.0), p1: (53.0, 706.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (603.0, 760.0), p1: (553.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 760.0), p1: (253.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 760.0), p1: (353.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 760.0), p1: (153.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 760.0), p1: (453.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 760.0), p1: (53.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 814.0), p1: (553.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (503.0, 760.0), p1: (503.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 814.0), p1: (453.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (403.0, 760.0), p1: (403.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 814.0), p1: (353.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (303.0, 760.0), p1: (303.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 814.0), p1: (253.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (203.0, 760.0), p1: (203.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 814.0), p1: (53.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 814.0), p1: (153.0, 760.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (103.0, 760.0), p1: (103.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (553.0, 814.0), p1: (503.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (453.0, 814.0), p1: (403.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (353.0, 814.0), p1: (303.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (253.0, 814.0), p1: (203.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (53.0, 814.0), p1: (3.0, 814.0) }) has the same coordinates as a previous segment.
* dkshade (U+2593): Line(Line { p0: (153.0, 814.0), p1: (103.0, 814.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (317.0, 170.0), p1: (253.0, 180.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (203.0, 230.0), p1: (193.0, 294.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (317.0, 540.0), p1: (253.0, 530.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (555.0, 230.0), p1: (565.0, 294.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (193.0, 416.0), p1: (203.0, 480.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (555.0, 480.0), p1: (565.0, 416.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (441.0, 540.0), p1: (505.0, 530.0) }) has the same coordinates as a previous segment.
* uni2318 (U+2318): Line(Line { p0: (505.0, 180.0), p1: (441.0, 170.0) }) has the same coordinates as a previous segment. [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'PAPR' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] fonts/variable</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/variable/PaperMono[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, coptic, math
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: coptic, canadian-aboriginal, duployan, hebrew, todhri, syriac, tai-le, malayalam, old-permic, math, tifinagh
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0312 COMBINING TURNED COMMA ABOVE: try adding math
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math
* U+039B GREEK CAPITAL LETTER LAMDA: try adding one of: greek, math, elbasan
* U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, math, greek
* U+03BB GREEK SMALL LETTER LAMDA: try adding one of: greek, math
* U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math
* U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi
* U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2070 SUPERSCRIPT ZERO: try adding math
* U+2074 SUPERSCRIPT FOUR: try adding math
* U+2075 SUPERSCRIPT FIVE: try adding math
* U+2076 SUPERSCRIPT SIX: try adding math
* U+2077 SUPERSCRIPT SEVEN: try adding math
* U+2078 SUPERSCRIPT EIGHT: try adding math
* U+2079 SUPERSCRIPT NINE: try adding math
* U+2080 SUBSCRIPT ZERO: try adding math
* U+2081 SUBSCRIPT ONE: try adding math
* U+2082 SUBSCRIPT TWO: try adding math
* U+2083 SUBSCRIPT THREE: try adding math
* U+2084 SUBSCRIPT FOUR: try adding math
* U+2085 SUBSCRIPT FIVE: try adding math
* U+2086 SUBSCRIPT SIX: try adding math
* U+2087 SUBSCRIPT SEVEN: try adding math
* U+2088 SUBSCRIPT EIGHT: try adding math
* U+2089 SUBSCRIPT NINE: try adding math
* U+2116 NUMERO SIGN: try adding cyrillic
* U+2117 SOUND RECORDING COPYRIGHT: try adding math
* U+2153 VULGAR FRACTION ONE THIRD: try adding symbols
* U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols
* U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols
* U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols
* U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols
* U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols
* U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
* U+2195 UP DOWN ARROW: try adding one of: symbols, math
* U+2196 NORTH WEST ARROW: try adding one of: math, symbols
* U+2197 NORTH EAST ARROW: try adding one of: math, symbols
* U+2198 SOUTH EAST ARROW: try adding one of: math, symbols
* U+2199 SOUTH WEST ARROW: try adding one of: symbols, math
* U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math
* U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math
* U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math
* U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B4 RIGHTWARDS ARROW WITH CORNER DOWNWARDS: try adding math
* U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math
* U+21B9 LEFTWARDS ARROW TO BAR OVER RIGHTWARDS ARROW TO BAR: try adding math
* U+21C6 LEFTWARDS ARROW OVER RIGHTWARDS ARROW: try adding math
* U+21E4 LEFTWARDS ARROW TO BAR: try adding math
* U+21E5 RIGHTWARDS ARROW TO BAR: try adding math
* U+21E7 UPWARDS WHITE ARROW: try adding symbols
* U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2236 RATIO: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+2303 UP ARROWHEAD: try adding symbols
* U+2318 PLACE OF INTEREST SIGN: try adding symbols
* U+2325 OPTION KEY: try adding symbols
* U+2326 ERASE TO THE RIGHT: try adding symbols
* U+2327 X IN A RECTANGLE BOX: try adding symbols
* U+232B ERASE TO THE LEFT: try adding symbols
* U+238B BROKEN CIRCLE WITH NORTHWEST ARROW: try adding symbols
* U+23CE RETURN SYMBOL: try adding symbols
* U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, yi, symbols
* U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi
* U+2462 CIRCLED DIGIT THREE: try adding one of: symbols, yi, mongolian
* U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi
* U+2464 CIRCLED DIGIT FIVE: try adding one of: symbols, yi, mongolian
* U+2465 CIRCLED DIGIT SIX: try adding one of: symbols, yi, mongolian
* U+2466 CIRCLED DIGIT SEVEN: try adding one of: symbols, mongolian, yi
* U+2467 CIRCLED DIGIT EIGHT: try adding one of: symbols, mongolian, yi
* U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, yi, symbols
* U+24EA CIRCLED DIGIT ZERO: try adding symbols
* U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols
* U+25CA LOZENGE: try adding one of: math, symbols
* U+25CB WHITE CIRCLE: try adding symbols
* U+25CF BLACK CIRCLE: try adding symbols
* U+25E6 WHITE BULLET: try adding symbols
* U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols
* U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols
* U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols
* U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols
* U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols
* U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols
* U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols
* U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols
* U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols
* U+3003 DITTO MARK: try adding one of: phags-pa, japanese, chinese-hongkong, yi, chinese-traditional, chinese-simplified
* U+301C WAVE DASH: try adding japanese

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, latin-ext, latin, symbols2 [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 14 | 8 | 111 | 49 | 
| 8% | 4% | 62% | 27% | 



