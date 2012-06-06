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
    title = name + ': Example of stroke_linecap, stroke_linejoin'
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    # give the name of the example and a title.
    text = dwg.add(dwg.g(font_family="sans-serif", font_size=font_size, fill='black'))
    lines = dwg.add(dwg.g(stroke_width=10, stroke='green', fill='none'))

    text.add(dwg.text(title, insert=(0, (font_size + 5))))
    lines.add(dwg.line(start=(50, 100), end=(150, 100)))
    text.add(dwg.text("Default is butt", insert=('175', '100')))
    lines.add(dwg.line(start=(50, 130), end=(150, 130), stroke_linecap='butt'))
    text.add(dwg.text("stroke_linecap='butt'", insert=('175', '130')))
    lines.add(dwg.line(start=(50, 160), end=(150, 160), stroke_linecap='square'))
    text.add(dwg.text("stroke_linecap='square'", insert=('175', '160')))
    lines.add(dwg.line(start=(50, 190), end=(150, 190), stroke_linecap='round'))
    text.add(dwg.text("stroke_linecap='round'", insert=('175', '190')))

    lines.add(dwg.polyline([(50, 250), (50, 300), (75, 250), (100, 300), (120, 250), (150, 250), (150, 300)]))
    text.add(dwg.text("Default is miter", insert=('175', '280')))
    lines.add(dwg.polyline([(50, 350), (50, 400), (75, 350), (100, 400), (120, 350), (150, 350), (150, 400)],
        stroke_linejoin='miter'))
    text.add(dwg.text("stroke_linejoin='miter'", insert=('175', '380')))
    lines.add(dwg.polyline([(50, 450), (50, 500), (75, 450), (100, 500), (120, 450), (150, 450), (150, 500)],
        stroke_linejoin='bevel'))
    text.add(dwg.text("stroke_linejoin='bevel'", insert=('175', '480')))
    lines.add(dwg.polyline([(50, 550), (50, 600), (75, 550), (100, 600), (120, 550), (150, 550), (150, 600)],
        stroke_linejoin='round'))
    text.add(dwg.text("stroke_linejoin='round'", insert=('175', '580')))
    lines.add(dwg.polyline([(50, 650), (50, 700), (75, 650), (100, 700), (120, 650), (150, 650), (150, 700)],
        stroke_linejoin='round',  stroke_linecap='round'))
    text.add(dwg.text("stroke_linejoin='round', stroke_linecap='round'", insert=('175', '680')))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
