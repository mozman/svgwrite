#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import svgwrite

PROGNAME = sys.argv[0].rstrip('.py')

#
# http://www.w3.org/TR/SVG11/struct.html#UseElement
#
# For more information on tesselation / tiling see http://en.wikipedia.org/wiki/Wallpaper_group
# The organization of these tilings are from the interesting book
#   Designing Testellations: The Secrets of Interlocking Patterns by Jinny Beyer.

def create_svg(name):
    svg_size_width = 900
    svg_size_height = 2200
    font_size = 20
    square_size = 30
    title1 = name + ': Part 2 tiling with multiple def, groups, use, translate and scale.'
    sample = ()
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)

    # Having a clip path seems to increase the visibility of the lines between the tiles.
    # A clipping path may be necessary if the shapes go outside the triangle.
    # clip path to prevent drawing outside of tile

    clip_path = dwg.defs.add(dwg.clipPath(id='clipsq'))
    clip_path.add(dwg.rect((0, 0), (square_size, square_size)))

    # define the group (tile) which will be repeated.

    defs_g = dwg.defs.add(dwg.g(id='defs_g', clip_path='url(#clipsq)'))
    defs_g.add(dwg.rect((0, 0), (square_size, square_size)))
    defs_g.add(dwg.circle(center=(0, 10), r=5, stroke='blue', fill='green', stroke_width=1))
    defs_g.add(dwg.polygon([(square_size, 0), 
        (square_size, square_size), 
        (0, square_size)], stroke='none', fill='navy'))

    # Background will be dark but not black so the background does not overwhelm the colors.

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='grey'))

    # Give the name of the example and a title.

    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + 20

    # Sample of tile.

    y = y + 20
    sq_created = dwg.use(defs_g, insert=(10, y), fill='yellow')
    dwg.add(sq_created)
    y += square_size

    # pm (mirror horizontally)

    title2 = 'Mirror horizontally, math name: pm'
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

                sq_created.translate(x + square_size, y)
                sq_created.scale(-1, 1)
            else:

                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y = y + square_size

    # pm (mirror vertically)

    title2 = 'Mirror vertically, math name: pm'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')

            # flip vertically every second row

            if i % 2:

                # odd row 1, 3, 5

                sq_created.translate(x, y + square_size)
                sq_created.scale(1, -1)
            else:

                # even row 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # cm (move horizontally then mirror. That pair is then moved vertically and staggered.)

    title2 = 'Move horiz & mirror vert. Move vert & mirror vert, math name: cm'
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

                    # odd row 1, 3, 5
                    # odd column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # odd row 1, 3, 5
                    # even column 0, 2, 4
                    # flip vertically every second square

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip vertically every second square

                sq_created.translate(x + square_size, y)
                sq_created.scale(-1, 1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # cm (move vertically then mirror. That pair is then moved horizontally and staggered.)

    title2 = 'Move horiz & mirror horiz, Move vert & mirror horiz, math name: cm'
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

                    # odd row 1, 3, 5
                    # odd column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # odd row 1, 3, 5
                    # even column 0, 2, 4
                    # flip horizontally every second square

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip horizontally every second square

                sq_created.translate(x, y + square_size)
                sq_created.scale(1, -1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # pmg (moved horizontally flip vertically. That pair is then moved vertically, mirrored and
    # staggered.)

    title2 = 'Move horiz mirror horiz. Pair is glided horiz and mirrored horiz, math name: pmg'
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

                    # odd row 1, 3, 5
                    # odd column 1, 3, 5
                    # flip horizontally every second square

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
                else:

                    # odd row 1, 3, 5
                    # even column 0, 2, 4
                    # flip vertically and horizontally every second square

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip vertically every second square

                sq_created.translate(x + square_size, y)
                sq_created.scale(-1, 1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # pmg (moved vertically flip horizontally. That pair is then moved horizontally, mirrored and
    # staggered.)

    title2 = 'Move vert mirror vert. Pair is glided vert and mirrored horiz, math name: pmg'
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

                    # odd row 1, 3, 5
                    # odd column 1, 3, 5
                    # flip vertically every second square

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # odd row 1, 3, 5
                    # even column 0, 2, 4
                    # flip horizontally every second square

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip vertically and horizontally every second square

                sq_created.translate(x + square_size, y + square_size)
                sq_created.scale(-1, -1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)
    y += square_size

    # pmm (as if mirrors were placed on all sides of square and diagonally.)

    title2 = 'Mirror all sides, math name: pm'
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

                    # odd row 1, 3, 5
                    # odd column 1, 3, 5
                    # flip vertically and horizontally every second square

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
                else:

                    # odd row 1, 3, 5
                    # even column 0, 2, 4
                    # flip horizontally every second square

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
            elif j % 2:

                # even row 0, 2, 4
                # odd column 1, 3, 5
                # flip vertically every second square

                sq_created.translate(x + square_size, y)
                sq_created.scale(-1, 1)
            else:

                # even row 0, 2, 4
                # even column 0, 2, 4

                sq_created.translate(x, y)
            dwg.add(sq_created)

    # All items have been added so save the svg to a the file.

    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99

