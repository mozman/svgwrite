#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import math

import svgwrite
from svgwrite import cm, mm, rgb, deg

DEBUG = True

def empty_drawing(name):
    drawing = svgwrite.Drawing(filename=name, debug=DEBUG)
    drawing.save()

def base_shapes_drawing(name):
    dwg = svgwrite.Drawing(filename=name, debug=DEBUG)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(20):
        hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(17):
        vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
    shapes = dwg.add(dwg.g(id='shapes', fill='red'))

    # set presentation attributes at object creation as SVG-Attributes
    shapes.add(dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue', stroke_width=3))

    # override the 'fill' attribute of the parent group 'shapes'
    shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm), fill='blue', stroke='red', stroke_width=3))

    # or set presentation attributes by helper functions of the Presentation-Mixin
    ellipse = shapes.add(dwg.ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
    ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])
    dwg.save()

def use_drawing(name):
    w, h = '100%', '100%'
    dwg = svgwrite.Drawing(filename=name, size=(w, h), debug=DEBUG)
    dwg.add(dwg.rect(insert=(0,0), size=(w, h), fill='lightgray', stroke='black'))
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
            u = dwg.use(g, insert=(x1, y1), fill=rgb(cval, cval, cval))
            u.rotate(y*5+x, center=(cx, cy))
            dwg.add(u)
    dwg.save()

def marker_drawing(name):
    dwg = svgwrite.Drawing(name, profile='full', debug=True)

    # create a new marker object
    # markerUnits='userSpaceOnUse'
    marker = dwg.marker(insert=(5,5), size=(10,10))

    # red point as marker
    marker.add(dwg.circle((5, 5), r=5, fill='red'))

    # add marker to defs section of the drawing
    dwg.defs.add(marker)

    # create a new line object
    line = dwg.add(dwg.polyline(
        [(10, 10), (50, 20), (70, 50), (100, 30)],
        stroke='black', fill='none'))

    # set marker (start, mid and end markers are the same)
    line.set_markers(marker)

    # or set markers direct as SVG Attributes 'marker-start', 'marker-mid',
    # 'marker-end' or 'marker' if all markers are the same.
    # line['marker'] = marker.get_funciri()
    dwg.save()

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
    dwg = svgwrite.Drawing(name, (imgx, imgy), profile='tiny', debug=DEBUG)

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
    dwg = svgwrite.Drawing(name, ('32cm', '20cm'), debug=DEBUG)

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


LevyDragon = {'length':1, 'numAngle':4, 'level':16, 'init': 'FX',
              'target': 'X', 'replacement': 'X+YF+', 'target2': 'Y',
              'replacement2': '-FX-Y'}

KochSnowflake = {'length':1, 'numAngle':6, 'level':6, 'init': 'F++F++F',
                 'target': 'F', 'replacement': 'F-F++F-F', 'target2': '',
                 'replacement2': ''}

LevyCurve = {'length':1, 'numAngle':8, 'level':17, 'init': 'F',
             'target': 'F', 'replacement': '+F--F+', 'target2': '',
             'replacement2': ''}

HilbertSpaceFillingCurve = {'length':1, 'numAngle':4, 'level':5, 'init': 'L',
             'target': 'L', 'replacement': '+RF-LFL-FR+', 'target2': 'R',
             'replacement2': '-LF+RFR+FL-'}

