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
    dwg = svgwrite.Drawing(name, debug=True)
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

if __name__ == '__main__':
    LSystem('lsys_hilbertspacefillingcurve.svg', formula=HilbertSpaceFillingCurve)
    LSystem('lsys_levydragon.svg', formula=LevyDragon)
    LSystem('lsys_levycurve.svg', formula=LevyCurve)
    LSystem('lsys_kochsnowflake.svg', formula=KochSnowflake)
