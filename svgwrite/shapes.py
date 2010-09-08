#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg shapes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement

class Line(BaseElement):
    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **kwargs):
        super(Line, self).__init__(attribs, kwargs)
        self.attribs['x1'] = start[0]
        self.attribs['y1'] = start[1]
        self.attribs['x2'] = end[0]
        self.attribs['y2'] = end[1]

class Rect(BaseElement):
    def __init__(self, start=(0, 0), width=1, height=1, rx=None, ry=None,
                 attribs=None, **kwargs):
        super(Rect, self).__init__(attribs, kwargs)
        self.attribs['x'] = start[0]
        self.attribs['y'] = start[1]
        self.attribs['width'] = width
        self.attribs['height'] = height
        if rx: self.attribs['rx'] = rx
        if ry: self.attribs['ry'] = ry

class Circle(BaseElement):
    def __init__(self, center=(0, 0), r=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, kwargs)
        self.attribs['cx'] = center[0]
        self.attribs['cy'] = center[1]
        self.attribs['r'] = r

class Ellipse(BaseElement):
    def __init__(self, center=(0, 0), rx=1, ry=1,
                 attribs=None, **kwargs):
        super(Circle, self).__init__(attribs, kwargs)
        self.attribs['cx'] = center[0]
        self.attribs['cy'] = center[1]
        self.attribs['rx'] = rx
        self.attribs['ry'] = ry

class Polyline(BaseElement):
    def __init__(self, points=[], attribs=None, **kwargs):
        super(Polyline, self).__init__(attribs, kwargs)
        self.attribs['points'] = points

    def add_point(self, point):
        self.attribs['points'].append(point)

class Polygon(Polyline):
    pass
