#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import svgwrite


# http://www.w3.org/TR/SVG11/struct.html#UseElement
#
# For more information on tesselation / tiling see http://en.wikipedia.org/wiki/Wallpaper_group
# The organization of these tilings are from the interesting book
#   Designing Testellations: The Secrets of Interlocking Patterns by Jinny Beyer.

PROGNAME = sys.argv[0].rstrip('.py')


def create_svg(name):
    svg_size_width = 900
    svg_size_height = 2000
    font_size = 20
    square_size = 30
    title1 = name + ': Part 3 tiling with multiple def, groups, use, translate and scale.'
    sample = ()
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)

    # clip path to prevent drawing outside of tile

    clip_path = dwg.defs.add(dwg.clipPath(id='clipsq'))

    # clip_path.add(dwg.circle((100, 100), 50))

    clip_path.add(dwg.rect((0, 0), (square_size, square_size)))

    # define the group (tile) which will be repeated.

    defs_g = dwg.defs.add(dwg.g(id='defs_g', clip_path='url(#clipsq)'))

    # defs_g.add(dwg.rect((0,0), (square_size, square_size)))

    defs_g.add(dwg.rect((0, 0), (square_size, square_size)))
    defs_g.add(dwg.circle(center=(0, 10), r=5, stroke='blue', fill='green', stroke_width=1))
    defs_g.add(dwg.polygon([(square_size, 0), 
        (square_size, square_size), 
        (0, square_size)], stroke='none', fill='navy'))

    # Background will be dark but not black so the background does not overwhelm the colors.

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='grey'))

    # Give the name of the example and a title.

    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    #
    # Sample of tile.

    y = y + 20
    sq_created = dwg.use(defs_g, insert=(10, y), fill='yellow')
    dwg.add(sq_created)
    y += square_size

    # cmm variation 1 (as if mirrors were placed on all sides of square and diagonally.)
    #     similar to pmm but the group of four tiles will be mirrored, staggered, or centered.

    title2 = 'Mirror all sides, then all are moved, variation 1, math name: cmm'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 4 == 0:

                    # column 0, 4, 8
                    # flip horizontally

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
                elif j % 4 == 1:

                    # column 1, 5, 9
                    # flip vertically and horizontally

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
                elif j % 4 == 2:

                    # column 2, 6, 10

                    sq_created.translate(x, y)
                else:

                    # column 3, 7, 11
                    # flip vertically

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
            else:

                # row 0, 2, 4

                if j % 4 == 0:

                    # column 0, 4, 8

                    sq_created.translate(x, y)
                elif j % 4 == 1:

                    # column 1, 5, 9
                    # flip vertically

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
                elif j % 4 == 2:

                    # column 2, 6, 10
                    # flip horizontally

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
                else:

                    # column 3, 7, 11
                    # flip vertically and horizontally

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
            dwg.add(sq_created)
    y += square_size

    # cmm variation 2 (as if mirrors were placed on all sides of square and diagonally.)
    #     similar to pmm but the group of four tiles will be mirrored, staggered, or centered.

    title2 = 'Mirror all sides, then all are moved, variation 2, math name: cmm'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    for i in range(8):
        y += square_size
        for j in range(16):
            x = 50 + j * square_size
            sq_created = dwg.use(defs_g, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 4 == 0:

                    # column 0, 4, 8
                    # flip horizontally

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
                elif j % 4 == 1:

                    # column 1, 5, 9

                    sq_created.translate(x, y)
                elif j % 4 == 2:

                    # column 2, 6, 10
                    # flip vertically and horizontally

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
                else:

                    # column 3, 7, 11
                    # flip horizontally

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
            else:

                # row 0, 2, 4

                if j % 4 == 0:

                    # column 0, 4, 8
                    # flip vertically and horizontally

                    sq_created.translate(x + square_size, y + square_size)
                    sq_created.scale(-1, -1)
                elif j % 4 == 1:

                    # column 1, 5, 9
                    # flip horizontally

                    sq_created.translate(x, y + square_size)
                    sq_created.scale(1, -1)
                elif j % 4 == 2:

                    # column 2, 6, 10
                    # flip vertically

                    sq_created.translate(x + square_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # column 3, 7, 11

                    sq_created.translate(x, y)
            dwg.add(sq_created)

    y += square_size

    # Instead of writing the p4g four times this code would have been better if it had been
    # put into a function and called indicating which corner is to be used for rotation.
    # p4g variation 1 (mirrored pinwheel which depending on which corner is the rotation center.)
    # lower right is the rotation corner

    defs_g_p4g_v1_size = square_size * 2
    defs_g_lr_90 = dwg.defs.add(dwg.g(id='defs_g_lr_90'))
    defs_g_lr_90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_lr_90.rotate(90, center=(square_size, square_size))
    defs_g_lr_m90 = dwg.defs.add(dwg.g(id='defs_g_lr_m90'))
    defs_g_lr_m90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_lr_m90.rotate(-90, center=(square_size, square_size))
    defs_g_lr_180 = dwg.defs.add(dwg.g(id='defs_g_lr_180'))
    defs_g_lr_180.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_lr_180.rotate(180, center=(square_size, square_size))
    defs_g_p4g_v1 = dwg.defs.add(dwg.g(id='defs_g_p4g_v1'))
    defs_g_p4g_v1.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_p4g_v1.add(dwg.use(defs_g_lr_90, insert=(0, 0)))
    defs_g_p4g_v1.add(dwg.use(defs_g_lr_m90, insert=(0, 0)))
    defs_g_p4g_v1.add(dwg.use(defs_g_lr_180, insert=(0, 0)))
    title2 = 'Mirrored pinwheel, rotate lower right, math name: p4g'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))

    # y = y + font_size

    for i in range(4):
        y += defs_g_p4g_v1_size
        for j in range(8):
            x = 50 + j * defs_g_p4g_v1_size
            sq_created = dwg.use(defs_g_p4g_v1, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 2:

                    # column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # column 0, 2, 4
                    # flip horizontally

                    sq_created.translate(x, y + defs_g_p4g_v1_size)
                    sq_created.scale(1, -1)
            else:

                # row 0, 2, 4

                if j % 2:

                    # column 1, 3, 5
                    # flip vertically

                    sq_created.translate(x + defs_g_p4g_v1_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # column 0, 2, 4

                    sq_created.translate(x, y)
            dwg.add(sq_created)

    y += defs_g_p4g_v1_size

    # p4g variation 2 (mirrored pinwheel which depending on which corner is the rotation center.)
    # upper right is the rotation corner

    title2 = 'Mirrored pinwheel, rotate upper right, math name: p4g'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))

    # y = y + font_size

    defs_g_p4g_v2_size = square_size * 2
    defs_g_ur_90 = dwg.defs.add(dwg.g(id='defs_g_ur_90'))
    defs_g_ur_90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ur_90.rotate(90, center=(square_size, 0))
    defs_g_ur_m90 = dwg.defs.add(dwg.g(id='defs_g_ur_m90'))
    defs_g_ur_m90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ur_m90.rotate(-90, center=(square_size, 0))
    defs_g_ur_180 = dwg.defs.add(dwg.g(id='defs_g_ur_180'))
    defs_g_ur_180.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ur_180.rotate(180, center=(square_size, 0))
    defs_g_p4g_v2 = dwg.defs.add(dwg.g(id='defs_g_p4g_v2'))
    defs_g_p4g_v2.add(dwg.use(defs_g, insert=(0, square_size)))
    defs_g_p4g_v2.add(dwg.use(defs_g_ur_90, insert=(0, square_size)))
    defs_g_p4g_v2.add(dwg.use(defs_g_ur_m90, insert=(0, square_size)))
    defs_g_p4g_v2.add(dwg.use(defs_g_ur_180, insert=(0, square_size)))
    for i in range(4):
        y += defs_g_p4g_v2_size
        for j in range(8):
            x = 50 + j * defs_g_p4g_v2_size
            sq_created = dwg.use(defs_g_p4g_v2, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 2:

                    # column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # column 0, 2, 4
                    # flip horizontally

                    sq_created.translate(x, y + defs_g_p4g_v2_size)
                    sq_created.scale(1, -1)
            else:

                # row 0, 2, 4

                if j % 2:

                    # column 1, 3, 5
                    # flip vertically

                    sq_created.translate(x + defs_g_p4g_v2_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # column 0, 2, 4

                    sq_created.translate(x, y)
            dwg.add(sq_created)

    y += defs_g_p4g_v2_size

    # p4g variation 3 (mirrored pinwheel which depending on which corner is the rotation center.)
    # upper left is the rotation corner

    defs_g_p4g_v3_size = square_size * 2
    defs_g_ul_90 = dwg.defs.add(dwg.g(id='defs_g_ul_90'))
    defs_g_ul_90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ul_90.rotate(90, center=(0, 0))
    defs_g_ul_m90 = dwg.defs.add(dwg.g(id='defs_g_ul_m90'))
    defs_g_ul_m90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ul_m90.rotate(-90, center=(0, 0))
    defs_g_ul_180 = dwg.defs.add(dwg.g(id='defs_g_ul_180'))
    defs_g_ul_180.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ul_180.rotate(180, center=(0, 0))
    defs_g_p4g_v3 = dwg.defs.add(dwg.g(id='defs_g_p4g_v3'))
    defs_g_p4g_v3.add(dwg.use(defs_g, insert=(square_size, square_size)))
    defs_g_p4g_v3.add(dwg.use(defs_g_ul_90, insert=(square_size, square_size)))
    defs_g_p4g_v3.add(dwg.use(defs_g_ul_m90, insert=(square_size, square_size)))
    defs_g_p4g_v3.add(dwg.use(defs_g_ul_180, insert=(square_size, square_size)))
    title2 = 'Mirrored pinwheel, rotate upper left, math name: p4g'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))

    # y = y + font_size

    for i in range(4):
        y += defs_g_p4g_v3_size
        for j in range(8):
            x = 50 + j * defs_g_p4g_v3_size
            sq_created = dwg.use(defs_g_p4g_v3, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 2:

                    # column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # column 0, 2, 4
                    # flip horizontally

                    sq_created.translate(x, y + defs_g_p4g_v3_size)
                    sq_created.scale(1, -1)
            else:

                # row 0, 2, 4

                if j % 2:

                    # column 1, 3, 5
                    # flip vertically

                    sq_created.translate(x + defs_g_p4g_v3_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # column 0, 2, 4

                    sq_created.translate(x, y)
            dwg.add(sq_created)

    y += defs_g_p4g_v3_size

    # p4g variation 4 (mirrored pinwheel which depending on which corner is the rotation center.)
    # lower left is the rotation corner

    defs_g_p4g_v4_size = square_size * 2
    defs_g_ll_90 = dwg.defs.add(dwg.g(id='defs_g_ll_90'))
    defs_g_ll_90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ll_90.rotate(90, center=(0, square_size))
    defs_g_ll_m90 = dwg.defs.add(dwg.g(id='defs_g_ll_m90'))
    defs_g_ll_m90.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ll_m90.rotate(-90, center=(0, square_size))
    defs_g_ll_180 = dwg.defs.add(dwg.g(id='defs_g_ll_180'))
    defs_g_ll_180.add(dwg.use(defs_g, insert=(0, 0)))
    defs_g_ll_180.rotate(180, center=(0, square_size))
    defs_g_p4g_v4 = dwg.defs.add(dwg.g(id='defs_g_p4g_v4'))
    defs_g_p4g_v4.add(dwg.use(defs_g, insert=(square_size, 0)))
    defs_g_p4g_v4.add(dwg.use(defs_g_ll_90, insert=(square_size, 0)))
    defs_g_p4g_v4.add(dwg.use(defs_g_ll_m90, insert=(square_size, 0)))
    defs_g_p4g_v4.add(dwg.use(defs_g_ll_180, insert=(square_size, 0)))
    title2 = 'Mirrored pinwheel, rotate lower left, math name: p4g'
    dwg.add(dwg.text(title2, insert=(50, y + square_size), font_family='serif', font_size=font_size, fill='white'))

    # y = y + font_size

    for i in range(4):
        y += defs_g_p4g_v4_size
        for j in range(8):
            x = 50 + j * defs_g_p4g_v4_size
            sq_created = dwg.use(defs_g_p4g_v4, fill='yellow')
            if i % 2:

                # row 1, 3, 5

                if j % 2:

                    # column 1, 3, 5

                    sq_created.translate(x, y)
                else:

                    # column 0, 2, 4
                    # flip horizontally

                    sq_created.translate(x, y + defs_g_p4g_v4_size)
                    sq_created.scale(1, -1)
            else:

                # row 0, 2, 4

                if j % 2:

                    # column 1, 3, 5
                    # flip vertically

                    sq_created.translate(x + defs_g_p4g_v4_size, y)
                    sq_created.scale(-1, 1)
                else:

                    # column 0, 2, 4

                    sq_created.translate(x, y)
            dwg.add(sq_created)

    # All items have been added so save the svg to a the file.

    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99

