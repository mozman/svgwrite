#coding:utf-8
# Author:  mozman
# Purpose: svg interface classes
# Created: 16.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

class IViewBox(object):
    _horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
    _vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}
    """ viewBox Interface """
    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Set the svg 'viewBox' attribute, arguments are <coordinate> values.
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

class IGroup(object):
    """ group interface """

