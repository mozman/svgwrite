#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: validator2 module - new validator module
# Created: 01.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from tiny12attributes import tiny12_attributes
from tiny12elements import tiny12_elements
import tiny12typechecker

class Tiny12Validator(object):
    def __init__(self, debug=True):
        self.debug = debug
        self._init_data()

    def _init_data(self):
        self.attributes = tiny12_attributes
        self.elements = tiny12_elements
        self.typechecker = tiny12typechecker.checkfuncs

    def check_all_svg_attribs(self, elementname, attributes):
        for attributename, value in attributes.iteritems():
            self.check_svg_attrib(elementname, attributename, value)

    def check_svg_attrib(self, elementname, attributename, value):
        if self.is_valid_svg_attribute(elementname, attributename):
            self.check_svg_value(elementname, attributename, value)
        else:
            raise ValueError("Attribute '%s' is not a valid SVG Attribute for" \
                             " Element '%s'." % (attributename, elementname))

    def check_svg_value(self, elementname, attributename, value):
        attribute = self.attributes[attributename]
        # check if value match a valid datatype
        for typename in attribute.valid_types:
            if self.typechecker[typename](value):
                return True
        # check if value is a valid constant
        valuestr = str(value)
        return valuestr in attribute.valid_const

    def is_valid_elementname(self, elementname):
        return elementname in self.elements

    def is_valid_svg_attribute(self, elementname, attributename):
        element = self.elements[elementname]
        return attributename in element.valid_attributes

    def is_valid_children(self, elementname, children_name):
        element = self.elements[elementname]
        return children_name in element.valid_children

class Full11Validator(Tiny12Validator):
    def _init_data(self):
        self.attributes = full11_attributes
        self.elements = full11_elements
        self.typechecker = full11typechecker.checkfuncs

