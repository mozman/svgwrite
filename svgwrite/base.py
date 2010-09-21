#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
The :class:`BaseElement` is the root for all SVG elements.
"""

import xml.etree.ElementTree as etree

from svgwrite import parameter
from svgwrite.utils import value_to_string
from svgwrite.validator import check_attribute_names, check_attribute_value, \
     check_valid_content, check_coordinate

class BaseElement(object):
    """
    The :class:`BaseElement` is the root for all SVG elements. The SVG attributes
    are stored in :attr:`attribs`, and the SVG subelements are stored in
    :attr:`elements`.

    .. automethod:: svgwrite.base.BaseElement.__init__([attribs=None, **extra])


    **Attributes**

    .. attribute:: BaseElement.attribs

       `dict` of SVG attributes

    .. attribute:: BaseElement.elements

       `list` of SVG subelements

    **Methods**


    .. automethod:: svgwrite.base.BaseElement.add(element)

    .. automethod:: svgwrite.base.BaseElement.tostring()

    .. automethod:: svgwrite.base.BaseElement.get_xml()

    .. automethod:: svgwrite.base.BaseElement.__getitem__(key)

    .. automethod:: svgwrite.base.BaseElement.__setitem__(key, value)

    set/get SVG attributes::

        element['attribute'] = value
        value = element['attribute']

    .. seealso::
       :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    """
    elementname = 'baseElement'

    def __init__(self, attribs=None, **extra):
        """
        :param dict attribs: a dictinary of SVG attributes
        :param keyword-args extra: extra SVG attributes, argument='value'

        SVG attribute names will be checked, if :data:`~svgwrite.parameter.debug_mode` is `True`.
        """
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.attribs.update(extra)
        if parameter.debug_mode:
            check_attribute_names(self.elementname, self.attribs)
        self.elements = list()

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
        self.attribs[key] = value
        if parameter.debug_mode:
            check_attribute_names(self._elementname(), self.attribs)

    def add(self, element):
        """ Add an SVG element as subelement.

        :param element: append this SVG element

        """
        if parameter.debug_mode:
            check_valid_content(self.elementname, element.elementname)
        self.elements.append(element)

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
        debug_mode = parameter.debug_mode
        if debug_mode:
            check_attribute_names(self.elementname, self.attribs)
        xml = etree.Element(self.elementname)
        for attribute, value in self.attribs.iteritems():
            value = value_to_string(value)
            if debug_mode:
                check_attribute_value(attribute, value)
            if value: # just add not empty attributes
                xml.set(attribute, value)

        for element in self.elements:
            xml.append(element.get_xml())
        return xml

