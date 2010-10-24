#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: mixins
# Created: 19.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from utils import strlist

class Presentation(object):
    """
    Helper methods to set presentation attributes.
    """
    def fill(self, color=None, rule=None, opacity=None):
        """
        Set SVG Properties **fill**, **fill-rule** and **fill-opacity**.

        """
        if color:
            self['fill'] = color
        if rule:
            self['fill-rule'] = rule
        if opacity:
            self['fill-opacity'] = opacity
        return self

    def stroke(self, color=None, width=None, opacity=None, linecap=None,
               linejoin=None, miterlimit=None):
        """
        Set SVG Properties **stroke**, **stroke-width**, **stroke-opacity**,
        **stroke-linecap** and **stroke-miterlimit**.

        """

        if color:
            self['stroke'] = color
        if width:
            self['stroke-width'] = width
        if opacity:
            self['stroke-opacity'] = opacity
        if linecap:
            self['stroke-linecap'] = linecap
        if linejoin:
            self['stroke-linejoin'] = linejoin
        if miterlimit:
            self['stroke-miterlimit'] = miterlimit
        return self

    def dasharray(self, dasharray=None, offset=None):
        """
        Set SVG Properties **stroke-dashoffset** and **stroke-dasharray**.

        Where *dasharray* specify the lengths of alternating dashes and gaps as
        <list> of <int> or <float> values or a <string> of comma and/or white
        space separated <lengths> or <percentages>. (e.g. as <list> dasharray=[1, 0.5]
        or as <string> dasharray='1 0.5')
        """
        if dasharray:
            self['stroke-dasharray'] = strlist(dasharray, ' ')
        if offset:
            self['stroke-dashoffset'] = offset
        return self

class MediaGroup(object):
    """
    Helper methods to set media group attributes.

    """

    def viewport_fill(self, color=None, opacity=None):
        """
        Set SVG Properties **viewport-fill** and **viewport-fill-opacity**.

        """
        if color:
            self['viewport-fill'] = color
        if opacity:
            self['viewport-fill-opacity'] = opacity
        return self
