#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import svgwrite as svg
from svgwrite import cm, mm, rgb, deg

# svg.init: define debug_mode and svg profile - optional
# baseProfile -- full, basic or tiny baseProfile (default: full)
# debug -- verify property-names and property-values and for each element verify
#          valid subelements(default: False)
svg.init(baseProfile='full', debug=True)

def example_empty_drawing(name):
    drawing = svg.Drawing(filename=name)
    drawing.save()

def example_base_shapes_drawing(name):
    drawing = svg.Drawing(filename=name)
    hlines = drawing.group(id='hlines', stroke='green')
    for y in range(20):
        hlines.add(svg.Line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    vlines = drawing.group(id = 'vline', stroke='blue')
    for x in range(17):
        vlines.add(svg.Line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
    shapes = drawing.group(id='shapes', fill='red')
    shapes.add(svg.Rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm)))
    shapes.add(svg.Circle(center=(15*cm, 8*cm), r='2.5cm', fill='blue'))
    shapes.add(svg.Ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
    drawing.save()

def example_use_drawing(name):
    w, h = '100%', '100%'
    dwg = svg.Drawing(filename=name, size=(w, h))
    dwg.add(svg.Rect(insert=(0,0), size=(w, h), fill='lightgray', stroke='black'))
    g = dwg.defs.group(id='g001')
    unit=40
    g.add(svg.Rect((0,0), (unit, unit)))
    for y in range(10):
        for x in range(5):
            x1 = 2*unit+2*unit*x
            y1 = 2*unit+2*unit*y
            cx = x1 + unit/2
            cy = y1 + unit/2
            cval = (y*5 + x)*2
            u = svg.Use(g, insert=(x1, y1), fill=rgb(cval, cval, cval))
            u.rotate(y*5+x, center=(cx, cy))
            dwg.add(u)
    dwg.save()

def main():
    example_empty_drawing('example_empty_drawing.svg')
    example_base_shapes_drawing('example_base_shapes_drawing.svg')
    example_use_drawing('example_use_drawing.svg')
if __name__ == '__main__':
    main()