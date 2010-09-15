#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import xml.etree.ElementTree as etree

import parameter
from svgwrite.utils import value_to_string
from svgwrite.validator import check_attribute_names, check_attribute_value, \
     check_valid_content, check_coordinate

class BaseElement(object):
    def __init__(self, attribs=None, **kwargs):
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.attribs.update(kwargs)
        if parameter.debug_mode:
            check_attribute_names(self._elementname(), self.attribs)
        self.elements = list()

    def __getitem__(self, key):
        return self.attribs[key]

    def __setitem__(self, key, value):
        self.attribs[key] = value
        if parameter.debug_mode:
            check_attribute_names(self._elementname(), self.attribs)

    def append(self, element):
        """ append subelement """
        if parameter.debug_mode:
            check_valid_content(self._elementname(), element._elementname())
        self.elements.append(element)

    def tostring(self):
        """ get XML as string representation. """
        xml = self.get_xml()
        return etree.tostring(xml, encoding='utf-8')

    def get_xml(self):
        """ get XML as ElementTree object. """
        debug_mode = parameter.debug_mode
        if debug_mode:
            check_attribute_names(self._elementname(), self.attribs)
        xml = etree.Element(self._elementname())
        for attribute, value in self.attribs.iteritems():
            value = value_to_string(value)
            if debug_mode:
                check_attribute_value(attribute, value)
            xml.set(attribute, value)

        for element in self.elements:
            xml.append(element.get_xml())
        return xml

    def _elementname(self):
        name = self.__class__.__name__
        return name[0].lower() + name[1:]

class IViewBox(object):
    _horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
    _vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}
    """ viewBox Interface """
    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Set the svg 'viewBox' attribute, arguments are <coordinate> values.
        """
        for value in (minx, miny, width, height):
            check_coordinate(value)
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
