#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7

import sys
import svgwrite

#
# http://www.w3.org/TR/SVG/coords.html#Units
# The supported length unit identifiers are: em, ex, px, pt, pc, cm, mm, in, and percentages.
#
PROGNAME = sys.argv[0].rstrip('.py')

def create_svg(name):
    SVG_SIZE = 900
    FONT_SIZE = 20
    title1 = name + ': Example of units of length'
    title2 = name + ': Example of class Unit and import from svgwrite cm, mm'
    sample = (
        ('px', ' one user unit which may or may not be pixels. This is the default if no units are specified.'),
        ('pt', ' 1.25px.'),
        ('mm', ' 3.543307px.'),
        ('ex', " the current font's height of the character x."),
        ('%', ' percent of the size of the viewport.'),
        ('pc', ' 15px.'),
        ('em', " the current font's height."),
        ('cm', ' 35.43307px.'),
        ('in', ' 90px.')
        )
    dwg = svgwrite.Drawing(name, (SVG_SIZE, SVG_SIZE))
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    # give the name of the example and a title.
    y = FONT_SIZE + 5
    x = 5
    linespace = FONT_SIZE * 2
    group = dwg.add(dwg.g(font_family="serif", font_size=FONT_SIZE, fill='black'))
    group.add(dwg.text(title1, insert=(x, y)))
    for i, sample_item in enumerate(sample):
        y += linespace
        unit = sample_item[0]
        group.add(dwg.rect(insert=(0, y), size=('1' + unit, '3px'), fill='red'))
        group.add(dwg.text("size='1%s': %s" % sample_item, insert=('2in', y+3)))

    # Show the use of class Unit
    y += linespace
    textlines = (
        title2, 
        'The Unit class overrides the right hand multiply', 
        '2*3*cm returns the string "6cm"'
        )
    for txt in textlines:
        group.add(dwg.text(txt, insert=(x, y)))
        y += linespace
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
