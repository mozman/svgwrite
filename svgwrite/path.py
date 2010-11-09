#coding:utf-8
# Author:  mozman
# Purpose: svg path element
# Created: 08.09.2010
#
#    Copyright (C) 2010  Manfred Moitzi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from svgwrite.base import BaseElement
from svgwrite.utils import strlist
from svgwrite.mixins import Presentation, Markers, Transform
from svgwrite.utils import to_unicode

class Path(BaseElement, Transform, Presentation, Markers):
    """ The <path> element represent the outline of a shape which can be filled,
    stroked, used as a clipping path, or any combination of the three.

    """
    elementname = 'path'
    def __init__(self, d=None, **extra):
        """
        :param `iterable` d: *coordinates*, *length* and *commands*
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments

        """
        super(Path, self).__init__(**extra)
        self.commands = []
        self.push(d)
        if self.debug:
            self.validator.check_all_svg_attribute_values(self.elementname, self.attribs)


    def push(self, *elements):
        """ Push commands and coordinats onto the command stack.

        :param `iterable` elements: *coordinates*, *length* and *commands*

        """
        self.commands.extend(elements)

    @staticmethod
    def arc_flags(large_arc=True, angle_dir='+'):
        large_arc_flag = int(large_arc)
        sweep_flag = {'+': 1, '-': 0}[angle_dir]
        return "%d,%d" % (large_arc_flag, sweep_flag)

    def push_arc(self, target, rotation, r, large_arc=True, angle_dir='+', absolute=False):
        """ Helper function for the elliptical-arc command.

        see SVG-Reference: http://www.w3.org/TR/SVG11/paths.html#PathData

        :param 2-tuple target: *coordinate* of the arc end point
        :param number rotation: x-axis-rotation of the ellipse in degrees
        :param number|2-tuple r: radii rx, ry when r is a *2-tuple* or rx=ry=r if r is a *number*
        :param bool large_arc: draw the arc sweep of greater than or equal to 180 degrees (**large-arc-flag**)
        :param angle_dir: ``'+|-'`` ``'+'`` means the arc will be drawn in a "positive-angle" direction (**sweep-flag**)
        :param bool absolute: indicates that target *coordinates* are absolute else they are relative to the current point

        """
        self.push({ True: 'A', False: 'a' }[absolute])
        if isinstance(r, (float, int)):
            self.push(r, r)
        else:
            self.push(r)
        self.push(rotation)
        self.push(Path.arc_flags(large_arc, angle_dir))
        self.push(target)

    def get_xml(self):
        """ Get the XML representation as `ElementTree` object.

        :return: XML `ElementTree` of this object and all its subelements

        """
        self.attribs['d'] = to_unicode(strlist(self.commands, ' '))
        return super(Path, self).get_xml()
