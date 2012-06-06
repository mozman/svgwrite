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

def create_svg(name):
    svg_size = 900
    font_size = 20
    title = name + ': Example of text_anchor (justified) text'
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    # give the name of the example and a title.
    dwg.add(dwg.text(title, insert=(0, (font_size + 5)),
            font_family="serif", font_size=font_size, fill='black'))
    # Show default
    dwg.add(dwg.text("No specified text_anchor means 'start' justified text", insert=('50%', font_size * 3),
        font_family="sans-serif", font_size=font_size, fill='black'))
    # add a circle to show the anchor point printing on top of the text.
    dwg.add(dwg.circle(('50%', font_size * 3), r='3px', fill='red'))
    for i, anchor in enumerate(['start', 'end', 'middle']):  # also 'inherit' which inherits from parent.
        dwg.add(dwg.text("text_anchor='" + anchor + "' means " + anchor + " justified text",
            insert=('50%', font_size * (i + 4)),
            text_anchor=anchor, font_family="sans-serif", font_size=font_size, fill='black'))
        # add a circle to show the anchor point printing on top of the text.
        dwg.add(dwg.circle(('50%', font_size * (i + 4)), r='3px', fill='red'))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
