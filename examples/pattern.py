#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite

def pattern(name):
    dwg = svgwrite.Drawing(name, size=('20cm', '15cm'), profile='full', debug=True)

    # set user coordinate space
    dwg.viewbox(width=200, height=150)
    pattern = dwg.defs.add(
        dwg.pattern(size=(20, 20), patternUnits="userSpaceOnUse"))
    pattern.add(dwg.circle((10, 10), 5))
    dwg.add(dwg.circle((100, 100), 50, fill=pattern.get_paint_server()))
    dwg.save()

if __name__ == '__main__':
    pattern("pattern.svg")
