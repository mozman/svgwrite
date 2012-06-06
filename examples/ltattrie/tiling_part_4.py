#!/usr/bin/python
# -*- coding: utf-8 -*-
import math, sys
import svgwrite

# http://www.w3.org/TR/SVG11/struct.html#UseElement
#
# For more information on tesselation / tiling see http://en.wikipedia.org/wiki/Wallpaper_group
# The organization of these tilings are from the interesting book
#   Designing Testellations: The Secrets of Interlocking Patterns by Jinny Beyer.

PROGNAME = sys.argv[0].rstrip('.py')

def create_svg(name):
    svg_size_width = 900
    svg_size_height = 2200
    font_size = 20
    triangle_size = 30
    square_size = 30
    title1 = name + ': Part 4 tiling with multiple def, groups, use, translate and scale.'
    sqrt3 = math.sqrt(3)  # do this calc once instead of repeating the calc many times.

    # sqrt2 = math.sqrt(2) # do this calc once instead of repeating the calc many times. 1.41421356237

    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)

    # 45 degrees, 90 degrees, 45 degrees Right angle triangle

    triright = dwg.defs.add(dwg.polygon([(0, 0), (triangle_size, 0), (triangle_size, triangle_size)], id='triangle', stroke='none'))

    # clip path to prevent drawing outside of tile

    clip_path_triright = dwg.defs.add(dwg.clipPath(id='cliptriright'))
    clip_path_triright.add(dwg.polygon([(0, 0), (triangle_size, 0), (triangle_size, triangle_size)]))

    # define the group (tile) which will be repeated.
    # Having a clip path seems to increase the visibility of the lines which can occur between tiles and patterns.

    defs_g_triright = dwg.defs.add(dwg.g(id='defs_g_triright', clip_path='url(#cliptriright)'))
    defs_g_triright.add(dwg.polygon([(0, 0), (triangle_size, 0), (triangle_size, triangle_size)], stroke='none'))
    defs_g_triright.add(dwg.polygon([(3 * triangle_size / 4.0, 0), 
        (triangle_size, 0), 
        (triangle_size, triangle_size)], stroke='none', fill='navy'))
    defs_g_triright.add(dwg.circle(center=(triangle_size / 2.0, triangle_size / 2.0), r=5, stroke='blue', fill='green', stroke_width=1))

    # define the mirror of  defs_g_triright

    defs_g_tr_m = dwg.defs.add(dwg.g(id='defs_g_tr_m'))
    defs_g_tr_m.add(dwg.use(defs_g_triright, insert=(0, 0)))
    defs_g_tr_m.rotate(90, center=(triangle_size / 2.0, triangle_size / 2.0))
    defs_g_tr_m.translate(0, triangle_size)
    defs_g_tr_m.scale(1, -1)

    # defs_g_tr_m.rotate(-90, center=(triangle_size, triangle_size))
    # defs_g_tr_m.rotate(-90, center=(0, 0))
    #                sq_created.translate(x, (y + defs_g_p4g_v1_size))
    # create the cell by using one triangle and one mirrored triangle

    defs_g_p4m_cell_size = triangle_size
    defs_g_p4m_cell = dwg.defs.add(dwg.g(id='defs_g_p4m_cell'))

    # defs_g_p4m_cell.add(dwg.use(defs_g_triright, insert=(0, 0), fill='aqua'))

    defs_g_p4m_cell.add(dwg.use(defs_g_triright, insert=(0, 0)))
    defs_g_p4m_cell.add(dwg.use(defs_g_tr_m, insert=(0, 0)))

    # Create rotations of the cell.

    defs_g_p4m_cell_lr_90 = dwg.defs.add(dwg.g(id='defs_g_p4m_cell_lr_90'))
    defs_g_p4m_cell_lr_90.add(dwg.use(defs_g_p4m_cell, insert=(0, 0)))
    defs_g_p4m_cell_lr_90.rotate(90, center=(square_size, square_size))
    defs_g_p4m_cell_lr_m90 = dwg.defs.add(dwg.g(id='defs_g_p4m_cell_lr_m90'))
    defs_g_p4m_cell_lr_m90.add(dwg.use(defs_g_p4m_cell, insert=(0, 0)))
    defs_g_p4m_cell_lr_m90.rotate(-90, center=(square_size, square_size))
    defs_g_p4m_cell_lr_180 = dwg.defs.add(dwg.g(id='defs_g_p4m_cell_lr_180'))
    defs_g_p4m_cell_lr_180.add(dwg.use(defs_g_p4m_cell, insert=(0, 0)))
    defs_g_p4m_cell_lr_180.rotate(180, center=(square_size, square_size))

    # Now use the cell and three rotated cells to create the pattern.

    defs_g_p4m_pattern_size = 2 * defs_g_p4m_cell_size
    defs_g_p4m_pattern = dwg.defs.add(dwg.g(id='defs_g_p4m_pattern'))
    defs_g_p4m_pattern.add(dwg.use(defs_g_p4m_cell, insert=(0, 0)))
    defs_g_p4m_pattern.add(dwg.use(defs_g_p4m_cell_lr_90, insert=(0, 0)))
    defs_g_p4m_pattern.add(dwg.use(defs_g_p4m_cell_lr_m90, insert=(0, 0)))
    defs_g_p4m_pattern.add(dwg.use(defs_g_p4m_cell_lr_180, insert=(0, 0)))

    # ####################
    # p3 - rombus - For the purpose of these tessellations a rombus is 4 * 30-60-90 triangles.
    # 30, 60, 90 angle triangle
    #   The length of the sides are 1:sqrt(3):2   2 is the hypotenuse
    # invsqrt2 = 1/sqrt2
    # invsqrt2_2 = invsqrt2 * invsqrt2 = 1/2 = .5 by definition
    # sin and cos(45 degrees) is 1/sqrt2 = 0.707106781187
    # cos(30 degrees) is sqrt3/2
    # sin(30 degrees) is 1/2

    defs_g_rombus_size_x = square_size
    defs_g_rombus_scale = defs_g_rombus_size_x / (sqrt3 * 2.0)
    defs_g_rombus_size_y = 2 * defs_g_rombus_scale

    # Having a clip path seems to increase the visibility of the lines between the tiles.
    # A clipping path may be necessary if the shapes go outside the triangle.
    # defs_g_rombus = dwg.defs.add(dwg.g(id='defs_g_rombus', clip_path='url(#cliprombus)'))

    defs_g_rombus = dwg.defs.add(dwg.g(id='defs_g_rombus'))
    defs_g_rombus.add(dwg.polygon([(0, defs_g_rombus_size_y / 2.0), (defs_g_rombus_size_x / 2.0, 0), (0, -defs_g_rombus_size_y / 2),
                      (-defs_g_rombus_size_x / 2.0, 0)], stroke='none'))
    defs_g_rombus.add(dwg.polygon([(0, -defs_g_rombus_size_y / 2.0), (defs_g_rombus_size_x / 4.0, defs_g_rombus_size_y / 4.0), (0,
                      defs_g_rombus_size_y / 2.0)], stroke='none', fill='darkolivegreen'))

    #     (0, defs_g_rombus_size_y/2.0) ], stroke='none', fill='aqua'))
    #     (0, defs_g_rombus_size_y/2.0) ], stroke='none'))
    #     (defs_g_rombus_size_x/4.0, defs_g_rombus_size_y/4.0),
    #     (defs_g_rombus_size_x*invsqrt2_2/2.0, defs_g_rombus_size_y*invsqrt2_2/2.0),

    defs_g_rombus.add(dwg.polygon([(0, -defs_g_rombus_size_y / 2.0), (-defs_g_rombus_size_x / 2.0, 0), (0, 0)], stroke='none', fill='palegreen'))

    # Create rotations of the rombus.

    defs_g_rombus_120 = dwg.defs.add(dwg.g(id='defs_g_rombus_120'))
    defs_g_rombus_120.add(dwg.use(defs_g_rombus, insert=(0, 0)))
    defs_g_rombus_120.rotate(120, center=(0, 0))
    defs_g_rombus_m120 = dwg.defs.add(dwg.g(id='defs_g_rombus_m120'))
    defs_g_rombus_m120.add(dwg.use(defs_g_rombus, insert=(0, 0)))
    defs_g_rombus_m120.rotate(-120, center=(0, 0))

    # Create the pattern by using the cell and two rotated cells

    defs_g_rombus_pattern_size_x = defs_g_rombus_size_x
    defs_g_rombus_pattern_size_y = 2.0 * defs_g_rombus_size_y
    defs_g_rombus_pattern = dwg.defs.add(dwg.g(id='defs_g_rombus_pattern'))
    defs_g_rombus_pattern.add(dwg.use(defs_g_rombus, insert=(defs_g_rombus_size_x / 2.0, 3 * defs_g_rombus_size_y / 2.0)))
    defs_g_rombus_pattern.add(dwg.use(defs_g_rombus_120, insert=(defs_g_rombus_size_x / 4.0, 3 * defs_g_rombus_size_y / 4.0)))
    defs_g_rombus_pattern.add(dwg.use(defs_g_rombus_m120, insert=(.75 * defs_g_rombus_size_x, 3 * defs_g_rombus_size_y / 4.0)))

    # ####################
    # p6 - Equilateral triangle
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

    # Create rotations of the equilateral triangle.

    defs_g_trieq_60 = dwg.defs.add(dwg.g(id='defs_g_trieq_60'))
    defs_g_trieq_60.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_60.rotate(60, center=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre))
    defs_g_trieq_120 = dwg.defs.add(dwg.g(id='defs_g_trieq_120'))
    defs_g_trieq_120.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_120.rotate(120, center=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre))
    defs_g_trieq_180 = dwg.defs.add(dwg.g(id='defs_g_trieq_180'))
    defs_g_trieq_180.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_180.rotate(180, center=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre))
    defs_g_trieq_m60 = dwg.defs.add(dwg.g(id='defs_g_trieq_m60'))
    defs_g_trieq_m60.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_m60.rotate(-60, center=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre))
    defs_g_trieq_m120 = dwg.defs.add(dwg.g(id='defs_g_trieq_m120'))
    defs_g_trieq_m120.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_m120.rotate(-120, center=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre))

    # Now use the cell and five rotated cells to create the pattern.

    defs_g_trieq_pattern_size_x = 2 * defs_g_trieq_size_x
    defs_g_trieq_pattern_size_y = 2 * defs_g_trieq_size_y
    defs_g_trieq_pattern = dwg.defs.add(dwg.g(id='defs_g_trieq_pattern'))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_60, insert=(0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_120, insert=(0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_180, insert=(0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_m60, insert=(0, 0)))
    defs_g_trieq_pattern.add(dwg.use(defs_g_trieq_m120, insert=(0, 0)))

    # Create centered rotations of the equilateral triangle.

    defs_g_trieq_c60 = dwg.defs.add(dwg.g(id='defs_g_trieq_c60'))
    defs_g_trieq_c60.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_c60.rotate(60, center=(0, 0))
    defs_g_trieq_c120 = dwg.defs.add(dwg.g(id='defs_g_trieq_c120'))
    defs_g_trieq_c120.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_c120.rotate(120, center=(0, 0))
    defs_g_trieq_c180 = dwg.defs.add(dwg.g(id='defs_g_trieq_c180'))
    defs_g_trieq_c180.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_c180.rotate(180, center=(0, 0))
    defs_g_trieq_cm60 = dwg.defs.add(dwg.g(id='defs_g_trieq_cm60'))
    defs_g_trieq_cm60.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_cm60.rotate(-60, center=(0, 0))
    defs_g_trieq_cm120 = dwg.defs.add(dwg.g(id='defs_g_trieq_cm120'))
    defs_g_trieq_cm120.add(dwg.use(defs_g_trieq, insert=(0, 0)))
    defs_g_trieq_cm120.rotate(-120, center=(0, 0))

    # Now use the cell and five rotated cells to create the pattern variation 2.
    # Variation 2 is the equilateral triangle rotated around a the upper corner.

    defs_g_trieq_pattern_v2_size_x = 2 * defs_g_trieq_size_x
    defs_g_trieq_pattern_v2_size_y = 2 * defs_g_trieq_size_y
    defs_g_trieq_pattern_v2 = dwg.defs.add(dwg.g(id='defs_g_trieq_pattern_v2'))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq, insert=(0, defs_g_trieq_size_y - defs_g_trieq_centre)))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq_c60, insert=(-defs_g_trieq_size_x / 2.0, defs_g_trieq_centre)))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq_c120, insert=(-defs_g_trieq_size_x / 2.0, -defs_g_trieq_centre)))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq_c180, insert=(0, defs_g_trieq_centre - defs_g_trieq_size_y)))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq_cm60, insert=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre)))
    defs_g_trieq_pattern_v2.add(dwg.use(defs_g_trieq_cm120, insert=(defs_g_trieq_size_x / 2.0, -defs_g_trieq_centre)))

    # Now use the cell and five rotated cells to create the pattern variation 3.
    # Variation 3 is the equilateral triangle rotated around a the lower left corner.

    defs_g_trieq_pattern_v3_size_x = 2 * defs_g_trieq_size_x
    defs_g_trieq_pattern_v3_size_y = 2 * defs_g_trieq_size_y
    defs_g_trieq_pattern_v3 = dwg.defs.add(dwg.g(id='defs_g_trieq_pattern_v3'))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq, insert=(defs_g_trieq_size_x / 2.0, -defs_g_trieq_centre)))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq_c60, insert=(defs_g_trieq_size_x / 2.0, defs_g_trieq_centre)))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq_c120, insert=(0, defs_g_trieq_size_y - defs_g_trieq_centre)))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq_c180, insert=(-defs_g_trieq_size_x / 2.0, defs_g_trieq_centre)))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq_cm60, insert=(0, defs_g_trieq_centre - defs_g_trieq_size_y)))
    defs_g_trieq_pattern_v3.add(dwg.use(defs_g_trieq_cm120, insert=(-defs_g_trieq_size_x / 2.0, -defs_g_trieq_centre)))

    # ########################
    # Background will be dark but not black so the background does not overwhelm the colors.

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='grey'))

    # Give the name of the example and a title.

    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    #
    # p4m 45 45 90 triangle

    title2 = '45 45 90 triangle mirrored and rotated, math name: p4m'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    # Sample of tile.

    y = y + triangle_size
    tri_created = dwg.use(defs_g_triright, insert=(50, y), fill='yellow')
    dwg.add(tri_created)
    tri_created = dwg.use(defs_g_p4m_cell, insert=(150, y), fill='yellow')
    dwg.add(tri_created)
    tri_created = dwg.use(defs_g_p4m_pattern, insert=(250, y), fill='yellow')
    dwg.add(tri_created)
    y = y + defs_g_p4m_pattern_size

    for i in range(4):
        y += defs_g_p4m_pattern_size
        for j in range(8):
            x = 50 + j * defs_g_p4m_pattern_size
            sq_created = dwg.use(defs_g_p4m_pattern, fill='yellow')
            sq_created.translate(x, y)
            dwg.add(sq_created)
    y += 2 * defs_g_p4m_pattern_size

    # p4m rombus

    title2 = 'Rombus rotated, math name: p3'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    # Sample of tile.
    # rombus_created = dwg.use(defs_g_rombus, insert=(100, y ), fill='yellow')

    rombus_created = dwg.use(defs_g_rombus, insert=(75, y), fill='black')
    dwg.add(rombus_created)
    tile_created = dwg.use(defs_g_rombus_120, insert=(150, y), fill='black')
    dwg.add(tile_created)
    pattern_created = dwg.use(defs_g_rombus_pattern, insert=(250, y), fill='black')
    dwg.add(pattern_created)
    y = y + defs_g_rombus_size_y

    y_offset = defs_g_rombus_size_y / 2.0
    for i in range(12):
        y += defs_g_rombus_pattern_size_y - y_offset
        for j in range(16):
            if i % 2:
                x = 50 + defs_g_rombus_pattern_size_x / 2.0 + j * defs_g_rombus_pattern_size_x
            else:
                x = 50 + j * defs_g_rombus_pattern_size_x
            pattern_created = dwg.use(defs_g_rombus_pattern, fill='black')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += 2 * defs_g_rombus_pattern_size_y

    # p6 Equilateral triangle

    title2 = 'Equilateral triangle rotated lower right point, math name: p6'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size

    # Sample of tile.

    y = y + triangle_size
    tri_created = dwg.use(defs_g_trieq, insert=(50 + defs_g_trieq_size_x / 2.0, y), fill='navy')
    dwg.add(tri_created)
    dwg.add(dwg.circle(center=(50 + defs_g_trieq_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    tile_created = dwg.use(defs_g_trieq_pattern, insert=(150 + defs_g_trieq_pattern_size_x / 2, y), fill='navy')
    dwg.add(tile_created)
    dwg.add(dwg.circle(center=(150 + defs_g_trieq_pattern_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_trieq_pattern_size_y
    for i in range(9):
        y += defs_g_trieq_pattern_size_y / 2.0
        for j in range(6):
            if i % 2:
                x = 50 + j * 1.5 * defs_g_trieq_pattern_size_x
            else:
                x = 50 + 1.5 * defs_g_trieq_size_x + j * 1.5 * defs_g_trieq_pattern_size_x
            pattern_created = dwg.use(defs_g_trieq_pattern, fill='navy')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_trieq_pattern_size_y

    title2 = 'Equilateral triangle rotated upper point, math name: p6'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + defs_g_trieq_pattern_size_y

    # sample centered rotated eqilateral triangle variation 2

    tri_created = dwg.use(defs_g_trieq, insert=(50 + defs_g_trieq_size_x / 2.0, y), fill='navy')
    dwg.add(tri_created)
    dwg.add(dwg.circle(center=(50 + defs_g_trieq_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    tile_created = dwg.use(defs_g_trieq_c60, insert=(150 + defs_g_trieq_size_x / 2, y), fill='navy')
    dwg.add(tile_created)
    dwg.add(dwg.circle(center=(150 + defs_g_trieq_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    tile_created = dwg.use(defs_g_trieq_pattern_v2, insert=(250 + defs_g_trieq_pattern_size_x / 2, y), fill='navy')
    dwg.add(tile_created)
    dwg.add(dwg.circle(center=(250 + defs_g_trieq_pattern_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_trieq_pattern_size_y
    for i in range(9):
        y += defs_g_trieq_pattern_v2_size_y / 2.0
        for j in range(6):
            if i % 2:
                x = 50 + j * 1.5 * defs_g_trieq_pattern_v2_size_x
            else:
                x = 50 + 1.5 * defs_g_trieq_size_x + j * 1.5 * defs_g_trieq_pattern_v2_size_x
            pattern_created = dwg.use(defs_g_trieq_pattern_v2, fill='navy')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_trieq_pattern_size_y

    title2 = 'Equilateral triangle rotated lower left, math name: p6'
    dwg.add(dwg.text(title2, insert=(50, y), font_family='serif', font_size=font_size, fill='white'))
    y = y + font_size + defs_g_trieq_pattern_size_y

    # sample centered rotated eqilateral triangle variation 3

    tri_created = dwg.use(defs_g_trieq, insert=(50 + defs_g_trieq_size_x / 2.0, y), fill='navy')
    dwg.add(tri_created)
    dwg.add(dwg.circle(center=(50 + defs_g_trieq_size_x / 2.0, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    tile_created = dwg.use(defs_g_trieq_c60, insert=(150 + defs_g_trieq_size_x / 2, y), fill='navy')
    dwg.add(tile_created)
    dwg.add(dwg.circle(center=(150 + defs_g_trieq_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    tile_created = dwg.use(defs_g_trieq_pattern_v3, insert=(250 + defs_g_trieq_pattern_size_x / 2, y), fill='navy')
    dwg.add(tile_created)
    dwg.add(dwg.circle(center=(250 + defs_g_trieq_pattern_size_x / 2, y), r=3, stroke='none', fill='purple', opacity='0.5'))
    y += defs_g_trieq_pattern_size_y
    for i in range(9):
        y += defs_g_trieq_pattern_v3_size_y / 2.0
        for j in range(6):
            if i % 2:
                x = 50 + j * 1.5 * defs_g_trieq_pattern_v3_size_x
            else:
                x = 50 + 1.5 * defs_g_trieq_size_x + j * 1.5 * defs_g_trieq_pattern_v3_size_x
            pattern_created = dwg.use(defs_g_trieq_pattern_v3, fill='navy')
            pattern_created.translate(x, y)
            dwg.add(pattern_created)
    y += defs_g_trieq_pattern_size_y

    # All items have been added so save the svg to a the file.# Sample of tile.

    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99

