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

import math
import svgwrite

def koch_snowflake(name):
    # Koch Snowflake and Sierpinski Triangle combination fractal using recursion
    # ActiveState Recipe 577156
    # Created by FB36 on Sat, 27 Mar 2010 (MIT)
    # http://code.activestate.com/recipes/577156-koch-snowflake-and-sierpinski-triangle-combination/

    def tf (x0, y0, x1, y1, x2, y2):
        a = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        b = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        c = math.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)

        if (a < stop_val) or (b < stop_val) or (c < stop_val):
            return

        x3 = (x0 + x1) / 2
        y3 = (y0 + y1) / 2
        x4 = (x1 + x2) / 2
        y4 = (y1 + y2) / 2
        x5 = (x2 + x0) / 2
        y5 = (y2 + y0) / 2
        points = [(x3, y3), (x4, y4), (x5, y5)]

        # append new polygon to snowflake element
        snowflake.add(dwg.polygon(points))
        tf(x0, y0, x3, y3, x5, y5)
        tf(x3, y3, x1, y1, x4, y4)
        tf(x5, y5, x4, y4, x2, y2)

    def sf (ax, ay, bx, by):
        f = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)

        if f < 1.:
            return

        f3 = f / 3
        cs = (bx - ax) / f
        sn = (by - ay) / f
        cx = ax + cs * f3
        cy = ay + sn * f3
        h = f3 * math.sqrt(3) / 2
        dx = (ax + bx) / 2 + sn * h
        dy = (ay + by) / 2 - cs * h
        ex = bx - cs * f3
        ey = by - sn * f3
        tf(cx, cy, dx, dy, ex, ey)
        sf(ax, ay, cx, cy)
        sf(cx, cy, dx, dy)
        sf(dx, dy, ex, ey)
        sf(ex, ey, bx, by)

    # const values
    stop_val = 8.
    imgx = 512
    imgy = 512

    # create a new drawing
    dwg = svgwrite.Drawing(name, (imgx, imgy), profile='tiny', debug=True)

    # create a new <g /> element, we will insert the snowflake by the <use /> element
    # here we set stroke, fill and stroke-width for all subelements
    # attention: 'stroke-width' is not a valid Python identifier, so use 'stroke_witdth'
    #   underlines '_' will be converted to dashes '-', this is true for all svg-keyword-attributs
    # if no 'id' is given ( like dwg.g(id="sflake") ), an automatic generated 'id' will be generated
    snowflake = dwg.g(stroke="blue", fill="rgb(90%,90%,100%)", stroke_width=0.25)

    # add the <g /> element to the <defs /> element of the drawing
    dwg.defs.add(snowflake)

    mx2 = imgx / 2
    my2 = imgy / 2
    r = my2
    a = 2 * math.pi / 3
    for k in range(3):
        x0 = mx2 + r * math.cos(a * k)
        y0 = my2 + r * math.sin(a * k)
        x1 = mx2 + r * math.cos(a * (k + 1))
        y1 = my2 + r * math.sin(a * (k + 1))
        sf(x0, y0, x1, y1)

    x2 = mx2 + r * math.cos(a)
    y2 = my2 + r * math.sin(a)
    tf(x0, y0, x1, y1, x2, y2)

    # create an <use /> element
    use_snowflake = dwg.use(snowflake)

    # you can transform each <use /> element
    # use_snowflake.rotate(15, center=(imgx/2, imgy/2))

    # insert snowflake by the <use /> element
    dwg.add(use_snowflake)

    # and save the drawing
    dwg.save()

if __name__ == '__main__':
    koch_snowflake("koch_snowflake.svg")
