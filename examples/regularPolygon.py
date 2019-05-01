#!/usr/bin/env python
#coding:utf-8
# Author:  ya-induhvidual
# Purpose: svg regular_polygon example
# Modified
# Copyright (C) 2019, Christof Hanke
# based on hyperlnks.py in the same directory.
# all rights and Author on copied stuff see there 
# License: MIT License
from __future__ import unicode_literals

try:
    import svgwrite
    import svgwrite.extensions
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))
    import svgwrite
    import svgwrite.extensions



def regular_polygon(name, edges):
    dwg = svgwrite.Drawing(name, (200, 200), debug=True)
    # use the regular_polygon element
    reg_fac = svgwrite.extensions.RegularPolygonFactory(dwg)
    dwg.add(reg_fac.get(7,10,(100,100), fill="none", stroke_width=1, stroke="black"))
    dwg.save(pretty=True)

if __name__ == '__main__':
    regular_polygon("heptagon.svg", 7)
