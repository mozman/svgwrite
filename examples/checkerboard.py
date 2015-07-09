#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg example: inline stylesheets, css, viewbox, groups
# Created: 09.06.2012
# Copyright (C) 2012, Manfred Moitzi
# License: MIT License

import sys
import os

try:
    import svgwrite
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
if svgwrite.version < (1,0,1):
    print("This script requires svgwrite 1.0.1 or newer for internal stylesheets.")
    sys.exit()

BOARD_WIDTH = "10cm"
BOARD_HEIGHT = "10cm"
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)
CSS_STYLES = """
    .background { fill: lavenderblush; }
    .line { stroke: firebrick; stroke-width: .1mm; }
    .blacksquare { fill: indigo; }
    .whitesquare { fill: hotpink; }
"""

def draw_board(dwg):
    def group(classname):
        return dwg.add(dwg.g(class_=classname))
    
    # setup element groups
    lines = group("line")
    white_squares = group("whitesquare")
    black_squares = group("blacksquare")
    
    # draw lines
    for i in range(9):
        y = i * 10
        lines.add(dwg.line(start=(0, y), end=(80, y)))
        x = i * 10
        lines.add(dwg.line(start=(x, 0), end=(x, 80)))
        
    # draw squares
    for x in range(8):
        for y in range(8):
            xc = x * 10 + 1
            yc = y * 10 + 1
            square = dwg.rect(insert=(xc, yc), size=(8, 8))
            (white_squares if (x+y) % 2 else black_squares).add(square)

def main():
    dwg = svgwrite.Drawing('checkerboard.svg', size=BOARD_SIZE)
    dwg.viewbox(0, 0, 80, 80)
    # checkerboard has a size of 10cm x 10cm;
    # defining a viewbox with the size of 80x80 means, that a length of 1
    # is 10cm/80 == 0.125cm (which is for now the famous USER UNIT)
    # but I don't have to care about it, I just draw 8x8 squares, each 10x10 USER-UNITS

    # always use css for styling
    dwg.defs.add(dwg.style(CSS_STYLES))
    
    # set background
    dwg.add(dwg.rect(size=('100%','100%'), class_='background'))
    draw_board(dwg)
    dwg.save()

if __name__== '__main__':
    main()
