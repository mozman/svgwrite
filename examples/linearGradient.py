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
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import svgwrite

def linearGradient(name):
    dwg = svgwrite.Drawing(name, size=('20cm', '15cm'), profile='full', debug=True)

    # set user coordinate space
    dwg.viewbox(width=200, height=150)

    # create a new linearGradient element
    horizontal_gradient = dwg.linearGradient((0, 0), (1, 0))
    vertical_gradient = dwg.linearGradient((0, 0), (0, 1))
    diagonal_gradient = dwg.linearGradient((0, 0), (1, 1))
    tricolor_gradient = dwg.linearGradient((0, 0), (1, 1))

    # add gradient to the defs section of the drawing
    dwg.defs.add(horizontal_gradient)
    dwg.defs.add(vertical_gradient)
    dwg.defs.add(diagonal_gradient)
    dwg.defs.add(tricolor_gradient)

    # define the gradient from white to red
    horizontal_gradient.add_stop_color(0, 'white')
    horizontal_gradient.add_stop_color(1, 'red')

    # define the gradient from white to green
    vertical_gradient.add_stop_color(0, 'white')
    vertical_gradient.add_stop_color(1, 'green')

    # define the gradient from white to blue
    diagonal_gradient.add_stop_color(0, 'white')
    diagonal_gradient.add_stop_color(1, 'blue')

    # define the gradient from white to red to green to blue
    tricolor_gradient.add_stop_color(0, 'white')
    tricolor_gradient.add_stop_color(.33, 'red')
    tricolor_gradient.add_stop_color(.66, 'green')
    tricolor_gradient.add_stop_color(1, 'blue')


    # use gradient for filling the rect
    dwg.add(dwg.rect((10,10), (50,50), fill=horizontal_gradient.get_paint_server(default='currentColor')))
    dwg.add(dwg.rect((70,10), (50,50), fill=vertical_gradient.get_paint_server(default='currentColor')))
    dwg.add(dwg.rect((130,10), (50,50), fill=diagonal_gradient.get_paint_server(default='currentColor')))

    dwg.add(dwg.rect((10,70), (50,50), fill=tricolor_gradient.get_paint_server(default='currentColor')))

    # rotate gradient about 90 degree
    # first copy gradient
    tricolor2_gradient = tricolor_gradient.copy()
    # rotate the gradient
    tricolor2_gradient.rotate(90, (.5, .5))
    # add gradient to the defs section of the drawing
    dwg.defs.add(tricolor2_gradient)
    # use the gradient
    dwg.add(dwg.rect((70,70), (50,50), fill=tricolor2_gradient.get_paint_server(default='currentColor')))

    updown = dwg.linearGradient()
    dwg.defs.add(updown)
    updown.add_colors(['red', 'white', 'red', 'white', 'red'], sweep=(.2, .8))
    dwg.add(dwg.rect((130,70), (50,50), fill=updown.get_paint_server(default='currentColor')))

    dwg.save()

if __name__ == '__main__':
    linearGradient("linearGradient.svg")
