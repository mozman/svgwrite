#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg util functions and classes
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

__all__ = ['rgb']

def rgb(r=0, g=0, b=0, mode="HEX"):
    """Convert r, g, b values to a string.

    mode -- "HEX" returns a hex-string format: #rrggbb
    mode -- "RGB" returna a rgb-string format: rgb(rr, gg, bb)
    mode -- "%" returns a rgb%-string format: rgb(rr%, gg%, bb%)
    """
    def percent(value):
        value = float(value)
        if value < 0.:
            value = 0.
        if value > 100.:
            value = 100.
        return value
    if mode.upper() == "HEX":
        return "#%02X%02X%02X" % (int(r) & 255, int(g) & 255, int(b) % 255)
    else if mode.upper() == "RGB":
        return "rgb(%d, %d, %d)" % (int(r) & 255, int(g) & 255, int(b) % 255)
    else if mode == "%":
        return "rgb(%.3f%%, %.3f%%, %.3f%%)" % (percent(r), percent(g), percent(b))
