#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: package definition file
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

"""
A Python library to create SVG drawings.

SVG is a language for describing two-dimensional graphics in XML. SVG allows
for three types of graphic objects: vector graphic shapes (e.g., paths
consisting of straight lines and curves), images and text. Graphical objects
can be grouped, styled, transformed and composited into previously rendered
objects. The feature set includes nested transformations, clipping paths,
alpha masks, filter effects and template objects.

SVG drawings can be interactive and dynamic. Animations can be defined and
triggered either declarative (i.e., by embedding SVG animation elements in
SVG content) or via scripting.

.. seealso:: http://www.w3.org/TR/SVG11/intro.html#AboutSVG

a simple example::

    import svgwrite

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2))
    dwg.save()

SVG Version
-----------

You can only create two types of SVG drawings:

* *SVG 1.2 Tiny Profile*, use Drawing(profile= ``'tiny'``)
* *SVG 1.1 Full Profile*, use Drawing(profile= ``'full'``)

"""

version = (1, 0, 1)
VERSION = '%d.%d.%d' % version

AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'mozman@gmx.at'
CYEAR = '2012'

from svgwrite.drawing import Drawing
from svgwrite.utils import rgb

class Unit(object):
    """ Add units to values.
    """
    def __init__(self, unit='cm'):
        """ Unit constructor

        :param str unit: specify the unit string
        """
        self._unit=unit

    def __rmul__(self, other):
        """ add unit-strint to 'other'. (e.g. 5*cm => '5cm') """
        return "%s%s" % (other, self._unit)

    def __call__(self, *args):
        """ Add unit-strings to all arguments.

        :param args: list of values
            e.g.: cm(1,2,3) => '1cm,2cm,3cm'
        """
        return ','.join(["%s%s" % (arg, self._unit) for arg in args])

cm = Unit('cm')
mm = Unit('mm')
em = Unit('em')
ex = Unit('ex')
px = Unit('px')
inch = Unit('in')
pc = Unit('pc')
pt = Unit('pt')
percent = Unit('%')
deg = Unit('deg')
grad = Unit('grad')
rad = Unit('rad')
Hz = Unit('Hz')
kHz = Unit('kHz')
