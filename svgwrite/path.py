#coding:utf-8
# Author:  mozman
# Purpose: svg path element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite.base import BaseElement
from svgwrite.utils import strlist2
from svgwrite.interface import ITransform

class Path(BaseElement, ITransform):
    """ *Paths* represent the outline of a shape which can be filled, stroked,
    used as a clipping path, or any combination of the three.

    Methods:
    --------
    push(*commands) -- add commands or points or both

    Attributes:
    -----------
    commands -- <list> command and coordinate stack

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

    Path-Commands:
    --------------
    Uppercase commands indicates absolute coordinates
    Lowercase commands indicates relative coordinates

    'h', 'H' x+ -- horizontal lineto
    'v', 'V' y+ -- vertical lineto
    'l', 'L' (x y)+ -- lineto
    'm', 'M' (x y)+ -- moveto
    'c', 'C' (x1 y1 x2 y2 x y)+ -- cubic Bézier curve to
    's', 'S' (x2 y2 x y)+ -- shorthand/smooth cubic Bézier curveto
    'q', 'Q' (x1 y1 x y)+ -- quadratic Bézier curveto
    't', 'T' (x y)+ -- Shorthand/smooth quadratic Bézier curveto
    'a', 'A' (rx ry x-axis-rotation large-arc-flag sweep-flag x y)+ -- elliptical arc
    'z', 'Z' -- closepath

    Supported svg-attributes:
    -------------------------
    class -- <string> assigns one or more css-class-names to an element
    style -- <string> allows per-element css-style rules to be specified directly on a given element
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true
    transform -- use ITransform interface
    pathLength -- the 'pathLength' attribute can be used to provide the author's
        computation of the total length of the path so that the user agent can
        scale distance-along-a-path computations by the ratio of 'pathLength' to
        the user agent's own computed value for total path length.
        A "moveto" operation within a 'path' element is defined to have zero length.
    d -- The definition of the outline of a shape, use push-method to add commands
        and coordinates

    Standard SVG Attributes:
    ------------------------
    see description in  **base.py**

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    def __init__(self, d=None, attribs=None, **kwargs):
        super(Path, self).__init__(attribs, **kwargs)
        self.commands = []
        self.push(d)


    def push(self, *elements):
        """ Push commands and coordinats onto the command stack.

        Path-Commands:
        --------------
        Uppercase commands indicates absolute coordinates
        Lowercase commands indicates relative coordinates

        'h', 'H' x+ -- Draws a horizontal line from the current point (cpx, cpy) to (x, cpy).

        'v', 'V' y+ -- Draws a vertical line from the current point (cpx, cpy) to (cpx, y).

        'l', 'L' (x y)+ -- Draw a line from the current point to the given (x,y) coordinate.

        'm', 'M' (x y)+ -- Start a new sub-path at the given (x,y) coordinate.
            If a moveto is followed by multiple pairs of coordinates, the subsequent
            pairs are treated as implicit lineto commands. Hence, implicit lineto
            commands will be relative if the moveto is relative, and absolute if the
            moveto is absolute. If a relative moveto (m) appears as the first element
            of the path, then it is treated as a pair of absolute coordinates.
            In this case, subsequent pairs of coordinates are treated as relative even
            though the initial moveto is interpreted as an absolute moveto.

        'c', 'C' (x1 y1 x2 y2 x y)+ -- Draws a cubic Bézier curve from the current point
            to (x,y) using (x1,y1) as the control point at the beginning of the curve
            and (x2,y2) as the control point at the end of the curve.

        's', 'S' (x2 y2 x y)+ -- Draws a cubic Bézier curve from the current point to
            (x,y). The first control point is assumed to be the reflection of the second
            control point on the previous command relative to the current point. (If
            there is no previous command or if the previous command was not an C, c,
            S or s, assume the first control point is coincident with the current point.)
            (x2,y2) is the second control point (i.e., the control point at the end of
            the curve).

        'q', 'Q' (x1 y1 x y)+ -- Draws a quadratic Bézier curve from the current point
            to (x,y) using (x1,y1) as the control point.

        't', 'T' (x y)+ -- Draws a quadratic Bézier curve from the current point to (x,y).
            The control point is assumed to be the reflection of the control point on
            the previous command relative to the current point. (If there is no previous
            command or if the previous command was not a Q, q, T or t, assume the control
            point is coincident with the current point.)

        'a', 'A' (rx ry x-axis-rotation large-arc-flag sweep-flag x y)+ -- Draws an
            elliptical arc from the current point to (x, y). The size and orientation
            of the ellipse are defined by two radii (rx, ry) and an x-axis-rotation,
            which indicates how the ellipse as a whole is rotated relative to the
            current coordinate system. The center (cx, cy) of the ellipse is
            calculated automatically to satisfy the constraints imposed by the other
            parameters. large-arc-flag and sweep-flag contribute to the automatic
            calculations and help determine how the arc is drawn.

        'z', 'Z' -- close current subpath
        """
        self.commands.extend(elements)

    def get_xml(self):
        self.attribs['d'] = unicode(strlist2(self.commands))
        return super(Path, self).get_xml()
