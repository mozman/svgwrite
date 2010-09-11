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
        return "rgb(%d,%d,%d)" % (int(r) & 255, int(g) & 255, int(b) & 255)
    elif mode == "%":
        return "rgb(%.3f%%,%.3f%%,%.3f%%)" % (percent(r), percent(g), percent(b))
    else:
        raise ValueError("Invalide mode '%s'" % mode)

def value_to_string(value):
    if parameter.debug_mode and parameter.profile=='tiny' and isinstance(value, (int, float)):
        check_tiny(value)
    return unicode(value)

def points_to_string(points):
    strings = []
    for point in points:
        if isinstance(point, tuple):
            check_coordinate(point[0])
            check_coordinate(point[1])
            point = "%s,%s" % point
        strings.append(point)
    return ' '.join(strings)

def _split_coordinate(value):
    """ Split value in (number, unit) if value has an unit or (number, None). """
    try:
        return float(value), None
    except ValueError:
        value = value.strip().lower()
        if value[-1] == '%':
            return float(value[:-1]), '%'
        elif value[-2:] in parameter.valid_units:
            return float(value[:-2]), value[-2:]
        else:
            raise ValueError("'%s' has not a valid svg unit." % value)

def get_coordinate(value):
    """ Get coordinate (number, unit), unit is None if value doesn't have a unit,
    raises ValueError if not valid."""
    number, unit = _split_coordinate(value)
    if parameter.profile == 'tiny': # check value range of tiny profile
        number = round(number, 4) # round to four places for tiny profile
        check_tiny(number)
    return number, unit

def check_tiny(number):
    """ Check if number is a valid 'tiny' coordinate, raises ValueError if not valid. """
    if not (-32767.9999 <= number <= 32767.9999):
        raise ValueError("'%s' out of range for baseProfile 'tiny'" % number)

def check_coordinate(value):
    """ Check if value is a valid coordinate, raises ValueError if not valid. """
    if debug_mode:
        number, unit = get_coordinate(value)
    return value
