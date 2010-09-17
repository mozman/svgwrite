#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: package definition file
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from parameter import init
from drawing import Drawing
from container import Group, Symbol, Use, SVG
from shapes import Line, Rect, Circle, Ellipse, Polygon, Polyline
from path import Path
from utils import rgb

class Unit(object):
    def __init__(self, unit='cm'):
        self._unit=unit

    def __rmul__(self, other):
        """add unit-strint to 'other'. (e.g. 5*cm => '5cm')"""
        return "%s%s" % (other, self._unit)

    def __call__(self, *args):
        """add unit-strings to all arguments.

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