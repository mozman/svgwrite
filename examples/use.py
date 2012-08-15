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
from svgwrite import cm, mm, rgb, deg

def use(name):
    # Shows how to use the 'use' element.
    #
    w, h = '100%', '100%'
    dwg = svgwrite.Drawing(filename=name, size=(w, h), debug=True)
    dwg.add(dwg.rect(insert=(0,0), size=(w, h), fill='lightgray', stroke='black'))

    # add a group of graphic elements to the defs section of the main drawing
    g = dwg.defs.add(dwg.g(id='g001'))

    unit=40
    g.add(dwg.rect((0,0), (unit, unit)))
    for y in range(10):
        for x in range(5):
            x1 = 2*unit+2*unit*x
            y1 = 2*unit+2*unit*y
            cx = x1 + unit/2
            cy = y1 + unit/2
            cval = (y*5 + x)*2

            # reference the group by the 'use' element, you can overwrite
            # graphical properties, ...
            u = dwg.use(g, insert=(x1, y1), fill=rgb(cval, cval, cval))
            # ... and you can also transform the the whole reference object.
            u.rotate(y*5+x, center=(cx, cy))
            dwg.add(u)
    dwg.save()

if __name__ == '__main__':
    use("use.svg")
