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
from svgwrite.validator import check_attribute_names, check_attribute_value, check_valid_content

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
            check_attribute_names(self._elementname, self.attribs)

    def append(self, element):
        """ append subelement """
        if parameter.debug_mode:
            check_valid_content(self._elementname, element._elementname)
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
