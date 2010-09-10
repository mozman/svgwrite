#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svgwrite package parameter
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

debug_mode = False
profile = "full" # full, basic or tiny
valid_units = ['em', 'ex', 'px', 'pt', 'pc', 'cm', 'mm', 'in', '%']

def verify(baseProfile="full", debug=False):
    global debug_mode
    debug_mode = debug
    global profile
    profile = baseProfile.lower()

def _split_coordinate(value):
    """ Split value in (number, unit) if value has an unit or (number, None). """
    try:
        return float(value), None
    except ValueError:
        value = value.strip().lower()
        if value[-1] == '%':
            return float(value[:-1]), '%'
        elif value[-2:] in valid_units:
            return float(value[:-2]), value[-2:]
        else:
            raise ValueError("'%s' has not a valid svg unit." % value)

def get_coordinate(value):
    """ Get coordinate (number, unit), unit is None if value doesn't have a unit,
    raises ValueError if not valid."""
    number, unit = _split_coordinate(value)
    if profile == 'tiny': # check value range of tiny profile
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
