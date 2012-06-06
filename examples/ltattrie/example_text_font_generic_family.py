#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7

import sys
import svgwrite

# http://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#propdef-font-family
# 'serif', 'sans-serif', 'cursive', 'fantasy', and 'monospace' from the CSS specification

PROGNAME = sys.argv[0].rstrip('.py')


def create_svg(name):
    svg_size = 900
    font_size = 20
    title = name + ': Example of text using generic family fonts'
    font_family_sample = (('serif', 'have finishing strokes, flared or tapering ends.'),
        ('sans-serif', 'have stroke endings that are plain.'),
        ('cursive', 'the characters are partially or completely connected'),
        ('fantasy', ' primarily decorative characters.'),
        ('monospace', 'all characters have the same fixed width.'))
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    # give the name of the example and a title.
    dwg.add(dwg.text(title, insert=(0, (font_size + 5)),
            font_family="serif", font_size=font_size, fill='black'))
    for i, font_family_item in enumerate(font_family_sample):
        dwg.add(dwg.text("font_family='" + font_family_item[0] + "': " + font_family_item[1],
            insert=(font_size, font_size * (i * 2 + 4)),
            font_family=font_family_item[0], font_size=font_size, fill='black'))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
