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

def radialGradient(name):
    dwg = svgwrite.Drawing(name, size=('20cm', '15cm'), profile='full', debug=True)

    # set user coordinate space
    dwg.viewbox(width=200, height=150)

    # create a new radialGradient element and add it to the defs section of
    # the drawing
    gradient1 = dwg.defs.add(dwg.radialGradient())
    # define the gradient from red to white
    gradient1.add_stop_color(0, 'red').add_stop_color(1, 'white')
    # use gradient for filling the rect
    dwg.add(dwg.rect((10,10), (50,50), fill=gradient1.get_paint_server()))

    wave = dwg.defs.add(dwg.radialGradient())
    wave.add_colors(['blue', 'lightblue'] * 8)
    dwg.add(dwg.rect((70,10), (50,50), fill=wave.get_paint_server()))

    dwg.save()

if __name__ == '__main__':
    radialGradient("radialGradient.svg")
