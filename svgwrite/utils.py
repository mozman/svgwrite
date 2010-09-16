#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg util functions and classes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
import re

import parameter
from validator import check_tiny, check_coordinate, _coordinate_pattern

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

def strlist(*args):
    return ",".join([str(value) for value in args if value is not None])

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

def get_unit(coordinate):
    if isinstance(coordinate, (int, float)):
        return None
    result = _coordinate_pattern.match(coordinate)
    if result:
        return result.group(3)
    else:
        raise ValueError("Invalid format: '%s'" % coordinate)

def split_coordinate(coordinate):
    if isinstance(coordinate, (int, float)):
        return (float(coordinate), None)
    result = _coordinate_pattern.match(coordinate)
    if result:
        return (float(result.group(1)), result.group(3))
    else:
        raise ValueError("Invalid format: '%s'" % coordinate)

def rect_top_left_corner(insert, size, pos='top-left'):
    """ Calculate top-left corner of a rectangle.
      - x-coordinate and width has to have the same unit
      - y-coordinate and height has to have the same unit.

    Returns a <2-tuple>

    Parameter:
    ----------
    insert -- <2-tuple> insert point
    size -- <2-tuple> (width, height)
    pos -- <string> insert position 'vert-horiz'
        vert -- 'top'|'middle'|'bottom'
        horiz -- 'left'|'center'|'right'
    """
    vert, horiz = pos.lower().split('-')
    x, xunit = split_coordinate(insert[0])
    y, yunit = split_coordinate(insert[1])
    width, wunit = split_coordinate(size[0])
    height, hunit = split_coordinate(size[1])

    if xunit != wunit:
        raise ValueError("x-coordinate and width has to have the same unit")
    if yunit != hunit:
        raise ValueError("y-coordinate and height has to have the same unit")

    if horiz == 'center':
        x = x - width / 2.
    elif horiz == 'right':
        x = x - width
    elif horiz != 'left':
        ValueError("Invalid horizontal position: '%s'" % horiz)

    if vert == 'middle':
        y = y - height / 2.
    elif vert == 'bottom':
        y = y - height
    elif vert != 'top':
        ValueError("Invalid vertical position: '%s'" % vert)

    if xunit:
        x = "%s%s" %(x, xunit)
    if yunit:
        y = "%s%s" %(y, yunit)
    return (x, y)
