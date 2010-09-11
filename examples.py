#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import svgwrite as svg

# svg.setup: define debug_mode and svg profile - optional
# baseProfile -- full, basic or tiny baseProfile (default: full)
# debug -- verify property names and property values (default: False)
svg.setup(baseProfile='tiny', debug=True)

def example_empty_drawing(name):
    drawing = svg.Drawing(filename=name)
    drawing.save()

def main():
    example_empty_drawing('example_empty_drawing.svg')

if __name__ == '__main__':
    main()