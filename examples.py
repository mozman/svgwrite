#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import math

import svgwrite as svg
from svgwrite import cm, mm, rgb, deg

# svg.init: define debug_mode and svg profile - optional
# baseProfile -- full, basic or tiny baseProfile (default: full)
# debug -- verify property-names and property-values and for each element verify
#          valid subelements(default: False)
svg.parameter.set_debug()
svg.parameter.set_profile('full')

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

def example_koch_snowflake(name):
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
        sflake.add(svg.Polygon(points))
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

    svg.parameter.set_profile('tiny')

    # create a new drawing
    dwg = svg.Drawing(name, (imgx, imgy))

    # create a new <g /> element, wee will insert the snowflkae by the <use /> element
    # here we set stroke, fill and stroke-width for all subelements
    # attention: 'stroke-width' is not a valid Python identifier, so use 'stroke_witdth'
    #   underlines '_' will be converted to dashes '-', this is true for all svg-keyword-attributs
    # if no 'id' is given ( like svg.Group(id="sflake") ), an automatic generated 'id' will be used
    sflake = svg.Group(stroke="#000", fill="rgb(90%,90%,100%)", stroke_width=0.25)

    # add the <g /> element to the <defs /> element of the drawing
    dwg.defs.add(sflake)

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
    use_sflake = svg.Use(sflake)

    # you can transform each <use /> element
    use_sflake.rotate(15, center=(imgx/2, imgy/2))

    # insert snowflake by the <use /> element
    dwg.add(use_sflake)

    # and save the drawing
    dwg.save()


def main():
    example_empty_drawing('example_empty_drawing.svg')
    example_base_shapes_drawing('example_base_shapes_drawing.svg')
    example_use_drawing('example_use_drawing.svg')
    example_koch_snowflake('example_koch_snowflake.svg')

if __name__ == '__main__':
    main()