#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg shapes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from parameter import check_coordinate
from utils import points_to_string

_line_attribs = ['x1', 'y1', 'x2', 'y2']
class Line(BaseElement):
    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **kwargs):
        super(Line, self).__init__(attribs, kwargs)
        self.attribs['x1'] = check_coordinate(start[0])
        self.attribs['y1'] = check_coordinate(start[1])
        self.attribs['x2'] = check_coordinate(end[0])
        self.attribs['y2'] = check_coordinate(end[1])

    def _valid_attribs(self):
        return _line_attribs

_rect_attribs = ['x', 'y', 'width', 'height', 'rx', 'ry']
class Rect(BaseElement):
    def __init__(self, start=(0, 0), width=1, height=1, rx=None, ry=None,
                 attribs=None, **kwargs):
        super(Rect, self).__init__(attribs, kwargs)
        self.attribs['x'] = check_coordinate(start[0])
        self.attribs['y'] = check_coordinate(start[1])
        self.attribs['width'] = check_coordinate(width)
        self.attribs['height'] = check_coordinate(height)
        if rx: self.attribs['rx'] = check_coordinate(rx)
        if ry: self.attribs['ry'] = check_coordinate(ry)

    def _valid_attribs(self):
        return _rect_attribs

_circle_attribs = ['cx', 'cy', 'r']
class Circle(BaseElement):
    def __init__(self, center=(0, 0), r=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, kwargs)
        self.attribs['cx'] = check_coordinate(center[0])
        self.attribs['cy'] = check_coordinate(center[1])
        self.attribs['r'] = check_coordinate(r)

    def _valid_attribs(self):
        return _circle_attribs

_ellipse_attribs = ['cx', 'cy', 'rx', 'ry']
class Ellipse(BaseElement):
    def __init__(self, center=(0, 0), rx=1, ry=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, kwargs)
        self.attribs['cx'] = check_coordinate(center[0])
        self.attribs['cy'] = check_coordinate(center[1])
        self.attribs['rx'] = check_coordinate(rx)
        self.attribs['ry'] = check_coordinate(ry)

    def _valid_attribs(self):
        return _ellipse_attribs

_polyline_attribs = ['points']
class Polyline(BaseElement):
    def __init__(self, points=[], attribs=None, **kwargs):
        super(Polyline, self).__init__(attribs, kwargs)
        self.points = points

    def append(self, point):
        self.points.append(point)

    def get_xml(self):
        self.attribs['points'] = points_to_string(self.points)
        return super(Polyline, self).get_xml()

    def _valid_attribs(self):
        return _polyline_attribs

class Polygon(Polyline):
    pass
