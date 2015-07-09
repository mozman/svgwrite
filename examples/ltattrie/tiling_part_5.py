#!/usr/bin/python
# -*- coding: utf-8 -*-
import math, sys
import svgwrite

#
# http://www.w3.org/TR/SVG11/struct.html#UseElement
#
# For more information on tesselation / tiling see http://en.wikipedia.org/wiki/Wallpaper_group
# The organization of these tilings are from the interesting book
#   Designing Testellations: The Secrets of Interlocking Patterns by Jinny Beyer.

PROGNAME = sys.argv[0].rstrip('.py')

def create_svg(name):
    svg_size_width = 900
    svg_size_height = 1600
    font_size = 20
    square_size = 30
    title1 = name + ': Part 5 tiling with multiple def, groups, use, translate and scale.'
    sqrt3 = math.sqrt(3)  # do this calc once instead of repeating the calc many times.
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)

    # ####################
    # p3m1 - Mirror and Three rotations
    #      - Equilateral triangle mirrored, rotated
    # All three sides are the same length, all three angles are 60 degrees.
    # The height of the triangle h = sqrt(3)/2.0 * length of a side
    # The centre of the triangle is  sqrt(3)/6.0 * length of a side

    defs_g_trieq_size_x = square_size
    defs_g_trieq_size_y = defs_g_trieq_size_x * sqrt3 / 2.0
    defs_g_trieq_centre = sqrt3 / 6.0 * defs_g_trieq_size_x

    # width of equilateral triangle at the centre

    defs_g_trieq_centre_size_x = defs_g_trieq_size_x - defs_g_trieq_size_x * defs_g_trieq_centre / defs_g_trieq_size_y

    # defs_g_trieq = dwg.defs.add(dwg.g(id='defs_g_trieq', clip_path='url(#cliptrieq)'))

    defs_g_trieq = dwg.defs.add(dwg.g(id='defs_g_trieq'))
    defs_g_trieq.add(dwg.polygon([(0, -defs_g_trieq_size_y + defs_g_trieq_centre), (defs_g_trieq_size_x / 2.0, defs_g_trieq_centre),
                     (-defs_g_trieq_size_x / 2.0, defs_g_trieq_centre)], stroke='none'))
    defs_g_trieq.add(dwg.polygon([(-defs_g_trieq_size_x / 2.0, defs_g_trieq_centre), (-defs_g_trieq_centre_size_x / 2.0, 0),
                     (defs_g_trieq_centre_size_x / 2.0, 0), (0, defs_g_trieq_centre)], stroke='none', fill='yellow'))

    # Create mirror of the equilateral triangle.

    defs_g_trieq_m = dwg.defs.add(dwg.g(id='defs_g_trieq_m'))
    defs_g_trieq_m.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_m.scale(-1, -1)

    # Create combined cell

    defs_g_trieq_cc_size_x = 1.5 * defs_g_trieq_size_x
    defs_g_trieq_cc_size_y = defs_g_trieq_size_y
    defs_g_trieq_cc = dwg.defs.add(dwg.g(id='defs_g_trieq_cc'))
    defs_g_trieq_cc.add(dwg.use(defs_g_trieq, insert=(-defs_g_trieq_size_x / 4.0, defs_g_trieq_size_y / 2.0 - defs_g_trieq_centre)))
    defs_g_trieq_cc.add(dwg.use(defs_g_trieq_m, insert=(defs_g_trieq_size_x / 4.0, -(defs_g_trieq_size_y / 2.0 - defs_g_trieq_centre))))

    # Create rotations of combined cell

    defs_g_trieq_cc_120 = dwg.defs.add(dwg.g(id='defs_g_trieq_cc_120'))
    defs_g_trieq_cc_120.add(dwg.use(defs_g_trieq_cc, insert=(0, 0), fill='mediumblue'))
    defs_g_trieq_cc_120.rotate(120, center=(0, 0))
    defs_g_trieq_cc_m120 = dwg.defs.add(dwg.g(id='defs_g_trieq_cc_m120'))
    defs_g_trieq_cc_m120.add(dwg.use(defs_g_trieq_cc, insert=(0, 0), fill='navy'))
    defs_g_trieq_cc_m120.rotate(-120, center=(0, 0))

    # Create pattern from rotations of combined cell

    defs_g_trieq_pattern_size_x = 2 * defs_g_trieq_size_x
    defs_g_trieq_pattern_size_y = 2 * defs_g_trieq_size_y
    defs_g_trieq_pattern = dwg.defs.add(dwg.g(id='defs_g_trieq_pattern'))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_cc, insert=(-defs_g_trieq_size_x / 4.0, -defs_g_trieq_cc_size_y / 2.0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_cc_120, insert=(defs_g_trieq_size_x / 2.0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_cc_m120, insert=(-defs_g_trieq_size_x / 4.0, defs_g_trieq_cc_size_y / 2.0)))

    # ####################
    # p31m - Three rotations and a mirror
    #      - A Kite shape, half hexagon, and half of a 60 degree diamond will all work for this
    #      symmetry.  This one will use a kite.
    # 30, 60, 90 angle triangle
    #   The length of the sides are 1:sqrt(3):2   2 is the hypotenuse
    # invsqrt2 = 1/sqrt2
    # invsqrt2_2 = invsqrt2 * invsqrt2 = 1/2 = .5 by definition
    # sin and cos(45 degrees) is 1/sqrt2 = 0.707106781187
    # cos(30 degrees) is sqrt3/2
    # sin(30 degrees) is 1/2
    # tan(30) = 1/sqrt(3)
    # The height of equilateral triangle h = sqrt(3)/2.0 * length of a side
    # The centre of equilateral triangle is  sqrt(3)/6.0 * length of a side

    defs_g_kite_size_x = square_size
    defs_g_kite_size_y = defs_g_kite_size_x * sqrt3 / 2.0 + defs_g_kite_size_x * sqrt3 / 6.0

    # Having a clip path seems to increase the visibility of the lines between the tiles.
    # A clipping path may be necessary if the shapes go outside the triangle.
    # defs_g_kite = dwg.defs.add(dwg.g(id='defs_g_kite', clip_path='url(#clipkite)'))

    defs_g_kite = dwg.defs.add(dwg.g(id='defs_g_kite'))
    defs_g_kite.add(dwg.polygon([(0, 0), 
        (defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0)), 
        (0, defs_g_kite_size_y), 
        (-defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0))], stroke='none'))
    #defs_g_kite.add(dwg.polygon([(0, 0), 
    #    (defs_g_kite_size_x / 4.0, (defs_g_kite_size_y + defs_g_kite_size_x / (sqrt3 * 2.0)) / 2.0),
    #    (-defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0))], stroke='none', fill='yellow'))
    defs_g_kite.add(dwg.polygon([(0, 0), 
        (defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0)),
        (0, defs_g_kite_size_y / 12.0),
        (-defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0))], stroke='none',
        fill='black'))
    defs_g_kite.add(dwg.polygon([(0, defs_g_kite_size_y), 
        (defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0)),
        (0, defs_g_kite_size_y * 8.0 / 12.0),
        (-defs_g_kite_size_x / 2.0, defs_g_kite_size_x / (sqrt3 * 2.0))], stroke='none',
        fill='green'))

    # Create rotations of the kite.

    defs_g_kite_120 = dwg.defs.add(dwg.g(id='defs_g_kite_120'))
    defs_g_kite_120.add(dwg.use(defs_g_kite, insert=(0, 0)))
    defs_g_kite_120.rotate(120, center=(0, 0))
    defs_g_kite_m120 = dwg.defs.add(dwg.g(id='defs_g_kite_m120'))
    defs_g_kite_m120.add(dwg.use(defs_g_kite, insert=(0, 0)))
    defs_g_kite_m120.rotate(-120, center=(0, 0))

    # Now use the cell, rotated cells to create the combined cell.
    # The height of equilateral triangle h = sqrt(3) / 2.0 * length of a side

    defs_g_kite_cc_size_x = 2 * defs_g_kite_size_x
    defs_g_kite_cc_size_y = defs_g_kite_size_x * sqrt3  # 2*(sqrt(3)/2.0)
    defs_g_kite_cc = dwg.defs.add(dwg.g(id='defs_g_kite_cc'))
    defs_g_kite_cc.add(dwg.use(defs_g_kite, insert=(0, 0)))
    defs_g_kite_cc.add(dwg.use(defs_g_kite_120, insert=(0, 0)))
    defs_g_kite_cc.add(dwg.use(defs_g_kite_m120, insert=(0, 0)))

    # Now use the combined cell to create a mirrored combined cell

    defs_g_kite_mcc = dwg.defs.add(dwg.g(id='defs_g_kite_mcc'))
    defs_g_kite_mcc.add(dwg.use(defs_g_kite_cc, insert=(0, 0)))
    defs_g_kite_mcc.scale(-1, -1)

    # Now use the combined cell, and mirrored combined cell to create a pattern

    defs_g_kite_pattern_size_x = 1.5 * defs_g_kite_cc_size_x
    defs_g_kite_pattern_size_y = defs_g_kite_cc_size_y
    defs_g_kite_pattern = dwg.defs.add(dwg.g(id='defs_g_kite_pattern'))
    defs_g_kite_pattern.add(dwg.use(defs_g_kite_cc, insert=(-defs_g_kite_cc_size_x / 4.0, -sqrt3 / 12.0 * defs_g_kite_cc_size_x)))
    defs_g_kite_pattern.add(dwg.use(defs_g_kite_mcc, insert=(defs_g_kite_cc_size_x / 4.0, sqrt3 / 12.0 * defs_g_kite_cc_size_x)))

    # ####################
    # p6m - Kaleidoscope Either of the two long sides of the primary triangle is mirrored.  The
    # resulting shape is rotated six times.
    # 30, 60, 90 angle triangle
    #   The length of the sides are 1:sqrt(3):2   2 is the hypotenuse
    # invsqrt2 = 1/sqrt2
    # invsqrt2_2 = invsqrt2 * invsqrt2 = 1/2 = .5 by definition
    # sin and cos(45 degrees) is 1/sqrt2 = 0.707106781187
    # cos(30 degrees) is sqrt3/2
    # sin(30 degrees) is 1/2
    # tan(30) = 1/sqrt(3)
    # # The height of equilateral triangle h = sqrt(3) / 2.0 * length of a side
    # # The centre of equilateral triangle is  sqrt(3) / 6.0 * length of a side

    defs_g_kale_tri_size_x = square_size
    defs_g_kale_tri_size_y = defs_g_kale_tri_size_x * 4.0 / sqrt3

    # Having a clip path seems to increase the visibility of the lines between the tiles.
    # A clipping path may be necessary if the shapes go outside the triangle.
    # defs_g_kale_tri = dwg.defs.add(dwg.g(id='defs_g_kale_tri', clip_path='url(#clipkale)'))

    defs_g_kale_tri = dwg.defs.add(dwg.g(id='defs_g_kale_tri'))
    defs_g_kale_tri.add(dwg.polygon([(0, -defs_g_kale_tri_size_y), (0, 0), (-defs_g_kale_tri_size_x, defs_g_kale_tri_size_x / sqrt3
                        - defs_g_kale_tri_size_y)], stroke='none'))
    defs_g_kale_tri.add(dwg.polygon([(-defs_g_kale_tri_size_x, defs_g_kale_tri_size_x / sqrt3 - defs_g_kale_tri_size_y), (0, 2.0
                        * defs_g_kale_tri_size_x / sqrt3 - defs_g_kale_tri_size_y), (0, 3.0 * defs_g_kale_tri_size_x / sqrt3
                        - defs_g_kale_tri_size_y)], stroke='none', fill='yellow'))

    # Create mirror of the kale.

    defs_g_kale_tri_m = dwg.defs.add(dwg.g(id='defs_g_kale_tri_m'))
    defs_g_kale_tri_m.add(dwg.use(defs_g_kale_tri, insert=(0, 0)))
    defs_g_kale_tri_m.scale(-1, 1)

    # Now use the tri, rotated tri to create the combined cell.

    defs_g_kale_cc_size_x = 2 * defs_g_kale_tri_size_x
    defs_g_kale_cc_size_y = defs_g_kale_tri_size_y
    defs_g_kale_cc = dwg.defs.add(dwg.g(id='defs_g_kale_cc'))
    defs_g_kale_cc.add(dwg.use(defs_g_kale_tri, insert=(0, 0)))
    defs_g_kale_cc.add(dwg.use(defs_g_kale_tri_m, insert=(0, 0)))

    # Now rotate the combined cell.

    defs_g_kale_cc_60 = dwg.defs.add(dwg.g(id='defs_g_kale_cc_60'))
    defs_g_kale_cc_60.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_cc_60.rotate(60, center=(0, 0))
    defs_g_kale_cc_120 = dwg.defs.add(dwg.g(id='defs_g_kale_cc_120'))
    defs_g_kale_cc_120.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_cc_120.rotate(120, center=(0, 0))
    defs_g_kale_cc_180 = dwg.defs.add(dwg.g(id='defs_g_kale_cc_180'))
    defs_g_kale_cc_180.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_cc_180.rotate(180, center=(0, 0))
    defs_g_kale_cc_m60 = dwg.defs.add(dwg.g(id='defs_g_kale_cc_m60'))
    defs_g_kale_cc_m60.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_cc_m60.rotate(-60, center=(0, 0))
    defs_g_kale_cc_m120 = dwg.defs.add(dwg.g(id='defs_g_kale_cc_m120'))
    defs_g_kale_cc_m120.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_cc_m120.rotate(-120, center=(0, 0))

    # Now use the cell and five rotated cells to create the pattern.

    defs_g_kale_pattern_size_x = 2 * defs_g_kale_cc_size_x
    defs_g_kale_pattern_size_y = 2 * defs_g_kale_cc_size_y
    defs_g_kale_pattern = dwg.defs.add(dwg.g(id='defs_g_kale_pattern'))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc, insert=(0, 0)))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc_60, insert=(0, 0)))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc_120, insert=(0, 0)))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc_180, insert=(0, 0)))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc_m60, insert=(0, 0)))
    defs_g_kale_pattern.add(dwg.use(defs_g_kale_cc_m120, insert=(0, 0)))

    # ########################
    # Background will be dark but not black so the background does not overwhelm the colors.

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='grey'))

    # Give the name of the example and a title.

    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    # p3m1 - Mirror and three rotations

    title2 = 'Mirror and three rotations, math name: p3m1'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + defs_g_trieq_size_x
    cell_created = dwg.use(defs_g_trieq, insert=(50 + defs_g_trieq_size_x, y), fill='lightblue')
    dwg.add(cell_created)
    dwg.add(dwg.circle(center=(50 + defs_g_trieq_size_x, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    cc_created = dwg.use(defs_g_trieq_cc, insert=(150 + defs_g_trieq_cc_size_x, y), fill='lightblue')
    dwg.add(cc_created)
    dwg.add(dwg.circle(center=(150 + defs_g_trieq_cc_size_x, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    pattern_created = dwg.use(defs_g_trieq_pattern, insert=(250 + defs_g_trieq_cc_size_x, y), fill='lightblue')
    dwg.add(pattern_created)
    dwg.add(dwg.circle(center=(250 + defs_g_trieq_cc_size_x, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_trieq_pattern_size_y
    for i in range(8):
        y += defs_g_trieq_pattern_size_y / 2.0
        for j in range(6):
            if i % 2:
                x = 50 + j * 1.5 * defs_g_trieq_pattern_size_x
            else:
                x = 50 + 1.5 * defs_g_trieq_size_x + j * 1.5 * defs_g_trieq_pattern_size_x
            pattern_created = dwg.use(defs_g_trieq_pattern, fill='lightblue')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_trieq_pattern_size_y

    #
    # p31m sample cell, combined cell and tile

    title2 = 'Kite rotated and mirrored, math name: p31m'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + defs_g_kite_size_y
    cell_created = dwg.use(defs_g_kite, insert=(50 + defs_g_kite_size_x / 2.0, y), fill='navy')
    dwg.add(cell_created)
    dwg.add(dwg.circle(center=(50 + defs_g_kite_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    cc_created = dwg.use(defs_g_kite_cc, insert=(150 + defs_g_kite_size_x / 2.0, y), fill='navy')
    dwg.add(cc_created)
    dwg.add(dwg.circle(center=(150 + defs_g_kite_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    mcc_created = dwg.use(defs_g_kite_mcc, insert=(250 + defs_g_kite_cc_size_x / 2, y), fill='navy')
    dwg.add(mcc_created)
    dwg.add(dwg.circle(center=(250 + defs_g_kite_cc_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    pattern_created = dwg.use(defs_g_kite_pattern, insert=(350 + defs_g_kite_cc_size_x, y), fill='navy')
    dwg.add(pattern_created)
    dwg.add(dwg.circle(center=(350 + defs_g_kite_cc_size_x, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_kite_pattern_size_y
    for i in range(6):
        y += defs_g_kite_pattern_size_y
        for j in range(8):
            if i % 2:
                x = 100 + (j + 0.5) * defs_g_kite_cc_size_x
            else:
                x = 100 + j * defs_g_kite_cc_size_x
            pattern_created = dwg.use(defs_g_kite_pattern, fill='navy')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_kite_pattern_size_y

    # ##
    # p6m kaleidoscope

    title2 = 'Kaleidoscope 30, 60, 90 triangle mirrored and rotated, math name: p6m'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size
    y += defs_g_kale_tri_size_y
    cell_created = dwg.use(defs_g_kale_tri, insert=(50 + defs_g_kale_tri_size_x, y), fill='navy')
    dwg.add(cell_created)
    dwg.add(dwg.circle(center=(50 + defs_g_kale_tri_size_x, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    cc_created = dwg.use(defs_g_kale_cc, insert=(150 + defs_g_kale_cc_size_x / 2.0, y), fill='navy')
    dwg.add(cc_created)
    dwg.add(dwg.circle(center=(150 + defs_g_kale_cc_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    pattern_created = dwg.use(defs_g_kale_pattern, insert=(250 + defs_g_kale_pattern_size_x / 2.0, y), fill='navy')
    dwg.add(pattern_created)
    dwg.add(dwg.circle(center=(250 + defs_g_kale_pattern_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_kale_pattern_size_y / 2.0
    for i in range(4):
        y += defs_g_kale_pattern_size_y - defs_g_kale_pattern_size_x / (sqrt3 * 2)
        for j in range(6):
            if i % 2:
                x = 100 + j * defs_g_kale_pattern_size_x
            else:
                x = 100 + defs_g_kale_cc_size_x + j * defs_g_kale_pattern_size_x
            pattern_created = dwg.use(defs_g_kale_pattern, fill='navy')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_kale_pattern_size_y

    # All items have been added so save the svg to a the file.

    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99

