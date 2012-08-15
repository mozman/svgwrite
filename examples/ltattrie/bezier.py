#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7
import sys
import svgwrite
from itertools import *

PROGNAME = sys.argv[0].rstrip('.py')

# http://code.activestate.com/recipes/66472-frange-a-range-function-with-float-increments/
# but instead of parameter for float increments there is a parameter for n points.


def nfrange(fstart, fstop, n):
    # n = number of points
    delta = (fstop - fstart) / n
    return [ fstart + delta * i for i in range(n) ]

def create_svg(name):
    class bezier(object):
        def __init__(self, val_x, val_y):
            # The main point
            self.x = val_x
            self.y = val_y
            # control point before main point
            self.cbx = None
            self.cby = None
            # control point after main point
            self.cax = None
            self.cay = None

        def displayf(self):
            # display formatted with brackets and commas
            if self.cbx:
                self.s_cb = '({:f}, {:f})'.format(self.cbx, self.cby)
            else:
                self.s_cb = '(None, None)'
            if self.cax:
                self.s_ca = '({:f}, {:f})'.format(self.cax, self.cay)
            else:
                self.s_ca = ' (None, None)'
            return '({:s}, ({:f}, {:f}), {:s})'.format(self.s_cb, self.x, self.y, self.s_ca)

        def display(self):
            # display without formatted with brackets and commas
            if self.cbx:
                self.s_cb = '{:f} {:f}'.format(self.cbx, self.cby)
            else:
                self.s_cb = 'None None'
            if self.cax:
                self.s_ca = '{:f} {:f}'.format(self.cax, self.cay)
            else:
                self.s_ca = ' None None'
            return '{:s} {:f} {:f} {:s}'.format(self.s_cb, self.x, self.y, self.s_ca)

    svg_size = 900
    font_size = 20
    title = name + ': Example of Bezier curves'
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='white'))
    # give the name of the example and a title.
    dwg.add(dwg.text(title, insert=(0, (font_size + 5)),
            font_family="serif", font_size=font_size, fill='black'))
    # http://www.w3.org/TR/SVG11/paths.html
    # M=move to L=line to z=close path.
    # Uppercase means absolute coordinates, lowercase means relative coordinates
    # H=draw horizonal line V=draw vertical line
    #
    # C (absolute) c (relative)	curveto	(x1 y1 x2 y2 x y)+
    #   Draws a cubic Bezier curve from the current point to (x,y) using (x1,y1) as the control point at the beginning of the curve and (x2,y2) as the control point at the end of the curve. C (uppercase) indicates that absolute coordinates will follow; c (lowercase) indicates that relative coordinates will follow. Multiple sets of coordinates may be specified to draw a polybezier. At the end of the command, the new current point becomes the final (x,y) coordinate pair used in the polybezier.
    # S (absolute) s (relative)	shorthand/smooth curveto (x2 y2 x y)+
    #   Draws a cubic Bezier curve from the current point to (x,y). The first control point is assumed to be the reflection of the second control point on the previous command relative to the current point. (If there is no previous command or if the previous command was not an C, c, S or s, assume the first control point is coincident with the current point.) (x2,y2) is the second control point (i.e., the control point at the end of the curve). S (uppercase) indicates that absolute coordinates will follow; s (lowercase) indicates that relative coordinates will follow. Multiple sets of coordinates may be specified to draw a polybezier. At the end of the command, the new current point becomes the final (x,y) coordinate pair used in the polybezier.
    # Q (absolute) q (relative)	quadratic Bezier curveto (x1 y1 x y)+
    #   Draws a quadratic Bezier curve from the current point to (x,y) using (x1,y1) as the control point. Q (uppercase) indicates that absolute coordinates will follow; q (lowercase) indicates that relative coordinates will follow. Multiple sets of coordinates may be specified to draw a polybezier. At the end of the command, the new current point becomes the final (x,y) coordinate pair used in the polybezier.
    # T (absolute) t (relative)	Shorthand/smooth quadratic Bezier curveto (x y)+
    #   Draws a quadratic Bezier curve from the current point to (x,y). The control point is assumed to be the reflection of the control point on the previous command relative to the current point. (If there is no previous command or if the previous command was not a Q, q, T or t, assume the control point is coincident with the current point.) T (uppercase) indicates that absolute coordinates will follow; t (lowercase) indicates that relative coordinates will follow. At the end of the command, the new current point becomes the final (x,y) coordinate pair used in the polybezier.
    #
    # Draw rectangle but with wiggly Bezier line.
    start = [50.0, 100.0]
    size = [200.0, 200.0]
    pts_per_side = 7
    ctl_pt_weight = 2.50  # what weight is given to control point? (distance to next point) x ctl_pt_weight
    vert_pt_weight = .80  # what weight is given to vertical distance? (distance to next point) x vert_pt_weight
    plus_minus = cycle([1, -1])  # create iterator which alternates between +1 and -1 forever.
    #
    s1 = 'M {0[0]} {0[1]}'.format(start)
    p3 = dwg.path(d=s1, stroke_width=1, stroke='red', fill='none')
    # top left to top right
    l1 = nfrange(start[0], (start[0] + size[0]), 7)
    for item in l1:
        circle_3 = dwg.circle(center=(item, start[1]), r=3)
        circle_3.fill('green', opacity=0.5).stroke('black', width=1)
        dwg.add(circle_3)
    pm = next(plus_minus)
    l1l = []
    for i, item in enumerate(l1):
        # Do not add the starting point because the starting point is given by the M command
        ## TODO: change the loop to have the starting point M done within the loop.
        if i != 0:
            # create control point for the previous point
            ctl_pt_dist = ctl_pt_weight * (item - l1[i - 1])
            vert_dist_chg = vert_pt_weight * (item - l1[i - 1]) * pm  # vertical distance off off straight line.
            l1l.append(l1[i - 1] + ctl_pt_dist)  # x
            l1l.append(start[1] + vert_dist_chg)  # y
            circle_1 = dwg.circle(center=(l1[i - 1] + ctl_pt_dist, start[1] + vert_dist_chg), r=1)
            circle_1.fill('blue', opacity=0.5).stroke('black', width=1)
            dwg.add(circle_1)
            pm = next(plus_minus)
            vert_dist_chg = vert_pt_weight * (item - l1[i - 1]) * pm  # vertical distance off off straight line.
            # create control point for the current point
            l1l.append(item - ctl_pt_dist)  # x
            l1l.append(start[1] + vert_dist_chg)  # y
            circle_1 = dwg.circle(center=(item - ctl_pt_dist, start[1] + vert_dist_chg), r=1)
            circle_1.fill('purple', opacity=0.5).stroke('black', width=1)
            dwg.add(circle_1)
            # create the current point
            l1l.append(item)
            l1l.append(start[1] + vert_dist_chg)
            circle_3 = dwg.circle(center=(item, start[1] + vert_dist_chg), r=3)
            circle_3.fill('blue', opacity=0.5).stroke('black', width=1)
            dwg.add(circle_3)
    p3.push('C', l1l)
    dwg.add(p3)
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
