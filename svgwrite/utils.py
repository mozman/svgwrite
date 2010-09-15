#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg util functions and classes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import parameter
from validator import check_tiny, check_coordinate

_horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
_vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}

def fit(horiz="center", vert="middle", scale="meet"):
    """ Returns the preserveAspectRatio string.

    Parameter:
    ----------
    horiz -- 'left' | 'center' | 'right'
    vert -- 'top' | 'middle' | 'bottom'
    scale -- 'meet' | 'slice'
        meet = preserve aspect ration and zoom to limits of viewBox
        slice = preserve aspect ration and viewBox touch viewport on all bounds,
                viewBox will extend beyond the bounds of the viewport
    """
    return _horiz[horiz]+_vert[vert]+' '+scale

def rgb(r=0, g=0, b=0, mode='RGB'):
    """Convert r, g, b values to a string.

    mode -- "RGB" returnd a rgb-string format: 'rgb(r, g, b)'
    mode -- "%" returns percent-values as rgb-string format: 'rgb(r%, g%, b%)'
    """
    def percent(value):
        value = float(value)
        if value < 0.:
            value = 0.
        if value > 100.:
            value = 100.
        return value

    if mode.upper() == 'RGB':
        return u"rgb(%d,%d,%d)" % (int(r) & 255, int(g) & 255, int(b) & 255)
    elif mode == "%":
        return u"rgb(%.3f%%,%.3f%%,%.3f%%)" % (percent(r), percent(g), percent(b))
    else:
        raise ValueError("Invalid mode '%s'" % mode)

def value_to_string(value):
    if parameter.debug_mode and parameter.profile=='tiny' and isinstance(value, (int, float)):
        check_tiny(value)
    return unicode(value)

def points_to_string(points):
    strings = []
    profile = parameter.profile
    debug_mode = parameter.debug_mode
    for point in points:
        if isinstance(point, tuple):
            if len(point) != 2:
                raise ValueError("<2-tuple> is required: '%s'" % str(point))
            if debug_mode:
                check_coordinate(point[0], profile)
                check_coordinate(point[1], profile)
            point = u"%s,%s" % point
        else:
            TypeError("'%s' <string> is given, but <2-tuple> is required." % point)
        strings.append(point)
    return u' '.join(strings)
