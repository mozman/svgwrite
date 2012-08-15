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
from svgwrite import rgb

def mandelbrot(name):
    ## {{{ http://code.activestate.com/recipes/577111/ (r2)
    # Mandelbrot fractal
    # FB - 201003254

    def putpixel(pos, color):
        mandelbrot_group.add(dwg.circle(center=pos, r=.5, fill=color))

    # image size
    imgx = 160
    imgy = 100

    # drawing defines the output size
    dwg = svgwrite.Drawing(name, ('32cm', '20cm'), debug=True)

    # define a user coordinate system with viewbox()
    dwg.viewbox(0, 0, imgx, imgy)

    mandelbrot_group = dwg.add(dwg.g(stroke_width=0, stroke='none'))

    # drawing area
    xa = -2.0
    xb = 1.0
    ya = -1.5
    yb = 1.5
    maxIt = 255 # max iterations allowed

    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1)  + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1)  + xa
            z = zx + zy * 1j
            c = z
            for i in range(maxIt):
                if abs(z) > 2.0: break
                z = z * z + c
            putpixel((x, y), rgb(i % 4 * 64, i % 8 * 32, i % 16 * 16))
    dwg.save()
    ## end of http://code.activestate.com/recipes/577111/ }}}

if __name__ == '__main__':
    mandelbrot("mandelbrot.svg")
