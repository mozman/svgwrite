#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg shapes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from interface import ITransform

class Line(BaseElement, ITransform):
    """ The <line> element defines a line segment that starts at one point and ends
    at another.

    .. automethod:: svgwrite.shapes.Line.__init__

    **SVG Attributes**

    * **x1** -- `coordinate` start-x
    * **y1** -- `coordinate` start-y
    * **x2** -- `coordinate` end-x
    * **y2** -- `coordinate` end-y
    """
    elementname = 'line'

    def __init__(self, start=(0, 0), end=(0, 0),
                 attribs=None, **extra):
        """
        :param 2-tuple start: start point (x1, y1)
        :param 2-tuple end: end point (x2, y2)
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Line, self).__init__(attribs=attribs, **extra)
        x1, y1 = start
        x2, y2 = end
        self['x1'] = x1
        self['y1'] = y1
        self['x2'] = x2
        self['y2'] = y2

class Rect(BaseElement, ITransform):
    """ The <rect> element defines a rectangle which is axis-aligned with the current
    user coordinate system. Rounded rectangles can be achieved by setting appropriate
    values for attributes <rx> and <ry>.

    .. automethod:: svgwrite.shapes.Rect.__init__

    **SVG Attributes**

    * **x** -- `coordinate` The x-axis coordinate of the side of the
               rectangle which has the smaller x-axis coordinate value
    * **y** -- `coordinate` The y-axis coordinate of the side of the
               rectangle which has the smaller y-axis coordinate value
    * **width** -- `lenght`
    * **height** -- `lenght`
    * **rx** -- `length` For rounded rectangles, the y-axis radius of the
                ellipse used to round off the corners of the rectangle.
    * **ry** -- `length` For rounded rectangles, the y-axis radius of the
                ellipse used to round off the corners of the rectangle.
    """
    elementname = 'rect'

    def __init__(self, insert=(0, 0), size=(1, 1), rx=None, ry=None,
                 attribs=None, **extra):
        """
        :param 2-tuple insert: insert point (x, y), left-upper point
        :param 2-tuple size: width, height
        :param length rx: corner x-radius
        :param length ry: corner y-radius
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Rect, self).__init__(attribs=attribs, **extra)
        x, y = insert
        width, height = size
        self['x'] = x
        self['y'] = y
        self['width'] = width
        self['height'] = height
        if rx: self['rx'] = rx
        if ry: self['ry'] = ry

class Circle(BaseElement, ITransform):
    """ The <circle> element defines a circle based on a center point and a radius.

    .. automethod:: svgwrite.shapes.Circle.__init__

    **SVG Attributes**

    * **cx** -- `coordinate` The x-axis coordinate of the center of the circle.
    * **cy** -- `coordinate` The y-axis coordinate of the center of the circle.
    * **r** -- `length` The radius of the circle.
    """
    elementname = 'circle'

    def __init__(self, center=(0, 0), r=1, attribs=None, **extra):
        """
        :param 2-tuple center: circle center point (cx, cy)
        :param length r: circle-radius r
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Circle, self).__init__(attribs=attribs, **extra)
        cx, cy = center
        self['cx'] = cx
        self['cy'] = cy
        self['r'] = r

class Ellipse(BaseElement, ITransform):
    """ The <ellipse> element defines an ellipse which is axis-aligned with the
    current user coordinate system based on a center point and two radii.

    .. automethod:: svgwrite.shapes.Ellipse.__init__

    **SVG Attributes**

    * **cx** -- `coordinate` The x-axis coordinate of the center of the ellipse.
    * **cy** -- `coordinate` The y-axis coordinate of the center of the ellipse.
    * **rx** -- `length` The x-axis radius of the ellipse.
    * **ry** -- `length` The y-axis radius of the ellipse.
    """
    elementname = 'ellipse'

    def __init__(self, center=(0, 0), r=(1, 1), attribs=None, **extra):
        """
        :param 2-tuple center: ellipse center point (cx, cy)
        :param 2-tuple r: ellipse radii (rx, ry)
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Ellipse, self).__init__(attribs=attribs, **extra)
        cx, cy = center
        rx, ry = r
        self['cx'] = cx
        self['cy'] = cy
        self['rx'] = rx
        self['ry'] = ry

class Polyline(BaseElement, ITransform):
    """ The <polyline> element defines a set of connected straight line segments.
    Typically, <polyline> elements define open shapes.

    .. automethod:: svgwrite.shapes.Polyline.__init__

    **Attributes**

    .. attribute:: Polyline.points

       *list* of points, a point is a <2-tuple> (x, y): x, y = <number>

    **SVG Attributes**

    * **points** -- <list-of-points> The points that make up the polyline.
       All coordinate values are in the **user coordinate system** (no units
       allowed).

    How to append points::

        Polyline.points.append( point )
        Polyline.points.extend( [point1, point2, point3, ...] )
    """
    elementname = 'polyline'

    def __init__(self, points=[], attribs=None, **extra):
        """
        :param `iterable` points: of points and points are <2-tuple>s
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Polyline, self).__init__(attribs=attribs, **extra)
        if self.debug:
            for point in points:
                x, y = point
                self.validator.check_svg_type(x, 'number')
                self.validator.check_svg_type(y, 'number')
        self.points = list(points)

    def get_xml(self):
        self.attribs['points'] = self.points_to_string(self.points)
        return super(Polyline, self).get_xml()

    def points_to_string(self, points):
        """
        Convert a <list> of points <2-tuples> to a <string> ``'p1x,p1y p2x,p2y ...'``.

        """
        strings = []
        for point in points:
            if len(point) != 2:
                raise TypeError('got %s values, but expected 2 values.' % len(point))
            x, y = point
            if self.debug:
                self.validator.check_svg_type(x, 'coordinate')
                self.validator.check_svg_type(y, 'coordinate')
            if self.profile == 'tiny':
                if isinstance(x, float):
                    x = round(x, 4)
                if isinstance(y, float):
                    y = round(y, 4)
            point = u"%s,%s" % (x, y)
            strings.append(point)
        return u' '.join(strings)

class Polygon(Polyline):
    """ The <polygon> element defines a closed shape consisting of a set of connected
    straight line segments.

    Same as :class:`~svgwrite.shapes.Polyline` but closed.
    """
    elementname = 'polygon'

