#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: drawing
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite import parameter
from svgwrite.validator import check_coordinate
from svgwrite.base import BaseElement

class Drawing(BaseElement):
    """This is the svg-drawing represented by the <svg /> element.

    A drawing consists of any number of SVG elements contained within the drawing
    element, stored in the element-attribute.

    A drawing can range from an empty drawing (i.e., no content inside of the drawing),
    to a very simple drawing containing a single svg-element such as a <rect>,
    to a complex, deeply nested collection of container elements and graphics elements.

    Attributes:
    -----------
    filename -- should be supported by the open-command

    inherited attributes see class: BaseElement

    Methods:
    --------
    viewbox(minx, miny, width, height) -- set the viewBox attribute
    write(fileobj) -- write xml-string to fileobject, 'utf-8'-encoding
    save() -- store xml-string to the filesystem (uses filename-attribute)
    saveas(filename) -- store xml-string to 'filename' resource

    inherited methods see class: BaseElement

    Supported SVG Attributes:
    -------------------------
    set attribute: drawing-object['attribute'] = value or on __init__()
    get attribute: value = drawing-object['attribute']

    class -- <string> : assigns one or more css-class-names to an element
    style -- <string> : allows per-element css-style rules to be specified directly
        on a given element
    x -- <coordinate> : x-coordinate, if <svg> is enbedded into another <svg>-element
    y -- <coordinate> : y-coordinate, if <svg> is enbedded into another <svg>-element
    width -- <coordinate> : canvas-width - default is '100%'
    height -- <coordinate> : canvas-height - default is '100%'
    viewBox -- <string> : a list of four numbers '<min-x>, <min-y>, <width> and <height>'
        better: use the viewbox-method
    preserveAspectRatio -- <string> : "[defer] <align>  [meet|slice]" influence graphic scaling
        see http://www.w3.org/TR/SVG11/coords.html#PreserveAspectRatioAttribute
    zoomAndPan -- "disable|magnify" : default is 'magnify'
        see http://www.w3.org/TR/SVG11/interact.html#ZoomAndPanAttribute
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true

    supported but do not set or change following svg-attributes:
    version, baseProfile, contentScriptType, contentStyleType
    """
    def __init__(self, filename="noname.svg", width='100%', height='100%', **extra):
        """Constructor for class Drawing
        Arguments:
        ----------
        filename -- filesystem-filename, should be supported by the open-command
        width -- float|int|string : canvas-width - default is '100%'
        height -- float|int|string : canvas-height - default is '100%'
        extra -- keyword arguments - any valid (for the <svg> element) svg-attributes
        """
        super(Drawing, self).__init__(xmlns="http://www.w3.org/2000/svg",
                                      width=width, height=height, **extra)
        self.filename = filename

    def get_xml(self):
        """ Get the ElementTree object.
        """
        profile = parameter.profile
        if profile == 'tiny':
            version = '1.2' # only tiny
        else:
            version = '1.1' # basic or full
        self.attribs['baseProfile'] = profile
        self.attribs['version'] = version
        return super(Drawing, self).get_xml()

    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Set the svg 'viewBox' attribute, argument are <coordinate> values.
        """
        for value in (minx, miny, width, height):
            check_coordinate(value)
        self.attribs['viewBox'] = "%s,%s,%s,%s" % (minx, miny, width, height)

    def _elementname(self):
        return 'svg'

    def write(self, fileobj):
        """Write the xml-string to 'fileobj' encoded as 'utf-8'-string."""
        xmlstr = self.tostring()
        fileobj.write(xmlstr)

    def save(self):
        """Write the xml-string to the 'self.filename' resource."""
        fileobj = open(self.filename, mode='w')
        self.write(fileobj)
        fileobj.close

    def saveas(self, filename):
        """Write the xml-string to the 'filename' resource."""
        self.filename = filename
        self.save()