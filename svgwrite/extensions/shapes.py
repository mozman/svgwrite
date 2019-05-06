"""
Extension to create and manipulate shapes
"""
# Copyright (c) 2019 Christof Hanke (christof.hanke@induhviduals.de)
# License: MIT License
import math

def ngon(num_corners, edge_length):
    """
    generator returning the corners of a regular polygon
    """
    internal_angle = (1 - 2.0/num_corners) * math.pi
    points = []
    circum_radius = edge_length / (2 * math.sin(math.pi / num_corners))
    first_corner = (math.sin(math.pi / num_corners) * circum_radius,
        - math.cos(math.pi / num_corners) * circum_radius)
    points.append(first_corner)
    angle = 0
    x = first_corner[0] - edge_length
    y = first_corner[1]
    for co in range(num_corners):
        x = x + math.cos(angle) * edge_length
        y = y - math.sin(angle) * edge_length
        angle = angle - (math.pi - internal_angle)
        yield(x, y)

def translate(vertices, delta_x, delta_y):
    """
    generator yielding a translated vertices
    """
    for x, y in vertices:
        yield (x+delta_x, y+delta_y)

def scale(vertices, scale_x, scale_y):
    """
    generator yielding vertices which positions have been scaled
    """
    for x, y in vertices:
        yield (x*scale_x, y*scale_y)

def rotate(vertices, delta):
    """
    generator yielding vertices which have been rotated aorund the origin
    """
    for x, y in vertices:
        r = math.hypot(x, y)
        angle = math.atan2(y, x) + delta
        yield (r*math.cos(angle), r*math.sin(angle))

def centroid(vertices):
    """
    return the centroid of a series of vertices
    """
    k, c_x, c_y = 0, 0, 0
    for x, y in vertices:
        c_x += x
        c_y += y
        k += 1
    c_x = float(c_x / k)
    c_y = float(c_y / k)
    return c_x, c_y