def LSystem(name, formula=LevyCurve):
    ## {{{ http://code.activestate.com/recipes/577159/ (r1)
    # L-System Fractals
    # FB - 201003276
    # image size

    # generate the fractal drawing string
    def _LSystem(formula):
        state = formula['init']
        target = formula['target']
        replacement = formula['replacement']
        target2 = formula['target2']
        replacement2 = formula['replacement2']
        level = formula['level']

        for counter in range(level):
            state2 = ''
            for character in state:
                if character == target:
                    state2 += replacement
                elif character == target2:
                    state2 += replacement2
                else:
                    state2 += character
            state = state2
        return state
    print("creating: %s\n" % name)
    xmin, ymin = (100000, 100000)
    xmax, ymax = (-100000, -100000)

    numAngle = formula['numAngle']
    length = formula['length']
    fractal = _LSystem(formula)
    na = 2.0 * math.pi / numAngle
    sn = []
    cs = []
    for i in range(numAngle):
        sn.append(math.sin(na * i))
        cs.append(math.cos(na * i))

    x = 0.0
    y = 0.0

    # jx = int((x - xa) / (xb - xa) * (imgx - 1))
    # jy = int((y - ya) / (yb - ya) * (imgy - 1))
    k = 0
    dwg = svgwrite.Drawing(name, debug=DEBUG)
    curve = dwg.polyline(points=[(x, y)], stroke='green', fill='none', stroke_width=0.1)
    for ch in fractal:
        if ch == 'F':
            # turtle forward(length)
            x +=  length * cs[k]
            y += length * sn[k]

            curve.points.append( (x, y) )

            # find maxima
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
        elif ch == '+':
            # turtle right(angle)
            k = (k + 1) % numAngle
        elif ch == '-':
            # turtle left(angle)
            k = ((k - 1) + numAngle) % numAngle
    print("L-System with %d segements.\n" % (len(curve.points)-1))
    dwg.viewbox(xmin, ymin, xmax-xmin, ymax-ymin)
    dwg.add(curve)
    dwg.save()
## end of http://code.activestate.com/recipes/577159/ }}}

def simple_text(name):
    dwg = svgwrite.Drawing(name, (200, 200), debug=DEBUG)
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text("This is a Test!", (10,20)))
    # 'x', 'y', 'dx', 'dy' and 'rotate' has to be a <list> or a <tuple>!!!
    # 'param'[0] .. first letter, 'param'[1] .. second letter, and so on
    # if there are more letters than values, the last list-value is used
    #
    # different 'y' coordinates does not work with Firefox 3.6
    paragraph.add(dwg.text("This is a Test!", x=[10], y=[40, 45, 50, 55, 60]))

    # different formats can be used by the TSpan element
    # The atext.tspan(...) method is a shortcut for: atext.add(dwg.tspan(...))
    atext = dwg.text("A", insert=(10, 80))

    # text color is set by the 'fill' property and 'stroke sets the outline color.
    atext.add(dwg.tspan(' Word', font_size='1.5em', fill='red'))
    atext.add(dwg.tspan(' is a Word!', dy=['1em'], font_size='0.7em', fill='green'))
    paragraph.add(atext)
    dwg.save()

def main():
    longrun = False
    # short time running
    print("start short time running examples!\n")

    print("start: example_empty_drawing.svg\n")
    empty_drawing('example_empty_drawing.svg')

    print("start: example_simple_text.svg\n")
    simple_text('example_simple_text.svg')

    print("start: example_base_shapes_drawing.svg\n")
    base_shapes_drawing('example_base_shapes_drawing.svg')

    print("start: example_use_drawing.svg\n")
    use_drawing('example_use_drawing.svg')

    print("start: example_koch_snowflake.svg\n")
    koch_snowflake('example_koch_snowflake.svg')

    print("start: example_markers.svg\n")
    marker_drawing('example_markers.svg')


    if longrun:
        print("start long time running examples!\n")

        print("start: example_mandelbrot.svg\n")
        mandelbrot('example_mandelbrot.svg')

        print("start: example_lsystem.svg\n")
        LSystem('example_lsys_hilbertspacefillingcurve.svg', formula=HilbertSpaceFillingCurve)
        LSystem('example_lsys_levydragon.svg', formula=LevyDragon)
        LSystem('example_lsys_levycurve.svg', formula=LevyCurve)
        LSystem('example_lsys_kochsnowflake.svg', formula=KochSnowflake)

if __name__ == '__main__':
    main()