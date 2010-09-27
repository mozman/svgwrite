#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 11.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
.. autoclass:: svgwrite.validator.FullProfileValidator

.. autoclass:: svgwrite.validator.TinyProfileValidator

"""
import re

from svgwrite import pattern

class FullProfileValidator(object):
    def __init__(self, debug=True):
        self.debug = debug

    def check_attribute_names(self, elementname, attribs):
        """Checks if all attribute-names (keys of attribs) for element 'elementname'
        are valid.

        Raises ValueError if not valid.
        """
        valid_attribs = attributes[elementname]
        for key in attribs.iterkeys():
            if key not in valid_attribs:
                raise ValueError("Invalid attribute '%s' for element '%s'." % (key, elementname))
        return attribs # pass-through function

    def check_attribute_value(self, attributename, value):
        """Checks if value is valid for attribute 'attribute-name'.

        Raises ValueError if not valid.
        """
        if not isinstance(value, basestring):
            value = unicode(value)
        if not validate_attribute[attributename](value):
            raise ValueError("Value '%s' is not valid for attribute '%s'." % (value, attributename))
        return value # pass-through function

    def check_valid_content(self, element, subelement):
        """ Check if element can contain subelement.

        Raises ValueError for invalid subelement.
        """
        valid_subelements = content_model[element]
        if '*' not in valid_subelements:
            if subelement not in valid_subelements:
                raise ValueError("Invalid content '%s' for element '%s'." % (subelement, element))
        return subelement

    def get_coordinate(self, value):
        """ Split value in (number, unit) if value has an unit or (number, None).

        Raises ValueError if not valid.
        """
        if value is None:
            raise TypeError("invalid type 'None'.")
        if isinstance(value, (int, float)):
            number, unit = float(value), None
        else:
            result = pattern.coordinate.match(value.strip())
            if result:
                number, tmp, unit = result.groups()
                number = float(number)
            else:
                raise ValueError("'%s' has not a valid svg coordinate." % value)
        return (number, unit)

    def get_angle(self, value):
        """ Split value in (number, unit) if value has an unit or (number, None).

        Raises ValueError if not valid.
        """
        if value is None:
            raise TypeError("invalid type 'None'.")
        if isinstance(value, (int, float)):
            number, unit = float(value), None
        else:
            result = pattern.angle.match(value.strip())
            if result:
                number, tmp, unit = result.groups()
                number = float(number)
            else:
                raise ValueError("'%s' has not a valid svg angle." % value)
        return (number, unit)

    def check_coordinate(self, value):
        """ Check if value is a valid coordinate, raises ValueError if not valid.
        """
        number, unit = self.get_coordinate(value)
        return value
    check_length = check_coordinate

    def check_angle(self, value):
        """ Check if value is a valid angle, raises ValueError if not valid.
        """
        number, unit = self.get_angle(value)
        return value

    def check_number(self, value):
        number = float(value) # ok if we get a float number
        return value

class TinyProfileValidator(FullProfileValidator):
    def check_tiny(self, number):
        """ Check if number is a valid 'tiny' number, raises ValueError
        if number is not valid.

        Raises ValueError if not valid.
        """
        if not (-32767.9999 <= number <= 32767.9999):
            raise ValueError("'%.4f' out of range for baseProfile 'tiny'" % number)
        return number # pass-through function

    def check_number(self, value):
        number = float(value)
        self.check_tiny(number)
        return value

    def get_angle(self, value):
        number, unit = (super(TinyProfileValidator, self).get_angle(value))
        number = self.check_tiny(round(number, 4)) # round to four places for tiny profile
        return (number, unit)

    def get_coordinate(self, value):
        number, unit = (super(TinyProfileValidator, self).get_coordinate(value))
        number = self.check_tiny(round(number, 4)) # round to four places for tiny profile
        return (number, unit)

################################################################################
## ELEMENT - ATTRIBUTES
################################################################################

core_attributes = ("id", "xml:base", "xml:lang", "xml:space")
conditional_processing_attributes = ("requiredFeatures", "requiredExtensions", "systemLanguage")
document_event_attributes = ("onunload", "onabort", "onerror", "onresize", "onscroll", "onzoom")
graphical_event_attributes = ("onfocusin", "onfocusout", "onactivate", "onclick",
                              "nmousedown", "onmouseup", "onmouseover", "onmousemove",
                              "onmouseout", "onload")
xlink_attributes = ("xlink:href", "xlink:show", "xlink:actuate", "xlink:type",
                    "xlink:role", "xlink:arcrole", "xlink:title")
presentation_attributes = ( "alignment-baseline", "baseline-shift", "clip", "clip-path",
                            "clip-rule", "color", "color-interpolation", "color-interpolation-filters",
                            "color-profile", "color-rendering", "cursor", "direction",
                            "display", "dominant-baseline", "enable-background",
                            "fill", "fill-opacity", "fill-rule", "filter", "flood-color",
                            "flood-opacity", "font-family", "font-size", "font-size-adjust",
                            "font-stretch", "font-style", "font-variant", "font-weight",
                            "glyph-orientation-horizontal", "glyph-orientation-vertical",
                            "image-rendering", "kerning", "letter-spacing", "lighting-color",
                            "marker-end", "marker-mid", "marker-start", "mask", "opacity",
                            "overflow", "pointer-events", "shape-rendering", "stop-color",
                            "stop-opacity", "stroke", "stroke-dasharray", "stroke-dashoffset",
                            "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
                            "stroke-opacity", "stroke-width", "text-anchor", "text-decoration",
                            "text-rendering", "unicode-bidi", "visibility", "word-spacing",
                            "writing-mode")
animation_event_attributes = ("onbegin", "onend", "onrepeat", "onload")
animation_attribute_target_attributes =("attributeType", "attributeName")
animation_timing_attributes = ("begin", "dur", "end", "min", "max", "restart", "repeatCount", "repeatDur", "fill")
animation_value_attributes = ("calcMode", "values", "keyTimes", "keySplines", "from", "to", "by")
animation_addition_attributes = ("additive", "accumulate")
filter_primitive_attributes = ("x", "y", "width", "height", "result")
transfer_function_element_attributes = ("type", "tableValues", "slope", "intercept",
                                        "amplitude", "exponent", "offset")
_attributes = {
    'a': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        xlink_attributes, ("class", "externalResourcesRequired", "style", "target", "transform", "xmlns:xlink")),
    'altGlyph': (conditional_processing_attributes, graphical_event_attributes,
        presentation_attributes, xlink_attributes, ("class", "dx", "dy", "externalResourcesRequired",
        "format", "glyphRef", "rotate", "style", "x", "xlink:href", "y")),
    'altGlyphDef': [],
    'altGlyphItem': [],
    'animate': (conditional_processing_attributes, animation_event_attributes, xlink_attributes,
        animation_attribute_target_attributes, animation_timing_attributes, animation_value_attributes,
        animation_addition_attributes, ("externalResourcesRequired",)),
    'animateColor': (conditional_processing_attributes, animation_event_attributes,
        xlink_attributes, animation_attribute_target_attributes, animation_timing_attributes,
        animation_value_attributes, animation_addition_attributes, ("externalResourcesRequired",)),
    'animateMotion': (conditional_processing_attributes, animation_event_attributes,
        xlink_attributes, animation_timing_attributes, animation_value_attributes,
        animation_addition_attributes, ("externalResourcesRequired", "keyPoints",
        "origin", "path", "rotate")),
    'animateTransform': (conditional_processing_attributes, animation_event_attributes,
        xlink_attributes, animation_attribute_target_attributes, animation_timing_attributes,
        animation_value_attributes, animation_addition_attributes, ("externalResourcesRequired",
        "type")),
    'circle': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "cx", "cy", "externalResourcesRequired", "r", "style", "transform")),
    'clipPath': (conditional_processing_attributes, presentation_attributes, ("class",
        "clipPathUnits", "externalResourcesRequired", "style", "transform")),
    'color-profile': (xlink_attributes, ("local", "name", "rendering-intent", "xlink:href")),
    'cursor': (conditional_processing_attributes, xlink_attributes, ("externalResourcesRequired",
        "x", "xlink:href", "y")),
    'defs': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "style", "transform")),
    'desc': (("class", "style"),),
    'ellipse': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "cx", "cy", "externalResourcesRequired", "rx", "ry", "style", "transform")),
    'feBlend': (presentation_attributes, filter_primitive_attributes, ("class",
        "style", "in", "in2", "mode")),
    'feColorMatrix': (presentation_attributes, filter_primitive_attributes, ("class",
        "style", "in", "type", "values")),
    'feComponentTransfer': (presentation_attributes, filter_primitive_attributes,("class", "style", "in")),
    'feComposite': (presentation_attributes, filter_primitive_attributes, ("class",
        "style", "in", "in2", "operator", "k1", "k2", "k3", "k4")),
    'feConvolveMatrix': (presentation_attributes, filter_primitive_attributes,
        ("class2", "style", "in", "bias", "divisor", "edgeMode", "kernelMatrix",
         "kernelUnitLength", "order", "preserveAlpha", "targetX", "targetY")),
    'feDiffuseLighting': (presentation_attributes, filter_primitive_attributes,
        ("class", "style", "in", "diffuseConstant", "kernelUnitLength", "surfaceScale")),
    'feDisplacementMap': (presentation_attributes, filter_primitive_attributes,
        ("class", "style", "in", "in2", "scale", "xChannelSelector", "yChannelSelector")),
    'feDistantLight': (("azimuth", "elevation"), ),
    'feFlood': (presentation_attributes, filter_primitive_attributes, ("class", "style")),
    'feFuncA': (transfer_function_element_attributes,),
    'feFuncB': (transfer_function_element_attributes,),
    'feFuncG': (transfer_function_element_attributes,),
    'feFuncR': (transfer_function_element_attributes,),
    'feGaussianBlur': (presentation_attributes, filter_primitive_attributes,
        ("class", "style", "in", "stdDeviation")),
    'feImage': (presentation_attributes, filter_primitive_attributes, xlink_attributes,
        ("class", "externalResourcesRequired", "style", "xlink:href", "preserveAsectRatio")),
    'feMerge': (presentation_attributes, filter_primitive_attributes, ("class", "style")),
    'feMergeNode': (("in",),),
    'feMorphology': (presentation_attributes, filter_primitive_attributes, ("class",
        "style", "in", "operator", "radius")),
    'feOffset': (presentation_attributes, filter_primitive_attributes, ("class",
        "style", "in", "dx", "dy")),
    'fePointLight': (("x", "y", "z"), ),
    'feSpecularLighting': (presentation_attributes, filter_primitive_attributes,
        ("class", "style", "in", "kernelUnitLength", "specularConstant", "specularExponent",
         "surfaceScale")),
    'feSpotLight': (("limitingConeAngle", "pointsAtX", "pointsAtY", "pointsAtZ",
        "specularExponent", "x", "y", "z"), ),
    'feTile': (presentation_attributes, filter_primitive_attributes, ("class", "style", "in")),
    'feTurbulence': (presentation_attributes, filter_primitive_attributes,
        ("baseFrequency", "numOctaves", "seed", "stitchTiles", "type")),
    'filter': (presentation_attributes, xlink_attributes, ("class", "externalResourcesRequired",
        "filterRes", "filterUnits", "height", "primitiveUnits", "style", "width",
        "x", "xlink:href", "y")),
    'font': (presentation_attributes, ("class", "externalResourcesRequired", "horiz-adv-x",
        "horiz-origin-x", "horiz-origin-y", "style", "vert-adv-y", "vert-origin-x",
        "vert-origin-y")),
    'font-face': (("accent-height", "alphabetic", "ascent", "bbox", "cap-height", "descent",
                  "font-family", "font-size", "font-stretch", "font-style", "font-variant",
                  "font-weight", "hanging", "ideographic", "mathematical", "overline-position",
                  "overline-thickness", "panose-1", "slope", "stemh", "stemv", "strikethrough-position",
                  "strikethrough-thickness", "underline-position", "underline-thickness", "unicode-range",
                  "units-per-em", "v-alphabetic", "v-hanging", "v-ideographic", "v-mathematical",
                  "widths", "x-height"),),
    'font-face-format': (("string",),),
    'font-face-name': (("name",),),
    'font-face-format': [],
    'font-face-uri': (xlink_attributes, ("xlink:href",)),
    'foreignObject': (conditional_processing_attributes, graphical_event_attributes,
        presentation_attributes,("class", "externalResourcesRequired", "height",
        "style", "transform", "width", "x", "y")),
    'g': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "style", "transform")),
    'glyph': (presentation_attributes, ("arabic-form", "class", "d", "glyph-name",
        "horiz-adv-x", "lang", "orientation", "style", "unicode", "vert-adv-y",
        "vert-origin-x", "vert-origin-y")),
    'glyphRef': (presentation_attributes, xlink_attributes, ("class", "dx", "dy",
        "format", "glyphRef", "style", "x", "xlink:href", "y")),
    'hkern': (("g1", "g2", "k", "u1", "u2"),),
    'image': (conditional_processing_attributes, graphical_event_attributes, xlink_attributes,
        presentation_attributes, ("class", "externalResourcesRequired", "height",
        "preserveAspectRatio", "style", "transform", "width", "x", "xlink:href", "y")),
    'line': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "style", "transform", "x1", "x2",
        "y1", "y2")),
    'linearGradient': (presentation_attributes, xlink_attributes, ("class", "externalResourcesRequired",
        "gradientTransform", "gradientUnits", "spreadMethod", "style", "x1", "x2",
        "xlink:href", "y1", "y2")),
    'marker': (presentation_attributes, ("class", "externalResourcesRequired", "markerHeight",
        "markerUnits", "markerWidth", "orient", "preserveAspectRatio", "refX", "refY",
        "style", "viewBox")),
    'mask': (conditional_processing_attributes, presentation_attributes, ("class",
        "externalResourcesRequired", "height", "maskContentUnits", "maskUnits",
        "style", "width", "x", "y")),
    'metadata': [],
    'missing-glyph': (presentation_attributes, ("class", "d", "horiz-adv-x", "style",
        "vert-adv-y", "vert-origin-x", "vert-origin-y")),
    'mpath': (xlink_attributes, ("externalResourcesRequired", "xlink:href")),
    'path': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "d", "externalResourcesRequired", "pathLength", "style", "transform")),
    'pattern': (conditional_processing_attributes, presentation_attributes, xlink_attributes,
        ("class", "externalResourcesRequired", "height", "patternContentUnits",
         "patternTransform", "patternUnits", "preserveAspectRatio", "style", "viewBox",
         "width", "x", "xlink:href", "y")),
    'polygon': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "points", "style", "transform")),
    'polyline': (conditional_processing_attributes, graphical_event_attributes,
        presentation_attributes, ("class", "externalResourcesRequired", "points",
        "style", "transform")),
    'radialGradient': (presentation_attributes, xlink_attributes, ("class", "cx",
        "cy", "externalResourcesRequired", "fx", "fy", "gradientTransform", "gradientUnits",
        "r", "spreadMethod", "style", "xlink:href")),
    'rect': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "height", "rx", "ry", "style", "transform",
         "width", "x", "y")),
    'script': (xlink_attributes, ("externalResourcesRequired", "type", "xlink:href")),
    'set': (conditional_processing_attributes, animation_event_attributes, xlink_attributes,
        animation_attribute_target_attributes, animation_timing_attributes, ("externalResourcesRequired", "to")),
    'stop': (presentation_attributes, ("class", "offset", "style")),
    'style': (("media", "title", "type"), ),
    'svg' : (conditional_processing_attributes, document_event_attributes, graphical_event_attributes,
        presentation_attributes, ("baseProfile", "class", "contentScriptType", "contentStyleType",
        "externalResourcesRequired", "height", "preserveAspectRatio", "style", "version",
        "viewBox", "width", "x", "xmlns", "xmlns:xlink", "y", "zoomAndPan")),
    'switch': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "externalResourcesRequired", "style", "transform")),
    'symbol': (graphical_event_attributes, presentation_attributes, ("class",
        "externalResourcesRequired", "preserveAspectRatio", "style", "viewBox")),
    'text': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "dx", "dy", "externalResourcesRequired", "lengthAdjust", "rotate",
        "style", "textLength", "transform", "x", "y")),
    'textPath': (conditional_processing_attributes, graphical_event_attributes,
        presentation_attributes, xlink_attributes, ("class", "externalResourcesRequired",
        "lengthAdjust", "method", "spacing", "startOffset", "style", "textLength", "xlink:href")),
    'title': (("class", "style"), ),
    'tref': (conditional_processing_attributes, core_attributes, graphical_event_attributes,
        presentation_attributes, xlink_attributes,("class", "dx", "dy", "externalResourcesRequired",
        "lengthAdjust", "rotate", "style", "textLength", "x", "xlink:href", "y")),
    'tspan': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
        ("class", "dx", "dy", "externalResourcesRequired", "lengthAdjust", "rotate",
        "style", "textLength", "x", "y")),
    'use': (conditional_processing_attributes, graphical_event_attributes, presentation_attributes,
            xlink_attributes, ("class", "externalResourcesRequired", "height", "style",
            "transform", "width", "x", "xlink:href", "y")),
    'view': (("externalResourcesRequired", "preserveAspectRatio", "viewBox", "viewTarget",
             "zoomAndPan"),),
    'vkern': (("g1", "g2", "k", "u1", "u2"),),
}

def flatten_attributes():
    attributes = {}
    for element, attrib_lists in _attributes.iteritems():
        collect = set(core_attributes)
        for attribs in attrib_lists:
            collect.update(attribs)
        attributes[element] = frozenset(collect)
    return attributes
# attibutes -- <dict> contains for every svg-element ALL valid attributs
attributes = flatten_attributes()

################################################################################
## ATTRIBUTE VALIDATION FUNCTIONS
################################################################################

def _always_valid(value):
    return True

def _valid_angle(value):
    return pattern.angle.match(value) is not None
def _valid_coordinate(value):
    return pattern.coordinate.match(value) is not None
def _valid_number(value):
    return pattern.number.match(value) is not None

validate_attribute = {
    'accent-height' : _always_valid,
    'accumulate' : _always_valid,
    'additive' : _always_valid,
    'alignment-baseline' : _always_valid,
    'alphabetic' : _always_valid,
    'amplitude' : _always_valid,
    'arabic-form' : _always_valid,
    'ascent' : _always_valid,
    'attributeName' : _always_valid,
    'attributeType' : _always_valid,
    'azimuth' : _always_valid,
    'baseFrequency' : _always_valid,
    'baseProfile' : _always_valid,
    'baseline-shift' : _always_valid,
    'bbox' : _always_valid,
    'begin' : _always_valid,
    'bias' : _always_valid,
    'by' : _always_valid,
    'calcMode' : _always_valid,
    'cap-height' : _always_valid,
    'class' : _always_valid,
    'class2' : _always_valid,
    'clip' : _always_valid,
    'clip-path' : _always_valid,
    'clip-rule' : _always_valid,
    'clipPathUnits' : _always_valid,
    'color' : _always_valid,
    'color-interpolation' : _always_valid,
    'color-interpolation-filters' : _always_valid,
    'color-profile' : _always_valid,
    'color-rendering' : _always_valid,
    'contentScriptType' : _always_valid,
    'contentStyleType' : _always_valid,
    'cursor' : _always_valid,
    'cx' : _valid_coordinate,
    'cy' : _valid_coordinate,
    'd' : _always_valid,
    'descent' : _always_valid,
    'diffuseConstant' : _always_valid,
    'direction' : _always_valid,
    'display' : _always_valid,
    'divisor' : _always_valid,
    'dominant-baseline' : _always_valid,
    'dur' : _always_valid,
    'dx' : _valid_coordinate,
    'dy' : _valid_coordinate,
    'edgeMode' : _always_valid,
    'elevation' : _always_valid,
    'enable-background' : _always_valid,
    'end' : _always_valid,
    'exponent' : _always_valid,
    'externalResourcesRequired' : _always_valid,
    'fill' : _always_valid,
    'fill-opacity' : _always_valid,
    'fill-rule' : _always_valid,
    'filter' : _always_valid,
    'filterRes' : _always_valid,
    'filterUnits' : _always_valid,
    'flood-color' : _always_valid,
    'flood-opacity' : _always_valid,
    'font-family' : _always_valid,
    'font-size' : _always_valid,
    'font-size-adjust' : _always_valid,
    'font-stretch' : _always_valid,
    'font-style' : _always_valid,
    'font-variant' : _always_valid,
    'font-weight' : _always_valid,
    'format' : _always_valid,
    'from' : _always_valid,
    'fx' : _always_valid,
    'fy' : _always_valid,
    'g1' : _always_valid,
    'g2' : _always_valid,
    'glyph-name' : _always_valid,
    'glyph-orientation-horizontal' : _always_valid,
    'glyph-orientation-vertical' : _always_valid,
    'glyphRef' : _always_valid,
    'gradientTransform' : _always_valid,
    'gradientUnits' : _always_valid,
    'hanging' : _always_valid,
    'height' : _valid_coordinate,
    'horiz-adv-x' : _always_valid,
    'horiz-origin-x' : _always_valid,
    'horiz-origin-y' : _always_valid,
    'id' : _always_valid,
    'ideographic' : _always_valid,
    'image-rendering' : _always_valid,
    'in' : _always_valid,
    'in2' : _always_valid,
    'intercept' : _always_valid,
    'k' : _always_valid,
    'k1' : _always_valid,
    'k2' : _always_valid,
    'k3' : _always_valid,
    'k4' : _always_valid,
    'kernelMatrix' : _always_valid,
    'kernelUnitLength' : _always_valid,
    'kerning' : _always_valid,
    'keyPoints' : _always_valid,
    'keySplines' : _always_valid,
    'keyTimes' : _always_valid,
    'lang' : _always_valid,
    'lengthAdjust' : _always_valid,
    'letter-spacing' : _always_valid,
    'lighting-color' : _always_valid,
    'limitingConeAngle' : _always_valid,
    'local' : _always_valid,
    'marker-end' : _always_valid,
    'marker-mid' : _always_valid,
    'marker-start' : _always_valid,
    'markerHeight' : _always_valid,
    'markerUnits' : _always_valid,
    'markerWidth' : _always_valid,
    'mask' : _always_valid,
    'maskContentUnits' : _always_valid,
    'maskUnits' : _always_valid,
    'mathematical' : _always_valid,
    'max' : _always_valid,
    'media' : _always_valid,
    'method' : _always_valid,
    'min' : _always_valid,
    'mode' : _always_valid,
    'name' : _always_valid,
    'nmousedown' : _always_valid,
    'numOctaves' : _always_valid,
    'offset' : _always_valid,
    'onabort' : _always_valid,
    'onactivate' : _always_valid,
    'onbegin' : _always_valid,
    'onclick' : _always_valid,
    'onend' : _always_valid,
    'onerror' : _always_valid,
    'onfocusin' : _always_valid,
    'onfocusout' : _always_valid,
    'onload' : _always_valid,
    'onmousemove' : _always_valid,
    'onmouseout' : _always_valid,
    'onmouseover' : _always_valid,
    'onmouseup' : _always_valid,
    'onrepeat' : _always_valid,
    'onresize' : _always_valid,
    'onscroll' : _always_valid,
    'onunload' : _always_valid,
    'onzoom' : _always_valid,
    'opacity' : _always_valid,
    'operator' : _always_valid,
    'order' : _always_valid,
    'orient' : _always_valid,
    'orientation' : _always_valid,
    'origin' : _always_valid,
    'overflow' : _always_valid,
    'overline-position' : _always_valid,
    'overline-thickness' : _always_valid,
    'panose-1' : _always_valid,
    'path' : _always_valid,
    'pathLength' : _always_valid,
    'patternContentUnits' : _always_valid,
    'patternTransform' : _always_valid,
    'patternUnits' : _always_valid,
    'pointer-events' : _always_valid,
    'points' : _always_valid,
    'pointsAtX' : _always_valid,
    'pointsAtY' : _always_valid,
    'pointsAtZ' : _always_valid,
    'preserveAlpha' : _always_valid,
    'preserveAsectRatio' : _always_valid,
    'preserveAspectRatio' : _always_valid,
    'primitiveUnits' : _always_valid,
    'r' : _valid_coordinate,
    'radius' : _valid_coordinate,
    'refX' : _always_valid,
    'refY' : _always_valid,
    'rendering-intent' : _always_valid,
    'repeatCount' : _always_valid,
    'repeatDur' : _always_valid,
    'requiredExtensions' : _always_valid,
    'requiredFeatures' : _always_valid,
    'restart' : _always_valid,
    'result' : _always_valid,
    'rotate' : _valid_angle,
    'rx' : _valid_coordinate,
    'ry' : _valid_coordinate,
    'scale' : _always_valid,
    'seed' : _always_valid,
    'shape-rendering' : _always_valid,
    'slope' : _always_valid,
    'spacing' : _always_valid,
    'specularConstant' : _always_valid,
    'specularExponent' : _always_valid,
    'spreadMethod' : _always_valid,
    'startOffset' : _always_valid,
    'stdDeviation' : _always_valid,
    'stemh' : _always_valid,
    'stemv' : _always_valid,
    'stitchTiles' : _always_valid,
    'stop-color' : _always_valid,
    'stop-opacity' : _always_valid,
    'strikethrough-position' : _always_valid,
    'strikethrough-thickness' : _always_valid,
    'stroke' : _always_valid,
    'stroke-dasharray' : _always_valid,
    'stroke-dashoffset' : _always_valid,
    'stroke-linecap' : _always_valid,
    'stroke-linejoin' : _always_valid,
    'stroke-miterlimit' : _always_valid,
    'stroke-opacity' : _always_valid,
    'stroke-width' : _always_valid,
    'style' : _always_valid,
    'surfaceScale' : _always_valid,
    'systemLanguage' : _always_valid,
    'tableValues' : _always_valid,
    'target' : _always_valid,
    'targetX' : _always_valid,
    'targetY' : _always_valid,
    'text-anchor' : _always_valid,
    'text-decoration' : _always_valid,
    'text-rendering' : _always_valid,
    'textLength' : _always_valid,
    'title' : _always_valid,
    'to' : _always_valid,
    'transform' : _always_valid,
    'type' : _always_valid,
    'u1' : _always_valid,
    'u2' : _always_valid,
    'underline-position' : _always_valid,
    'underline-thickness' : _always_valid,
    'unicode' : _always_valid,
    'unicode-bidi' : _always_valid,
    'unicode-range' : _always_valid,
    'units-per-em' : _always_valid,
    'v-alphabetic' : _always_valid,
    'v-hanging' : _always_valid,
    'v-ideographic' : _always_valid,
    'v-mathematical' : _always_valid,
    'values' : _always_valid,
    'version' : _always_valid,
    'vert-adv-y' : _always_valid,
    'vert-origin-x' : _always_valid,
    'vert-origin-y' : _always_valid,
    'viewBox' : _always_valid,
    'viewTarget' : _always_valid,
    'visibility' : _always_valid,
    'width' : _valid_coordinate,
    'widths' : _always_valid,
    'word-spacing' : _always_valid,
    'writing-mode' : _always_valid,
    'x' : _valid_coordinate,
    'x-height' : _always_valid,
    'x1' : _valid_coordinate,
    'x2' : _valid_coordinate,
    'xChannelSelector' : _always_valid,
    'xlink:actuate' : _always_valid,
    'xlink:arcrole' : _always_valid,
    'xlink:href' : _always_valid,
    'xlink:role' : _always_valid,
    'xlink:show' : _always_valid,
    'xlink:title' : _always_valid,
    'xlink:type' : _always_valid,
    'xml:base' : _always_valid,
    'xml:lang' : _always_valid,
    'xml:space' : _always_valid,
    'xmlns' : _always_valid,
    'xmlns:xlink' : _always_valid,
    'y' : _valid_coordinate,
    'y1' : _valid_coordinate,
    'y2' : _valid_coordinate,
    'yChannelSelector' : _always_valid,
    'z' : _always_valid,
    'zoomAndPan' : _always_valid,
}

################################################################################
## CONTENT MODEL
################################################################################

animation_elements = ("animate", "animateColor", "animateMotion", "animateTransform", "set")
descriptive_elements = ("desc", "metadata", "title")
shape_elements = ("circle", "ellipse", "line", "path", "polygon", "polyline", "rect")
structural_elements = ("defs", "g", "svg", "symbol", "use")
gradient_elements = ("linearGradient", "radialGradient")
filter_primitive_elements = ("feBlend", "feColorMatrix", "feComponentTransfer", "feComposite",
                             "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feFlood",
                             "feGaussianBlur", "feImage", "feMerge", "feMorphology", "feOffset",
                             "feSpecularLighting", "feTile", "feTurbulence")
text_content_child_elements = ("altGlyph", "textPath", "tref", "tspan")
any_elements = ("*", )

_content_model = {
'a' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'altGlyp' : (any_elements, ),
'altGlyphDef' : (any_elements, ),
'altGlyphItem' : (any_elements, ),
'animate' : (descriptive_elements,),
'animateColor' : (descriptive_elements,),
'animateMotion' : (descriptive_elements, ('mpath',)),
'animateTransform' : (descriptive_elements, ),
'circle' : (descriptive_elements, animation_elements),
'clipPath' : (descriptive_elements, animation_elements, shape_elements, ('text', 'use')),
'color-profile' : (descriptive_elements, ),
'cursor' : (descriptive_elements, ),
'defs' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'desc' : (any_elements, ),
'ellipse' : (animation_elements, descriptive_elements),
'feBlend' : (('animate', 'set'), ),
'feColorMatrix' : (('animate', 'set'), ),
'feComponentTransfer' : (('feFuncA', 'feFuncR', 'feFuncG', 'feFuncB'), ),
'feComposite' : (('animate', 'set'), ),
'feConvolveMatrix' : (('animate', 'set'), ),
'feDiffuseLighting' : (descriptive_elements, ('feDistantLight', 'fePointLight', 'feSpotLight')),
'feDisplacementMap' : (('animate', 'set'), ),
'feDistantLight' : (('animate', 'set'), ),
'feFlood' : (('animate', 'animateColor', 'set'), ),
'feFuncA' : (('animate', 'set'), ),
'feFuncR' : (('animate', 'set'), ),
'feFuncG' : (('animate', 'set'), ),
'feFuncB' : (('animate', 'set'), ),
'feGaussianBlur' : (('animate', 'set'), ),
'feImage' : (('animate', 'animateColor', 'set'), ),
'feMerge' : (('animate', 'set'), ),
'feMergeNode' : (('animate', 'set'), ),
'feMorphology' : (('animate', 'set'), ),
'feOffset' : (('animate', 'set'), ),
'fePointLight' : (('animate', 'set'), ),
'feSpecularLighting' : (descriptive_elements, ('feDistantLight', 'fePointLight', 'feSpotLight')),
'feSpotLight' : (('animate', 'set'), ),
'feTile' : (('animate', 'set'), ),
'feTurbolence' : (('animate', 'set'), ),
'filter' : (descriptive_elements, filter_primitive_attributes, ('animate', 'set')),
'font' : (descriptive_elements, ("font-face", "glyph", "hkern", "missing-glyph", "vkern")),
'font-face' : (descriptive_elements, ('font-face-src', )),
'font-face-format': [],
'font-face-name': [],
'font-face-src': (('font-face-name', 'font-face-uri'), ),
'font-face-uri': (('font-face-format', ), ),
'foreignObject': (any_elements, ),
'g' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'glyph' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'glyphRef' : [],
'hkern' : [],
'image' : (animation_elements, descriptive_elements),
'line' : (animation_elements, descriptive_elements),
'linearGradient' : (descriptive_elements, ("animate", "animateTransform", "set", "stop")),
'marker' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'mask' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'metadata' : (any_elements, ),
'missing-glyph' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'mpath' : (descriptive_elements, ),
'path' : (animation_elements, descriptive_elements),
'pattern': (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'polygon' : (animation_elements, descriptive_elements),
'polyline' : (animation_elements, descriptive_elements),
'radialGradient': (descriptive_elements, ("animate", "animateTransform", "set", "stop")),
'rect' : (descriptive_elements, animation_elements),
'scripte' : (any_elements, ),
'set' : (descriptive_elements, ),
'stop' : (('animate', 'animateColor', 'set'), ),
'style' : (any_elements, ),
'svg' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'switch' : (animation_elements, descriptive_elements, shape_elements, ("a", "foreignObject",
    "g", "image", "svg", "switch", "text", "use")),
'symbol' : (animation_elements, descriptive_elements, shape_elements, structural_elements, gradient_elements,
    ("a", "altGlyphDef", "clipPath", "color-profile", "cursor", "filter", "font", "font-face",
     "foreignObject", "image", "marker", "mask", "pattern", "script", "style", "switch","text", "view")),
'text' : (animation_elements, descriptive_elements, text_content_child_elements, ('a',)),
'textPath' : (descriptive_elements, ("a", "altGlyph", "animate", "animateColor", "set", "tref", "tspan")),
'title' : (any_elements, ),
'tref' : (descriptive_elements, ('animate', 'animateColor', 'set')),
'tspan' : (descriptive_elements, ("a", "altGlyph", "animate", "animateColor", "set", "tref", "tspan")),
'use' : (animation_elements, descriptive_elements),
'view' : (descriptive_elements, ),
'vkern' : [],
}

def flatten_content_model():
    content_model = {}
    for element, element_lists in _content_model.iteritems():
        collect = set()
        for elements in element_lists:
            collect.update(elements)
        content_model[element] = frozenset(collect)
    return content_model
# attibutes -- <dict> contains for every svg-element ALL valid attributs
content_model = flatten_content_model()
