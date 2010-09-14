n= ( "font-weight", "glyph-orientation-horizontal", "glyph-orientation-vertical",
 "image-rendering", "kerning", "letter-spacing", "lighting-color", "marker-end",
 "marker-mid", "marker-start", "mask", "opacity", "overflow", "pointer-events",
 "shape-rendering", "stop-color", "stop-opacity", "stroke", "stroke-dasharray",
 "stroke-dashoffset", "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
 "stroke-opacity", "stroke-width", "text-anchor", "text-decoration", "text-rendering",
 "unicode-bidi", "visibility", "word-spacing", "writing-mode")

f = open('props.txt', 'w')
for a in n:
    s = a.split('-')
    b = "".join([t.capitalize() for t in s])
    f.write("* [[http://www.w3.org/TR/SVG11/text.html#%sProperty | %s]]\n" % (b, a))
f.close()