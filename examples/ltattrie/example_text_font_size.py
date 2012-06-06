#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7

import sys
import svgwrite

PROGNAME = sys.argv[0].rstrip('.py')

# http://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-size-props

def create_svg(name):
    svg_size = 900
    font_size = 20
    title = name + ': Example of text font_sizes'
    sample = (8, 10, 12, 15, 20, 30, 40, 50)
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    # give the name of the example and a title.
    y = font_size + 5
    dwg.add(dwg.text(title, insert=(0, y),
            font_family="serif", font_size=font_size, fill='black'))
    for i, item in enumerate(sample):
        # font_size has many properties and adjustments which can be done. See the web page listed
        # above for the complete description.
        y += item + 10
        dwg.add(dwg.text("font_size='" + str(item) + "'",
            insert=(font_size, y),
            font_family="serif", font_size=item, fill='black'))
    y += font_size + 10
    dwg.add(dwg.text('Since svg fonts are usually vectors, font_size can be very large.', insert=(0, y),
            font_family="serif", font_size=font_size, fill='black'))
    y += font_size + 10
    # Show just the top of the single letter 'f'. The whole letter will not fit in the view area.
    dwg.add(dwg.text('Enlarged small parts of a character are like looking through a microscope. (font_size=4000)',
        insert=(0, y), font_family="serif", font_size=font_size, fill='black'))
    y += 2800 + 10
    # Note the insert value of x is a negative number which is actually outside the view area.
    dwg.add(dwg.text('f', insert=(-1100, y), font_family="serif", font_size=4000, fill='black'))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
