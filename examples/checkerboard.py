#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg example: inline stylesheets, css, viewbox, groups
# Created: 09.06.2012
# Copyright (C) 2012, Manfred Moitzi
# License: GPLv3

import sys

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

if svgwrite.version < (1,0,1):
    print("This script requires svgwrite 1.0.1 or newer for internal stylesheets.")
    sys.exit()

BOARD_WIDTH = "10cm"
BOARD_HEIGHT = "10cm"
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)
CSS_STYLES = """
    .line { stroke: firebrick; stroke-width: .1mm; }
    .blacksquare { fill: indigo; }
    .whitesquare { fill: hotpink; }
"""

def draw_board(dwg):
    def draw_lines():
        lines = dwg.add(dwg.g(class_="line"))
        for i in range(9):
            y = i * 10
            lines.add(dwg.line(start=(0, y), end=(80, y)))
            x = i * 10
            lines.add(dwg.line(start=(x, 0), end=(x, 80)))

    def draw_squares():
        white_squares = dwg.add(dwg.g(class_="whitesquare"))
        black_squares = dwg.add(dwg.g(class_="blacksquare"))
        for x in range(8):
            for y in range (8):
                xc = x * 10 + 1
                yc = y * 10 + 1
                square = dwg.rect(insert=(xc, yc), size=(8, 8))
                (white_squares if (x+y) % 2 else black_squares).add(square)
    draw_lines()
    draw_squares()


def main():
    dwg = svgwrite.Drawing('checkerboard.svg', size=BOARD_SIZE)
    dwg.viewbox(0, 0, 80, 80)
    # checkerboard has a size of 10cm x 10cm;
    # defining a viewbox with the size of 80x80 means, that a length of 1
    # is 10cm/80 == 0.125cm (which is for now the famous USER UNIT)
    # but I don't have to care about it, I just draw 8x8 squares, each 10x10 USER-UNITS

    # always use css for styling
    dwg.defs.add(dwg.style(CSS_STYLES))
    draw_board(dwg)
    dwg.save()

if __name__== '__main__':
    main()
