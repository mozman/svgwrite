#coding:utf-8
# Author:  mozman
# Purpose: svg interface classes
# Created: 16.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

_horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
_vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}

from utils import strlist

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
        self._add_transformation("translate(%s)" % strlist(tx, ty))

    def rotate(self, angle, center=None):
        if center:
            self._add_transformation("rotate(%s, %s, %s)" % (angle, center[0], center[1]))
        else:
            self._add_transformation("rotate(%s)" % angle)

    def scale(self, sx, sy=None):
        self._add_transformation("scale(%s)" % strlist(sx, sy))

    def skewX(self, angle):
        self._add_transformation("skewX(%s)" % angle)

    def skewY(self, angle):
        self._add_transformation("skewY(%s)" % angle)

    def matrix(self, a, b, c, d, e, f):
        self._add_transformation("matrix(%s)" % strlist(a, b, c, d, e, f))

    def rev(self, tx=None, ty=None):
        self._add_transformation("rev(%s)" % strlist('svg', tx, ty))

    def del_transform(self):
        self.attribs.pop('transform', None)

    def _add_transformation(self, new_transform):
        old_transform = self.attribs.get('transform', '')
        self.attribs['transform'] = ("%s %s" % (old_transform, new_transform)).strip()
