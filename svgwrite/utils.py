#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg util functions and classes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import parameter

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
        return "rgb(%d, %d, %d)" % (int(r) & 255, int(g) & 255, int(b) % 255)
    else if mode == "%":
        return "rgb(%.3f%%, %.3f%%, %.3f%%)" % (percent(r), percent(g), percent(b))

def attrib_to_string(value):
    if parameter.debug_mode and parameter.profile=='tiny' and isinstance(value, [int, float]):
        check_tiny(value)
    return unicode(value)

def points_to_string(points):
    strings = []
    for point in points:
        if isinstance(point, tuple):
            parameter.check_coordinate(point[0])
            parameter.check_coordinate(point[1])
            point = "%s,%s" % point
        strings.append(point)
    return ' '.join(strings)
