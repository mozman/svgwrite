"""
Extension to create and manipulate shapes
"""
# Copyright (c) 2019 Christof Hanke (christof.hanke@induhviduals.de)
# License: MIT License
import math


def ngon(num_corners, edge_length=None, radius=None, rotation=0.):
    """
    Returns the corners of a regular polygon as iterable of (x, y) tuples. The polygon size is determined by the
    `edge_length` or the `radius` argument. If both are given `edge_length` will be taken.

    Args:
        num_corners: count of polygon corners
        edge_length: length of polygon side
        radius: circum radius
        rotation: rotation angle in radians

    """
    if num_corners < 3:
        raise ValueError('Argument `num_corners` has to be greater than 2.')
    if edge_length is not None:
        radius = edge_length / 2. / math.sin(math.pi / num_corners)
    elif radius is not None:
        if radius <= 0.:
            raise ValueError('Argument `radius` has to be greater than 0.')
    else:
        raise ValueError('Argument `edge_length` or `radius` required.')

    delta = 2. * math.pi / num_corners
    angle = rotation
    for _ in range(num_corners):
        yield (radius * math.cos(angle), radius * math.sin(angle))
        angle += delta


def translate(vertices, delta_x, delta_y):
    """
    Translates `vertices` about `delta_x` and `delta_y`

    Args:
         vertices: iterable of (x, y) tuples
         delta_x: translation in x axis
         delta_y: translation in y axis

    Returns: iterable of (x, y) tuples

    """
    for x, y in vertices:
        yield (x + delta_x, y + delta_y)


def scale(vertices, scale_x, scale_y):
    """
    Scales `vertices` about `scale_x` and `scale_y`

    Args:
         vertices: iterable of (x, y) tuples
         scale_x: scaling factor in x axis direction
         scale_y: scaling factor in y axis direction

    Returns: iterable of (x, y) tuples

    """
    for x, y in vertices:
        yield (x * scale_x, y * scale_y)


def rotate(vertices, delta):
    """
    Rotates `vertices` about `delta` degrees around the origin (0, 0).

    Args:
         vertices: iterable of (x, y) tuples
         delta: rotation angle in radians

    Returns: iterable of (x, y) tuples

    """
    for x, y in vertices:
        r = math.hypot(x, y)
        angle = math.atan2(y, x) + delta
        yield (r * math.cos(angle), r * math.sin(angle))


def centroid(vertices):
    """
    Returns the centroid of a series of `vertices`.

    """
    k, c_x, c_y = 0, 0, 0
    for x, y in vertices:
        c_x += x
        c_y += y
        k += 1
    c_x = float(c_x / k)
    c_y = float(c_y / k)
    return c_x, c_y
