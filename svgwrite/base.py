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
from svgwrite.validator import check_attribs

class BaseElement(object):
    def __init__(self, attribs=None, **kwargs):
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.attribs.update(kwargs)
        self.elements = list()

    def __getitem__(self, key):
        return self.attribs[key]

    def __setitem__(self, key, value):
        self.attribs[key] = value

    def append(self, element):
        """ append subelement """
        self.elements.append(element)

    def tostring(self):
        """ get XML as string representation. """
        xml = self.get_xml()
        return etree.tostring(xml)

    def get_xml(self):
        """ get XML as ElementTree object. """
        attrib = {}
        keys = self.attribs.keys()
        if parameter.debug_mode:
            keys.sort() # for testing resons
            check_attribs(self._elementname(), self.attribs)
        for key in keys:
            attrib[key] = value_to_string(self.attribs[key])
        xml = etree.Element(self._elementname(), attrib)
        for element in self.elements:
            xml.append(element.get_xml())
        return xml

    def _elementname(self):
        name = self.__class__.__name__
        return name[0].lower() + name[1:]

class GenericElement(BaseElement):
    def __init__(self, elementname, attribs=None, **kwargs):
        super(GenericElement, self).__init__(attribs, **kwargs)
        self.elementname = elementname
    def _elementname(self):
        return self.elementname