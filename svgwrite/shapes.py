#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg shapes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

"""
Valid for all classes: Line, Rect, Circle, Ellipse, Polyline, Polygon

Inherited Attributes:
---------------------
attribs -- <dict> svg attributes dictionary
elements -- <list> list of containing svg-elements

Inherited Methods:
------------------
add(svg-element) -- add an svg-element
tostring() -- get the xml-representation as <string> 'utf-8' encoded
get_xml() -- get the xml-representation as ElementTree object

Supported Interfaces:
---------------------
ITransform: translate, rotate, scale, skewX, skewY, matrix, rev, del_transform

Supported svg-attributes:
-------------------------
class -- <string> assigns one or more css-class-names to an element
style -- <string> allows per-element css-style rules to be specified directly on a given element
externalResourcesRequired -- "true|false" false: if document rendering can proceed
    even if external resources are unavailable else: true
transform -- use ITransform interface

Standard SVG Attributes:
------------------------
see description in  **base.py**

* Core Attributes
* Conditional Processing Attributes
* Graphical Event Attributes
* Presentation Attributes
"""

import parameter
from base import BaseElement
from validator import check_coordinate
from utils import points_to_string
from interface import ITransform

class Line(BaseElement, ITransform):
    """ The *line* element defines a line segment that starts at one point and ends
    at another.

    Supported svg-attributes:
    -------------------------
    x1 -- <coordinate> start-x
    y1 -- <coordinate> start-y
    x2 -- <coordinate> end-x
    y2 -- <coordinate> end-y
    """
    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **extra):
        """ Constructor

        start -- <2-tuple> start point (x1, y1)
        end -- <2-tuple> end point (x2, y2)
        """
        super(Line, self).__init__(attribs=attribs, **extra)
        profile = parameter.profile
        self.attribs['x1'] = check_coordinate(start[0], profile)
        self.attribs['y1'] = check_coordinate(start[1], profile)
        self.attribs['x2'] = check_coordinate(end[0], profile)
        self.attribs['y2'] = check_coordinate(end[1], profile)

class Rect(BaseElement, ITransform):
    """ The *rect* element defines a rectangle which is axis-aligned with the current
    user coordinate system. Rounded rectangles can be achieved by setting appropriate
    values for attributes *rx* and *ry*.

    Supported svg-attributes:
    -------------------------
    x -- <coordinate> The x-axis coordinate of the side of the rectangle which has
        the smaller x-axis coordinate value
    y -- <coordinate> The y-axis coordinate of the side of the rectangle which has
        the smaller y-axis coordinate value
    width -- <lenght>
    height -- <lenght>
    rx -- <length> For rounded rectangles, the y-axis radius of the ellipse used to
        round off the corners of the rectangle.
    ry -- <length> For rounded rectangles, the y-axis radius of the ellipse used to
        round off the corners of the rectangle.
    """
    def __init__(self, insert=(0, 0), size=(1, 1), rx=None, ry=None,
                 attribs=None, **extra):
        """ Constructor

        insert -- <2-tuple> insert point (x, y), left-upper point
        size -- <2-tuple> (width, height)
        rx -- corner x-radius
        ry -- corner y-radius
        """
        super(Rect, self).__init__(attribs=attribs, **extra)

        profile = parameter.profile
        self.attribs['x'] = check_coordinate(insert[0], profile)
        self.attribs['y'] = check_coordinate(insert[1], profile)
        self.attribs['width'] = check_coordinate(size[0], profile)
        self.attribs['height'] = check_coordinate(size[1], profile)
        if rx: self.attribs['rx'] = check_coordinate(rx, profile)
        if ry: self.attribs['ry'] = check_coordinate(ry, profile)

class Circle(BaseElement, ITransform):
    """ The *circle* element defines a circle based on a center point and a radius.

    Supported svg-attributes:
    -------------------------
    cx -- <coordinate> The x-axis coordinate of the center of the circle.
    cy -- <coordinate> The y-axis coordinate of the center of the circle.
    r -- <length> The radius of the circle.
    """
    def __init__(self, center=(0, 0), r=1, attribs=None, **extra):
        """ Constructor

        center -- <2-tuple> circle center point (cx, cy)
        r -- <length> circle-radius r
        """
        super(Circle, self).__init__(attribs=attribs, **extra)
        profile = parameter.profile
        self.attribs['cx'] = check_coordinate(center[0], profile)
        self.attribs['cy'] = check_coordinate(center[1], profile)
        self.attribs['r'] = check_coordinate(r, profile)

class Ellipse(BaseElement, ITransform):
    """ The *ellipse* element defines an ellipse which is axis-aligned with the
    current user coordinate system based on a center point and two radii.

    Supported svg-attributes:
    -------------------------
    cx -- <coordinate> The x-axis coordinate of the center of the ellipse.
    cy -- <coordinate> The y-axis coordinate of the center of the ellipse.
    rx -- <length> The x-axis radius of the ellipse.
    ry -- <length> The y-axis radius of the ellipse.
    """
    def __init__(self, center=(0, 0), r=(1, 1), attribs=None, **extra):
        """ Constructor

        center -- <2-tuple> ellipse center point (cx, cy)
        r -- <2-tuple> ellipse radii (rx, ry)
        """
        super(Ellipse, self).__init__(attribs=attribs, **extra)
        profile = parameter.profile
        self.attribs['cx'] = check_coordinate(center[0], profile)
        self.attribs['cy'] = check_coordinate(center[1], profile)
        self.attribs['rx'] = check_coordinate(r[0], profile)
        self.attribs['ry'] = check_coordinate(r[1], profile)

class Polyline(BaseElement, ITransform):
    """ The *polyline* element defines a set of connected straight line segments.
    Typically, *polyline* elements define open shapes.

    Attributes:
    -----------
    points -- <list> of points, a point is a <2-tuple> (x, y): x, y = <number>.

    Supported svg-attributes:
    -------------------------
    points -- <list-of-points> The points that make up the polyline. All coordinate
    values are in the **user coordinate system** (no units allowed).

    How to append points::
        Polyline.points.append( point )
        Polyline.points.extend( [point1, point2, point3, ...] )
    """
    def __init__(self, points=[], attribs=None, **extra):
        """ Constructor

        points -- python-list of points, a point is a <2-tuple> (x, y), where x and y
            can be an int or a float.
        """
        super(Polyline, self).__init__(attribs=attribs, **extra)
        self.points = points

    def get_xml(self):
        self.attribs['points'] = points_to_string(self.points)
        return super(Polyline, self).get_xml()

class Polygon(Polyline):
    """ The *polygon* element defines a closed shape consisting of a set of connected
    straight line segments.

    Same as *Polyline* but closed.
    """
    pass
