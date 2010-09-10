#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import xml.etree.ElementTree as etree

import parameter
from svgwrite.utils import attrib_to_string

class BaseElement(object):
    def __init__(self, attribs=None, **kwargs):
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.update(kwargs)
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
        for key, value in self.attribs:
            self._check_attrib(key, )
            attrib[key] = attrib_to_string(value)
        xml = etree.Element(self._element_name, attrib)
        for element in self.elements:
            xml.append(element.get_xml())
        return xml

    def _element_name(self):
        return self.__class__.__name__.lower()

    def _check_attrib(self, attrib):
        if parameter.debug_mode and attrib not in self._valid_attribs():
            raise ValueError("Invalid parameter '%s'" % attrib)
