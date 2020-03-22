# Copyright (c) 2019 Manfred Moitzi
# Copyright (c) 2019 Christof Hanke
# License: MIT License
import math

from svgwrite.extensions.shapes import ngon, translate, scale, rotate, centroid


def are_close_points(p1, p2, abs_tol=1e-9):
    return math.isclose(p1[0], p2[0], abs_tol=abs_tol) and math.isclose(p1[1], p2[1], abs_tol=abs_tol)


def test_square_by_radius():
    corners = list(ngon(4, radius=1))
    assert len(corners) == 4
    assert are_close_points(corners[0], (1, 0))
    assert are_close_points(corners[1], (0, 1))
    assert are_close_points(corners[2], (-1, 0))
    assert are_close_points(corners[3], (0, -1))


def test_heptagon_by_edge_length():
    corners = list(ngon(7, edge_length=10))
    assert len(corners) == 7
    assert are_close_points(corners[0], (11.523824354812433, 0.0))
    assert are_close_points(corners[1], (7.184986963636852, 9.009688679024192))
    assert are_close_points(corners[2], (-2.564292158181384, 11.234898018587335))
    assert are_close_points(corners[3], (-10.382606982861683, 5.0))
    assert are_close_points(corners[4], (-10.382606982861683, -5))
    assert are_close_points(corners[5], (-2.564292158181387, -11.234898018587335))
    assert are_close_points(corners[6], (7.18498696363685, -9.009688679024192))


def test_rotate():
    points = [(1, 0), (0, 1)]
    result = list(rotate(points, math.pi / 2))
    assert are_close_points(result[0], (0, 1))
    assert are_close_points(result[1], (-1, 0))


def test_scale():
    points = [(1, 0), (0, 1)]
    result = list(scale(points, 2, 3))
    assert are_close_points(result[0], (2, 0))
    assert are_close_points(result[1], (0, 3))


def test_translate():
    points = [(1, 0), (0, 1)]
    result = list(translate(points, 2, 3))
    assert are_close_points(result[0], (3, 3))
    assert are_close_points(result[1], (2, 4))


def test_centroid():
    assert are_close_points(centroid(ngon(7, edge_length=10)), (0, 0))
