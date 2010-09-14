#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import svgwrite as svg
from svgwrite import cm, mm
from svgwrite.utils import rgb

# svg.init: define debug_mode and svg profile - optional
# baseProfile -- full, basic or tiny baseProfile (default: full)
# debug -- verify property names and property values (default: False)
svg.init(baseProfile='tiny', debug=True)

def example_empty_drawing(name):
    drawing = svg.Drawing(filename=name)
    drawing.save()

def example_base_shapes_drawing(name):
    svg.init('full', True)
    drawing = svg.Drawing(filename=name)
    for y in range(20):
        drawing.append(svg.Line(start=(cm(2), cm(2+y)), end=(cm(18), cm(2+y)), stroke='green'))
    for x in range(17):
        drawing.append(svg.Line(start=(cm(2+x), cm(2)), end=(cm(2+x), cm(21)), stroke='blue'))

    drawing.append(svg.Rect(insert=(cm(5),cm(5)), size=(mm(45),mm(45))))
    drawing.append(svg.Circle(center=(cm(15), cm(8)), r='2.5cm', fill=rgb(100, 0, 0, '%')))
    drawing.append(svg.Ellipse(center=(cm(10), cm(15)), rx='5cm', ry='17mm'))
    drawing.save()

def main():
    example_empty_drawing('example_empty_drawing.svg')
    example_base_shapes_drawing('example_base_shapes_drawing.svg')

if __name__ == '__main__':
    main()