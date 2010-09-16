#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg shapes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import parameter
from base import BaseElement
from validator import check_coordinate
from utils import points_to_string
from interface import ITransform

class Line(BaseElement, ITransform):
    """ The svg <line /> object. """
    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **kwargs):
        """ Constructor

        start -- start point as 2-tuple
        end -- end point as 2-tuple
        """
        super(Line, self).__init__(attribs, **kwargs)
        profile = parameter.profile
        self.attribs['x1'] = check_coordinate(start[0], profile)
        self.attribs['y1'] = check_coordinate(start[1], profile)
        self.attribs['x2'] = check_coordinate(end[0], profile)
        self.attribs['y2'] = check_coordinate(end[1], profile)

class Rect(BaseElement, ITransform):
    """ The svg <rect /> object. """
    def __init__(self, insert=(0, 0), size=(1, 1), rx=None, ry=None,
                 attribs=None, **kwargs):
        """ Constructor

        insert -- insert point as 2-tuple, left-upper point
        size -- 2-tuple (width, height)
        rx -- corner x-radius
        ry -- corner y-radius
        """
        super(Rect, self).__init__(attribs, **kwargs)

        profile = parameter.profile
        self.attribs['x'] = check_coordinate(insert[0], profile)
        self.attribs['y'] = check_coordinate(insert[1], profile)
        self.attribs['width'] = check_coordinate(size[0], profile)
        self.attribs['height'] = check_coordinate(size[1], profile)
        if rx: self.attribs['rx'] = check_coordinate(rx, profile)
        if ry: self.attribs['ry'] = check_coordinate(ry, profile)

class Circle(BaseElement, ITransform):
    """ The svg <circle /> object. """
    def __init__(self, center=(0, 0), r=1,
                 attribs=None, **kwargs):
        """ Constructor

        center -- circle center point as 2-tuple
        r -- circle-radius
        """
        super(Circle, self).__init__(attribs, **kwargs)
        profile = parameter.profile
        self.attribs['cx'] = check_coordinate(center[0], profile)
        self.attribs['cy'] = check_coordinate(center[1], profile)
        self.attribs['r'] = check_coordinate(r, profile)

class Ellipse(BaseElement, ITransform):
    """ The svg <ellipse /> object. """
    def __init__(self, center=(0, 0), r=(1, 1),
                 attribs=None, **kwargs):
        """ Constructor

        center -- circle center point as 2-tuple
        r -- <2-tuple> (x-radius, y-radius)
        """
        super(Ellipse, self).__init__(attribs, **kwargs)
        profile = parameter.profile
        self.attribs['cx'] = check_coordinate(center[0], profile)
        self.attribs['cy'] = check_coordinate(center[1], profile)
        self.attribs['rx'] = check_coordinate(r[0], profile)
        self.attribs['ry'] = check_coordinate(r[1], profile)

class Polyline(BaseElement, ITransform):
    """ The svg <polyline /> object

    Attributes:
    -----------
    points -- python-list of points, a point is a 2-tuple (x,y), where x and y
        can be an int, float or a string like '10mm' e.g. ('10cm', '10cm') or (10, 10)

    Howto:
    ------
    add one point: Polyline.points.append( point )
    add multiple points: Polyline.points.extend( [point1, point2, point3, ...] )
    """
    def __init__(self, points=[], attribs=None, **kwargs):
        """ Constructor

        points -- list of points, where points can be 2-tuples (x,y),
             where x and y can be an int, float or a string like '10mm'
        """
        super(Polyline, self).__init__(attribs, **kwargs)
        self.points = points

    def get_xml(self):
        self.attribs['points'] = points_to_string(self.points)
        return super(Polyline, self).get_xml()

class Polygon(Polyline):
    """ The svg <polygone /> object is always a closed polyline.

    All attributes and methods are inherited from Polyline.

    Attributes:
    -----------
    points -- python-list of points, a point is a 2-tuple (x,y), where x and y
        can be an int, float or a string like '10mm' e.g. ('10cm', '10cm') or (10, 10)

    Howto:
    ------
    add one point: Polyline.points.append( point )
    add multiple points: Polyline.points.extend( [point1, point2, point3, ...] )
    """
    pass
