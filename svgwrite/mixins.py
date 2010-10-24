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

class Markers(object):
    """
    Helper methods to set marker attributes.

    """
    def set_markers(self, markers):
        """
        Set markers for line elements (line, polygon, polyline, path) to
        values specified by  `markers`.

        * if `markers` is a 3-tuple:

          * attribute 'marker-start' = markers[0]
          * attribute 'marker-mid' = markers[1]
          * attribute 'marker-end' = markers[2]

        * `markers` is as `string` or a `Marker` class:

          * attribute 'marker' = markers

        """
        def get_funciri(value):
            if isinstance(value, basestring):
                # strings has to be a valid reference including the '#'
                return 'url(%s)' % value
            else:
                # else create a reference to the object '#id'
                return 'url(#%s)' % value['id']
        if isinstance(markers, basestring):
            self['marker'] = get_funciri(markers)
        else:
            try:
                markerstart, markermid, markerend = markers
                self['marker-start'] = get_funciri(markerstart)
                self['marker-mid'] = get_funciri(markermid)
                self['marker-end'] = get_funciri(markerend)
            except (TypeError, KeyError):
                self['marker'] = get_funciri(markers)
