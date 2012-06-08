from __future__ import print_function

import sys
import os
import colorsys
import svgwrite

PROGNAME = sys.argv[0].rstrip('.py')
RGB_TXT = 'rgb.txt'

# To Do
#   Automate the file name and title and axis swatch_y
#   Create multiple layers and put the third component divided into 10 layers?
#   Create new examples for svgwrite
#     text follow path based on http://www.w3.org/TR/SVG/text.html example toap01
#     text stroke, stroke colour
#     text font names
#     colour names, colour by rbg, colour by hex, colour by hsl.
#     clipping and masking perhaps use http://www.w3.org/TR/SVG/masking.html example opacity01 
#     multishapes with various opacities overlapping. ex rounded corner rectangles.
#     Are clones an inkscape feature?
#     View examples by following links at http://tavmjong.free.fr/INKSCAPE/
#     Table of contents page to show example svgs. Links go to each svg.
#        It does this by looking at the current dir and listing *.svg  or example*.svg
#     Drop shadow?
#     Create sample programs which match the svg test in the www.? pages
#     Complain / document that 
#          sq_created.translate(x, (y+square_size))
#          sq_created.scale(1, -1)   is not the same as 
#          sq_created.scale(1, -1)
#          sq_created.translate(x, (y+square_size))
#       www.? said that evaluation is done RIGHT to LEFT! But the program puts the most recent on
#       the left so what appears in the program to happen first actually happens last! To me this
#       should be changed and is likely that the author of svgwrite did not know of the Right to
#       Left evaluation.  Needs example from www.?
#     Note that sq_created.scale='(1, -1)' does not work and is incorrect but does not produce an
#     error. The program ignores it and caused me a lot of debugging time. 
#
# read the name and colour data provided by xkcd and change to svg diagram.
# http://blog.xkcd.com/2010/05/03/color-survey-results/
#
# The file format is tab delimeted: colour name tab hex colour tab newline
# max name length =26
#
# http://stackoverflow.com/questions/214359/converting-hex-to-rgb-and-vice-versa
# A hex value is just RGB numbers represented in hexadecimal. So you just have to take each pair of hex digits 
# and convert them to decimal.  Example: #FF6400 = RGB(0xFF, 0x64, 0x00) = RGB(255, 100, 0)

def hex_to_rgb(value):
    value = value.lstrip('#')
    def get_int(pos):
        start = pos * 2
        return int(value[start:start+2], 16)
    return get_int(0), get_int(1), get_int(2)

def create_svg(name):
    swatch_w = 10 # swatch width
    swatch_h = 10 # swatch height

    if not os.path.exists(RGB_TXT):
      print("Error.  The data file is not readable. File name is: %s" % RGB_TXT)
      sys.exit(1)

    # 1050 = 1000 width of color + width of last rectangle which might start at 1000 + approx width of font name text
    svg_size = 1050
    dwg = svgwrite.Drawing(name, (svg_size, svg_size))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='grey'))
    dwg.add(dwg.text('XKCD.com color name survey x=hue, y=lightness', insert=(svg_size/2, '28px'),
        text_anchor='middle', font_family="sans-serif", font_size='25px', fill='black'))

    # http://www.svgbasics.com/using_fonts.html
    # http://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#propdef-font-family
    # 'serif', 'sans-serif', 'cursive', 'fantasy', and 'monospace' from the CSS specification
    # You can also use other family names like "Times", "Baskerville", "Verdena", and "Symbol." I got those names from the CSS specification and some experimenting, but I'm looking for more.
    # 'font-weight' Value:  	normal | bold + others.

    for line_count, line in enumerate(open(RGB_TXT)):
        colour_item = line.split('\t')
        # strip the trailing newline \n char then split by the tab chars
        colour_item = line.strip().split('\t')
        rgb = hex_to_rgb(colour_item[1])
        # hsl is also called hls
        #hsl = 
        #h, l, s = colorsys.rgb_to_hls(r, g, b)
        # rgb values are integer but colorsys wants float(0..1) and returns float
        h, l, s = colorsys.rgb_to_hls(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
        hsl = (h, s, l)
        swatch_x=int(h*1000)
        # hue by lightness
        swatch_y=svg_size - 25 - int(l*1000)
        # hue by saturation
        #swatch_y=int(s*1000) + 25
        ## svg can handle colors in hex mode so no conversion is necessary.
        group_rec_text = dwg.add(dwg.g())
        group_rec_text.add(dwg.rect(insert=(swatch_x, swatch_y), size=(swatch_w, swatch_h), rx=None, ry=None,
            fill=colour_item[1]))
        # text is to start on the right side of swatch in the middle.
        tx_x = int(swatch_x + swatch_w)
        tx_y = int(swatch_y + swatch_h/2)
        group_rec_text.add(dwg.text(colour_item[0], insert = (tx_x, tx_y),
            font_family="sans-serif", font_size='6px', fill='white', stroke='black', stroke_width='0.1px'))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '_hl.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
