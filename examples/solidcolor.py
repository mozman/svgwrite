#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 26.10.2016
# Copyright (C) 2016, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import svgwrite

def solid_color(name):
    dwg = svgwrite.Drawing(name, size=('20cm', '15cm'), profile='tiny', debug=True)

    # set user coordinate space
    dwg.viewbox(width=200, height=150)
    my_color = dwg.defs.add(dwg.solidColor(color='red'))
    dwg.add(dwg.circle((100, 100), 50, fill=my_color.get_paint_server()))
    dwg.save()

if __name__ == '__main__':
    solid_color("solid_color.svg")
