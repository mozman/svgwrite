#coding:utf-8
# Author:  mozman
# Purpose: svg interface classes
# Created: 16.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

_horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
_vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}

import parameter

from utils import strlist
from validator import check_coordinate, check_angle, check_number

class IViewBox(object):
    """ viewBox Interface operates on USER SPACE coordinates - no units allowed."""
    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Specify a rectangle in USER SPACE (no units allowed) which should be
        mapped to the bounds of the viewport established by the given element.
        """
        if parameter.debug_mode:
            for value in (minx, miny, width, height):
                check_number(value, parameter.profile)
        self.attribs['viewBox'] = strlist(minx, miny, width, height)

    def stretch(self):
        """ strech viewBox in x and y direction to fill viewport, does not
        preserve aspect ratio.
        """
        self.attribs['preserveAspectRatio'] = 'none'

    def fit(self, horiz="center", vert="middle", scale="meet"):
        """ Set the preserveAspectRatio attribute.

        Parameter:
        ----------
        horiz -- 'left' | 'center' | 'right'
        vert -- 'top' | 'middle' | 'bottom'
        scale -- 'meet' | 'slice'
            meet = preserve aspect ration and zoom to limits of viewBox
            slice = preserve aspect ration and viewBox touch viewport on all bounds,
                    viewBox will extend beyond the bounds of the viewport
        """
        self.attribs['preserveAspectRatio'] = "%s%s %s" % (_horiz[horiz],_vert[vert], scale)

class ITransform(object):
    """ Transform operates on USER SPACE coordinates, no units allowed """
    def translate(self, tx, ty=None):
        """ tx, ty in USER SPACE coordinates - no units allowed """
        if parameter.debug_mode:
            profile = parameter.profile
            check_number(tx, profile)
            if ty : check_number(ty, profile)
        self._add_transformation("translate(%s)" % strlist(tx, ty))

    def rotate(self, angle, center=None):
        """ angle in degree, center in USER SPACE coordinates - no units allowed """
        if parameter.debug_mode:
            profile = parameter.profile
            check_number(angle, profile)
            if center:
                check_number(center[0], profile)
                check_number(center[1], profile)
        self._add_transformation("rotate(%s)" % strlist(angle, center))

    def scale(self, sx, sy=None):
        """ sx, sy are scalar values, no units allowed. """
        if parameter.debug_mode:
            profile = parameter.profile
            check_number(sx)
            if sy : check_number(sy)
        self._add_transformation("scale(%s)" % strlist(sx, sy))

    def skewX(self, angle):
        """ angle in degree, no units allowed """
        if parameter.debug_mode:
            check_number(angle, parameter.profile)
        self._add_transformation("skewX(%s)" % angle)

    def skewY(self, angle):
        """ angle in degree, no units allowed """
        if parameter.debug_mode:
            check_number(angle, parameter.profile)
        self._add_transformation("skewY(%s)" % angle)

    def matrix(self, a, b, c, d, e, f):
        self._add_transformation("matrix(%s)" % strlist(a, b, c, d, e, f))

    def rev(self, tx=None, ty=None):
        """ tx, ty in USER SPACE coordinates (parent system) - no units allowed """
        if parameter.debug_mode:
            profile = parameter.profile
            check_number(tx)
            if ty : check_number(ty)
        self._add_transformation("rev(%s)" % strlist('svg', tx, ty))

    def del_transform(self):
        self.attribs.pop('transform', None)

    def _add_transformation(self, new_transform):
        old_transform = self.attribs.get('transform', '')
        self.attribs['transform'] = ("%s %s" % (old_transform, new_transform)).strip()
