#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
The **BaseElement** is the root for all SVG elements.
"""

import xml.etree.ElementTree as etree
import copy

from params import Parameter
from utils import AutoID

class BaseElement(object):
    """
    The :class:`BaseElement` is the root for all SVG elements. The SVG attributes
    are stored in :attr:`attribs`, and the SVG subelements are stored in
    :attr:`elements`.

    """
    elementname = 'baseElement'

    def __init__(self, **extra):
        """
        :param dict extra: extra SVG attributes, argument='value'

        SVG attribute names will be checked, if :attr:`self.debug` is `True`.
        """
        factory = extra.pop('factory', None) # the keyword 'factory' specifies the object creator
        if factory is not None:
            self._parameter = factory._parameter # take parameter from 'factory'
        else:
            self._parameter = Parameter() # default parameter debug=True profile='full'

        debug = extra.pop('debug', None) # override debug
        if debug is not None:
            self._parameter.set_debug(debug)

        profile = extra.pop('profile', None) # override profile
        if profile is not None:
            self._parameter.set_profile(profile)

        self.attribs = dict()
        self.update(extra)
        self.elements = list()
        if self.debug:
            self.validator.check_all_svg_attribute_values(self.elementname, self.attribs)

    def update(self, attribs):
        for key, value in attribs.iteritems():
            # remove trailing underscores
            # and replace inner underscores
            key = key.rstrip('_').replace('_', '-')
            self.__setitem__(key, value)

    def copy(self):
        newobj = copy.copy(self) # shallow copy of object
        newobj.attribs = copy.copy(self.attribs) # shallow copy of attributes
        newobj.elements = copy.copy(self.elements) # shallow copy of subelements
        if 'id' in newobj.attribs: # create a new 'id'
            newobj['id'] = newobj.next_id()
        return newobj

    def get_debug(self):
        return self._parameter.debug
    debug = property(get_debug)

    def get_profile(self):
        return self._parameter.profile
    profile = property(get_profile)

    def get_validator(self):
        return self._parameter.validator
    validator = property(get_validator)

    def get_version(self):
        return self._parameter.get_version()

    def set_parameter(self, parameter):
        self._parameter = parameter

    def next_id(self, value=None):
        return AutoID.next_id(value)

    def get_id(self):
        """ Get the object `id` string, if the object does not have an `id`,
        a new `id` will be created.

        :returns: `string`
        """
        if 'id' not in self.attribs:
            self.attribs['id'] = self.next_id()
        return self.attribs['id']

    def get_iri(self):
        """
        Get the `IRI` reference string of the object. (i.e., ``'#id'``).

        :returns: `string`
        """
        return "#%s" % self.get_id()

    def get_funciri(self):
        """
        Get the `FuncIRI` reference string of the object. (i.e. ``'url(#id)'``).

        :returns: `string`
        """
        return "url(%s)" % self.get_iri()

    def __getitem__(self, key):
        """ Get SVG attribute by `key`.

        :param string key: SVG attribute name
        :return: SVG attribute value

        """
        return self.attribs[key]

    def __setitem__(self, key, value):
        """ Set SVG attribute by `key` to `value`.

        :param string key: SVG attribute name
        :param object value: SVG attribute value

        """
        if self.debug:
            self.validator.check_svg_attribute_value(self.elementname, key, value)
        self.attribs[key] = value

    def add(self, element):
        """ Add an SVG element as subelement.

        :param element: append this SVG element

        """
        if self.debug:
            self.validator.check_valid_children(self.elementname, element.elementname)
        self.elements.append(element)
        return element

    def tostring(self):
        """ Get the XML representation as `string`.

        :return: ``utf-8`` encoded XML string of this object and all its subelements

        """
        xml = self.get_xml()
        return etree.tostring(xml, encoding='utf-8')

    def get_xml(self):
        """ Get the XML representation as `ElementTree` object.

        :return: XML `ElementTree` of this object and all its subelements

        """
        xml = etree.Element(self.elementname)
        if self.debug:
            self.validator.check_all_svg_attribute_values(self.elementname, self.attribs)
        for attribute, value in self.attribs.iteritems():
            value = self.value_to_string(value)
            if value: # just add not empty attributes
                xml.set(attribute, value)

        for element in self.elements:
            xml.append(element.get_xml())
        return xml

    def value_to_string(self, value):
        """
        Converts *value* into a <string> includes a value check, depending
        on :attr:`self.debug` and :attr:`self.profile`.

        """
        if isinstance(value, (int, float)):
            if self.debug:
                self.validator.check_svg_type(value, 'number')
            if isinstance(value, float) and self.profile == 'tiny':
                value = round(value, 4)
        return unicode(value)
