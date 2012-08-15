#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7

import math, sys
import svgwrite
from svgwrite import rgb
#
# http://www.w3.org/TR/SVG11/types.html#ColorKeywords
# Note both grey and gray are valide but only color not colour is valid.
#

PROGNAME = sys.argv[0].rstrip('.py')

def create_svg(name):
    WIDTH = 900
    HEIGHT = 900
    FONT_SIZE = 20
    COMPLETE_SIZE = 800   # size of the whole set of triangles.
    TRIANGLES_PER_SIDE = 50     # How many triangles there will be per side. integer.
    TRIHEIGHT = math.sqrt(3)/2.0

    title1 = name + ': Example of creating your own colors.'
    start = ((WIDTH - COMPLETE_SIZE)/2, (HEIGHT - COMPLETE_SIZE)/2)  # center triangle
    #tri_color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
    #tri_color = ((128, 0, 0), (0, 128, 0), (0, 0, 128))
    tri_color = ((20, 128, 30), (10, 0, 50), (0, 0, 128))
    dwg = svgwrite.Drawing(name, (WIDTH, HEIGHT), debug=True)


    def draw_triangle(insert, size, fill, rotate=None):
        x, y = insert
        points = [insert, (x + size, y), ((x + size / 2.0), (y + size * TRIHEIGHT))]
        triangle = dwg.add(dwg.polygon(points, fill=fill, stroke='none'))
        if rotate:
            triangle.rotate(rotate, center=insert)

    def nfrange(fstart, fstop, n):
        # n = number of points
        delta = (fstop - fstart) / n
        return [ fstart + delta * i for i in range(n) ]

    # Background will be dark but not black so the background does not overwhelm the colors.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='grey'))
    # Give the name of the example and a title.
    y = FONT_SIZE + 5
    dwg.add(dwg.text(title1, insert=(0, y),
            font_family="serif", font_size=FONT_SIZE, fill='white'))
    tri_size = COMPLETE_SIZE / TRIANGLES_PER_SIDE
    tri_height = tri_size * TRIHEIGHT
    ratio_side = nfrange(0.0, 1.0, TRIANGLES_PER_SIDE)

    for i in range(TRIANGLES_PER_SIDE, 0, -1):
        # The number of triangle in the row is the sum of the point up and the point down
        # triangles.
        num_tri_in_row = 2 * i - 1
        num_tri_drawn_in_row = 0

        # Calculate color
        start_color = [int(tri_color[0][k] * ratio_side[i-1] +
                           tri_color[2][k] * (1 - ratio_side[i-1])) for k in range(3)]
        end_color = [int(tri_color[1][k] * ratio_side[i-1] +
                         tri_color[2][k] * (1 -ratio_side[i-1])) for k in range(3)]

        # calculate ratios of the two ending colors.
        ratio_row = nfrange(0.0, 1.0, num_tri_in_row) if num_tri_in_row > 1 else [0.5]

        for j in range(i):
            x = start[0] + (j + ((TRIANGLES_PER_SIDE - i) / 2.0)) * tri_size
            y = start[1] + (TRIANGLES_PER_SIDE - i) * tri_height
            # Calculate color
            new_color = [int(start_color[k] * (1 - ratio_row[num_tri_drawn_in_row ]) +
                             end_color[k] * ratio_row[num_tri_drawn_in_row]) for k in range(3)]
            draw_triangle((x, y), tri_size, rgb(*new_color))
            num_tri_drawn_in_row += 1

            if j != (i - 1):
                # The on screen point up triangles have one fewer per row.
                x += tri_size

                # Calculate color
                new_color = [int(start_color[k] * (1 - ratio_row[num_tri_drawn_in_row ]) +
                                 end_color[k] * ratio_row[num_tri_drawn_in_row]) for k in range(3)]
                draw_triangle((x, y), tri_size, rgb(*new_color), rotate=60)
                num_tri_drawn_in_row += 1

    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99

