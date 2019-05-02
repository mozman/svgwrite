"""
Extension to create regular polygons easily
"""
# Copyright (c) 2019 Christof Hanke (christof.hanke@induhviduals.de)
# License: MIT License
import math

def regular_polygon(svg, num_corners, edge_length, center=(0,0), **extra):
    """
    return a regular polygons
    """
    internal_angle = (1 - 2.0/num_corners) * math.pi
    points = []
    circum_radius = edge_length / (2 * math.sin(math.pi / num_corners))
    first_corner = (center[0] + math.sin(math.pi / num_corners) * circum_radius,
    center[1] - math.cos(math.pi / num_corners) * circum_radius)
    points.append(first_corner)
    angle = 0
    x = first_corner[0]
    y = first_corner[1]
    for co in range(num_corners - 1):
        angle = angle - (math.pi - internal_angle)
        x = x + math.cos(angle) * edge_length
        y = y - math.sin(angle) * edge_length
        points.append((x,y))
    return svg.polygon(points, **extra)
