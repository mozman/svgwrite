#coding:utf-8
# Author:  mozman
# Purpose: svg path element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite.base import BaseElement
from svgwrite.utils import strlist
from svgwrite.interface import ITransform

class Path(BaseElement, ITransform):
    """ The <path> element represent the outline of a shape which can be filled,
    stroked, used as a clipping path, or any combination of the three.

    .. automethod:: svgwrite.Path.__init__

    **Attributes**

    .. attribute:: commands

       `list` -- the command and coordinate stack

    **Methods**

    .. automethod:: svgwrite.Path.push(commands)

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.Path.add(element)

    .. automethod:: svgwrite.Path.tostring()

    .. automethod:: svgwrite.Path.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    .. _path command:

    **Path Commands**

    Uppercase commands indicates absolute coordinates, lowercase commands
    indicates relative coordinates

    * **'h', 'H' x+** -- Draws a horizontal line from the current point (cpx, cpy) to (x, cpy).
    * **'v', 'V' y+** -- Draws a vertical line from the current point (cpx, cpy) to (cpx, y).
    * **'l', 'L' (x y)+** -- Draw a line from the current point to the given (x,y) coordinate.
    * **'m', 'M' (x y)+** -- Start a new sub-path at the given (x,y) coordinate.
      If a moveto is followed by multiple pairs of coordinates, the subsequent
      pairs are treated as implicit lineto commands. Hence, implicit lineto
      commands will be relative if the moveto is relative, and absolute if the
      moveto is absolute. If a relative moveto (m) appears as the first element
      of the path, then it is treated as a pair of absolute coordinates.
      In this case, subsequent pairs of coordinates are treated as relative even
      though the initial moveto is interpreted as an absolute moveto.
    * **'c', 'C' (x1 y1 x2 y2 x y)+** -- Draws a cubic Bézier curve from the current point
      to (x,y) using (x1,y1) as the control point at the beginning of the curve
      and (x2,y2) as the control point at the end of the curve.
    * **'s', 'S' (x2 y2 x y)+** -- Draws a cubic Bézier curve from the current point to
      (x,y). The first control point is assumed to be the reflection of the second
      control point on the previous command relative to the current point. (If
      there is no previous command or if the previous command was not an C, c,
      S or s, assume the first control point is coincident with the current point.)
      (x2,y2) is the second control point (i.e., the control point at the end of
      the curve).
    * **'q', 'Q' (x1 y1 x y)+** -- Draws a quadratic Bézier curve from the current point
      to (x,y) using (x1,y1) as the control point.
    * **'t', 'T' (x y)+** -- Draws a quadratic Bézier curve from the current point to (x,y).
      The control point is assumed to be the reflection of the control point on
      the previous command relative to the current point. (If there is no previous
      command or if the previous command was not a Q, q, T or t, assume the control
      point is coincident with the current point.)
    * **'a', 'A' (rx ry x-axis-rotation large-arc-flag sweep-flag x y)+** -- Draws an
      elliptical arc from the current point to (x, y). The size and orientation
      of the ellipse are defined by two radii (rx, ry) and an x-axis-rotation,
      which indicates how the ellipse as a whole is rotated relative to the
      current coordinate system. The center (cx, cy) of the ellipse is
      calculated automatically to satisfy the constraints imposed by the other
      parameters. large-arc-flag and sweep-flag contribute to the automatic
      calculations and help determine how the arc is drawn.
    * **'z', 'Z'** -- close current subpath

    **Supported SVG attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering can proceed
      even if external resources are unavailable else: *True*
    * **transform** -- use :class:`svgwrite.interface.ITransform` interface
    * **pathLength** -- the *pathLength* attribute can be used to provide the author's
      computation of the total length of the path so that the user agent can
      scale distance-along-a-path computations by the ratio of 'pathLength' to
      the user agent's own computed value for total path length.
      A "moveto" operation within a 'path' element is defined to have zero length.
    * **d** -- The definition of the outline of a shape, use push-method to add commands
      and coordinates

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    elementname = 'path'
    def __init__(self, d=None, attribs=None, **extra):
        """
        :param `iterable` d: *coordinates*, *length* and *commands*
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Path, self).__init__(attribs, **extra)
        self.commands = []
        self.push(d)


    def push(self, *elements):
        """ Push commands and coordinats onto the command stack.

        :param `iterable` elements: *coordinates*, *length* and *commands*

        """
        self.commands.extend(elements)

    def get_xml(self):
        """ Get the XML representation as `ElementTree` object.

        :return: XML `ElementTree` of this object and all its subelements

        see `path command`_

        """
        self.attribs['d'] = unicode(strlist(self.commands, ' '))
        return super(Path, self).get_xml()
