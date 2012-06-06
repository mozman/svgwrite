#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7

import sys
import svgwrite

# http://www.w3.org/TR/SVG11/struct.html#UseElement
#
# For more information on tesselation / tiling see http://en.wikipedia.org/wiki/Wallpaper_group
# The organization of these tilings are from the interesting book
# Designing Testellations: The Secrets of Interlocking Patterns by Jinny Beyer.

PROGNAME = sys.argv[0].rstrip('.py')


def create_svg(name):
    svg_size_width = 900
    svg_size_height = 2800
    font_size = 20
    square_size = 30
    title1 = name + ': Part 1 tiling with multiple def, groups, use, translate and scale.'
    sample = ()
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)

    # clip path to prevent drawing outside of tile
    # Having a clip path seems to increase the visibility of the lines between the tiles.
    # A clipping path may be necessary if the shapes go outside the triangle.
    # defs_g_kite = dwg.defs.add(dwg.g(id='defs_g_kite', clip_path='url(#clipkite)'))

    clip_path = dwg.defs.add(dwg.clipPath(id='clipsq'))

    # clip_path.add(dwg.circle((100, 100), 50))

    clip_path.add(dwg.rect((0, 0), (square_size, square_size)))

    # define the group (tile) which will be repeated.

    defs_g = dwg.defs.add(dwg.g(id='defs_g', clip_path='url(#clipsq)'))
    defs_g.add(dwg.rect((0, 0), (square_size, square_size)))
    #defs_g.add(dwg.circle(center=(0, 5), r=6, stroke='blue', fill='green', stroke_width=1))
    defs_g.add(dwg.ellipse(center=(5, 5), r=(5, 10), fill='green'))
    defs_g.add(dwg.polygon([(square_size / 2.0, 0), 
        (square_size, square_size), 
        (0, square_size)], stroke='none', fill='navy'))
    #defs_g.add(dwg.line(start=(0, 0), end=(square_size, square_size), stroke_width=2, stroke='black'))

    # Background will be dark but not black so the background does not overwhelm the colors.

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='grey'))

    # Give the name of the example and a title.

    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + 20

    # show sample of tile

    sq_created = dwg.use(defs_g, insert=(10, y), fill='yellow')
    dwg.add(sq_created)
    y += square_size
    title2 = 'Translation, math name: p1'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            sq_created = dwg.use(defs_g, insert=(50 + j * square_size, y), fill='yellow')
            dwg.add(sq_created)
    y += square_size

    # p2 (180 rotation to side)

    title2 = '180 rotation to side, math name: p2'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, insert=(x, y), fill='yellow')

            # rotate every second square

            if j % 2:
                sq_created.rotate(180, center=(x + square_size / 2.0, y + square_size / 2.0))
            dwg.add(sq_created)
    y += square_size

    # p2 (180 rotation below)

    title2 = '180 rotation below, math name: p2'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, insert=(x, y), fill='yellow')

            # rotate every second row

            if i % 2 == 1:
                sq_created.rotate(180, center=(x + square_size / 2.0, y + square_size / 2.0))
            dwg.add(sq_created)
    y += square_size

    # p2 (180 rotation side, below, and diagonally)

    title2 = '180 rotation below, math name: p2'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, insert=(x, y), fill='yellow')

            # rotate every second square

            if i % 2 != j % 2:
                sq_created.rotate(180, center=(x + square_size / 2.0, y + square_size / 2.0))
            dwg.add(sq_created)
    y += square_size

    # p4 (90 rotation effectively rotating around the lower right corner.)

    title2 = '90 degree rotation around lower right, math name: p4'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, insert=(x, y), fill='yellow')

            # rotate every second square

            if i % 2 == 1:

                # odd row

                if j % 2:
                    sq_created.rotate(-90, center=(x + square_size / 2.0, y + square_size / 2.0))
                else:
                    sq_created.rotate(180, center=(x + square_size / 2.0, y + square_size / 2.0))
            elif j % 2:
                sq_created.rotate(90, center=(x + square_size / 2.0, y + square_size / 2.0))
            dwg.add(sq_created)
    y += square_size

    # p4 (90 rotation effectively rotating around the upper left corner.)

    title2 = '90 degree rotation around upper left, math name: p4'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, insert=(x, y), fill='yellow')

            # rotate every second square

            if i % 2:

                # even row

                if j % 2:
                    sq_created.rotate(180, center=(x + square_size / 2.0, y + square_size / 2.0))
                else:
                    sq_created.rotate(-90, center=(x + square_size / 2.0, y + square_size / 2.0))
            elif j % 2:
                sq_created.rotate(90, center=(x + square_size / 2.0, y + square_size / 2.0))
            dwg.add(sq_created)
    y += square_size

    # pg (moved horizontally then flipped vertically)
    # scale(1,-1)

    title2 = 'Glide: move horizontally then flip vertically, math name: pg'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')

            # flip vertically every second square

            if j % 2:

                # odd column 1, 3, 5

                sq_created.translate(x, y + square_size)
                sq_created.scale(1, -1)
            else:

                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # pg (moved vertically then flipped horizontally)

    title2 = 'Glide: move vertically then flip horizontally, math name: pg'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')

            # flip horizontally every second row

            if i % 2:

                # odd row 1, 3, 5

                sq_created.translate(x + square_size, y)
                sq_created.scale(-1, 1)
            else:

                # even row 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # pgg (moved horizontally then flipped vertically, moved vertically then flipped horizontally)

    title2 = 'Double Glide: Move vert, flip horiz. Move horiz flip vert. math name: pgg'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')
            if i % 2:

                # odd row 1, 3, 5

                if j % 2:

                    # odd column 1, 3, 5
                    # flip vertically and horizontally every second square

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
                else:

                    # even column 0, 2, 4
                    # flip vertically every second square

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip vertically every second square but start with the first square

                sq_created.translate(x, y + square_size)
                sq_created.scale(1, -1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
