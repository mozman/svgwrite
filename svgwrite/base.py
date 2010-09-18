#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
Common SVG Attributes
=====================

Core Attributes
---------------
`W3C Core Attributes`_

The core attributes are those attributes that can be specified on any SVG element.

id, xml:base, xml:lang, xml:space

Conditional Processing Attributes
---------------------------------
`W3C Conditional Processing Attributes`_

A conditional processing attribute is one that controls whether or not the element
on which it appears is processed. Most elements, but not all, may have conditional
processing attributes specified on them.

requiredExtensions, requiredFeatures, systemLanguage

Document Event Attributes
-------------------------
`W3C Document Event Attributes`_

A document event attribute is an event attribute that specifies script to run for
a particular document-wide event.

onabort, onerror, onresize, onscroll, onunload, onzoom

Graphical Event Attributes
--------------------------
`W3C Graphical Event Attributes`_

A graphical event attribute is an event attribute that specifies script to run for
a particular user interaction event.

onactivate, onclick, onfocusin, onfocusout, onload, onmousedown, onmousemove,
onmouseout, onmouseover, onmouseup

Presentation Attributes:
------------------------
`W3C Presentation Attributes`_

An XML attribute on an SVG element which specifies a value for a given property for that element.

alignment-baseline, baseline-shift, clip, clip-path, clip-rule, color, color-interpolation,
color-interpolation-filters, color-profile, color-rendering, cursor, direction,
display, dominant-baseline, enable-background, fill, fill-opacity, fill-rule, filter,
flood-color, flood-opacity, font-family, font-size, font-size-adjust, font-stretch,
font-style, font-variant, font-weight, glyph-orientation-horizontal, glyph-orientation-vertical,
image-rendering, kerning, letter-spacing, lighting-color, marker-end, marker-mid,
marker-start, mask, opacity, overflow, pointer-events, shape-rendering, stop-color,
stop-opacity, stroke, stroke-dasharray, stroke-dashoffset, stroke-linecap, stroke-linejoin,
stroke-miterlimit, stroke-opacity, stroke-width, text-anchor, text-decoration,
text-rendering, unicode-bidi, visibility, word-spacing, writing-mode

XLink Attributs:
----------------
`W3C XLink Attributes`_

The XLink attributes are the seven attributes defined in the XML Linking Language
specification XLINK_, which are used on various SVG elements that can reference resources.

xlink:href, xlink:show, xlink:actuate, xlink:type, xlink:role, xlink:arcrole,
xlink:title

.. _W3C Core Attributes: http://www.w3.org/TR/SVG11/intro.html#TermCoreAttribute
.. _W3C Conditional Processing Attributes: http://www.w3.org/TR/SVG11/intro.html#TermConditionalProcessingAttribute
.. _W3C Document Event Attributes: http://www.w3.org/TR/SVG11/intro.html#TermDocumentEventAttribute
.. _W3C Graphical Event Attributes: http://www.w3.org/TR/SVG11/intro.html#TermGraphicalEventAttribute
.. _W3C Presentation Attributes: http://www.w3.org/TR/SVG11/intro.html#TermPresentationAttribute
.. _W3C XLink Attributes: http://www.w3.org/TR/SVG11/intro.html#TermXLinkAttribute
.. _XLINK: http://www.w3.org/TR/SVG11/refs.html#ref-XLINK
"""

import xml.etree.ElementTree as etree

from svgwrite import parameter
from svgwrite.utils import value_to_string
from svgwrite.validator import check_attribute_names, check_attribute_value, \
     check_valid_content, check_coordinate

class BaseElement(object):
    """ The *BaseElement* class is the root for all svg-element classes.

    Attributes:
    -----------
    attribs -- <dict> svg attributes dictionary
    elements -- <list> list of containing svg-elements

    Methods:
    --------
    add(svg-element) -- add an svg-element
    tostring() -- get the xml-representation as <string> 'utf-8' encoded
    get_xml() -- get the xml-representation as ElementTree object


    set/get svg-attributes:
    -------------------------
    set attribute: svg-element['attribute'] = value
    get attribute: value = svg-element['attribute']
    """
    def __init__(self, attribs=None, **extra):
        """ Constructor

        Attributes:
        -----------
        attribs -- <dict> of svg-attributes
        **extra -- extra svg-attributs as keyword arguments, argument='value'

        Argument-names will be checked if parameter.debug_mode is True.
        """
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.attribs.update(extra)
        if parameter.debug_mode:
            check_attribute_names(self._elementname(), self.attribs)
        self.elements = list()

    def __getitem__(self, key):
        """ Get svg-attribute key """
        return self.attribs[key]

    def __setitem__(self, key, value):
        """ Set svg-attribute key=value """
        self.attribs[key] = value
        if parameter.debug_mode:
            check_attribute_names(self._elementname(), self.attribs)

    def add(self, element):
        """ Add an svg-element as subelement."""
        if parameter.debug_mode:
            check_valid_content(self._elementname(), element._elementname())
        self.elements.append(element)

    def tostring(self):
        """ Get the xml-representation as <string>, 'utf-8' encoded. """
        xml = self.get_xml()
        return etree.tostring(xml, encoding='utf-8')

    def get_xml(self):
        """ Get the xml-representation as ElementTree object. """
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
        """ Returns the svg-object name, defaults to the lowercase class name."""
        name = self.__class__.__name__
        return name[0].lower() + name[1:]

