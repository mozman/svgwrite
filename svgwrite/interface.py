#coding:utf-8
# Author:  mozman
# Purpose: svg interface classes
# Created: 16.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

_horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
_vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}

from utils import strlist
from validator import check_coordinate, check_angle

class IViewBox(object):
    """ viewBox Interface """
    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Set the 'viewBox' attribute, arguments are <coordinate> values.
        """
        for value in (minx, miny, width, height):
            check_coordinate(value, parameter.profile)
        self.attribs['viewBox'] = "%s,%s,%s,%s" % (minx, miny, width, height)

    def stretch(self):
        """ strech viewBox in x and y direction to fill viewport, does not
        preserve aspect ratio.
        """
        self.attributes['preserveAspectRatio'] = 'none'

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
        self.attributes['preserveAspectRatio'] = "%s%s %s" % (_horiz[horiz],_vert[vert], scale)

class ITransform(object):
    def translate(self, tx, ty=None):
        check_coordinate(tx)
        if ty : check_coordinate(ty)
        self._add_transformation("translate(%s)" % strlist(tx, ty))

    def rotate(self, angle, center=None):
        check_angle(angle)
        if center:
            check_coordinate(center[0])
            check_coordinate(center[1])
        self._add_transformation("rotate(%s)" % strlist(angle, center))

    def scale(self, sx, sy=None):
        check_coordinate(sx)
        if sy : check_coordinate(sy)
        self._add_transformation("scale(%s)" % strlist(sx, sy))

    def skewX(self, angle):
        self._add_transformation("skewX(%s)" % check_angle(angle))

    def skewY(self, angle):
        self._add_transformation("skewY(%s)" % check_angle(angle))

    def matrix(self, a, b, c, d, e, f):
        self._add_transformation("matrix(%s)" % strlist(a, b, c, d, e, f))

    def rev(self, tx=None, ty=None):
        check_coordinate(tx)
        if ty : check_coordinate(ty)
        self._add_transformation("rev(%s)" % strlist('svg', tx, ty))

    def del_transform(self):
        self.attribs.pop('transform', None)

    def _add_transformation(self, new_transform):
        old_transform = self.attribs.get('transform', '')
        self.attribs['transform'] = ("%s %s" % (old_transform, new_transform)).strip()
