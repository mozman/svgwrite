#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svgwrite package parameter
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

__docformat__ = "restructuredtext en"

debug_mode = False
profile = "full" # full, basic or tiny

def init(baseProfile="full", debug=False):
    global debug_mode
    debug_mode = debug
    baseProfile = baseProfile.lower()
    if baseProfile in ('tiny', 'basic', 'full'):
        global profile
        profile = baseProfile
    else:
        raise ValueError("'%s' is not a valid profile." % baseProfile)