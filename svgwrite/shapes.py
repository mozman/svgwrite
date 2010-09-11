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

class Line(BaseElement):
    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **kwargs):
        super(Line, self).__init__(attribs, **kwargs)
        self.attribs['x1'] = check_coordinate(start[0])
        self.attribs['y1'] = check_coordinate(start[1])
        self.attribs['x2'] = check_coordinate(end[0])
        self.attribs['y2'] = check_coordinate(end[1])

class Rect(BaseElement):
    def __init__(self, start=(0, 0), width=1, height=1, rx=None, ry=None,
                 attribs=None, **kwargs):
        super(Rect, self).__init__(attribs, **kwargs)
        self.attribs['x'] = check_coordinate(start[0])
        self.attribs['y'] = check_coordinate(start[1])
        self.attribs['width'] = check_coordinate(width)
        self.attribs['height'] = check_coordinate(height)
        if rx: self.attribs['rx'] = check_coordinate(rx)
        if ry: self.attribs['ry'] = check_coordinate(ry)

class Circle(BaseElement):
    def __init__(self, center=(0, 0), r=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, **kwargs)
        self.attribs['cx'] = check_coordinate(center[0])
        self.attribs['cy'] = check_coordinate(center[1])
        self.attribs['r'] = check_coordinate(r)

class Ellipse(BaseElement):
    def __init__(self, center=(0, 0), rx=1, ry=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, **kwargs)
        self.attribs['cx'] = check_coordinate(center[0])
        self.attribs['cy'] = check_coordinate(center[1])
        self.attribs['rx'] = check_coordinate(rx)
        self.attribs['ry'] = check_coordinate(ry)

class Polyline(BaseElement):
    def __init__(self, points=[], attribs=None, **kwargs):
        """ points -- list of points, where points can be 2-tuples (x,y),
        where x and y can be an int, float or a string like '10mm'
        """
        super(Polyline, self).__init__(attribs, **kwargs)
        self.points = points

    def add_point(self, point):
        """ point -- 2-tuple (x,y), where x and y can be an int, float or a
        string like '10mm'
        """
        self.points.append(point)

    def get_xml(self):
        self.attribs['points'] = points_to_string(self.points)
        return super(Polyline, self).get_xml()

class Polygon(Polyline):
    pass
