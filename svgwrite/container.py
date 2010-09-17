#coding:utf-8
# Author:  mozman
# Purpose: svg container classes
# Created: 15.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import parameter

from base import BaseElement
from interface import IViewBox, ITransform
from validator import check_coordinate


class Group(BaseElement, ITransform):
    """ The <g /> element.

    methods:
    --------
    group(**attributes) -- create a new group element with attributes

    Supported Interfaces:
    ---------------------
    ITransform: translate, rotate, scale, skewX, skewY, matrix, rev, del_transform
    """
    def _elementname(self):
        return 'g'

    def group(self, **attributes):
        """ Create a new group with attributs."""
        g = Group(**attributes)
        self.add(g)
        return g

class Defs(Group):
    """ The <defs /> element> see Group class."""
    def _elementname(self):
        return 'defs'

class Symbol(BaseElement, IViewBox):
    """ The <symbol /> element.
    methods:
    --------
    group(**attributes) -- create a new group element with attributes

    Supported Interfaces:
    ---------------------
    IViewBox: viewboy, strech, fit
    """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    def _elementname(self):
        return 'symbol'

    def group(self, **attributes):
        g = Group(**attributes)
        self.add(g)
        return g

class SVG(Symbol):
    """The <svg /> element.

    Attributes:
    -----------
    defs -- <Defs> container for referenced elements
        you got direct access: defs.add( svg-class )

    Supported Interfaces:
    ---------------------
    IViewBox: viewbox, stretch, fit

    Supported SVG Attributes:
    -------------------------
    set attribute: drawing-object['attribute'] = value or on __init__()
    get attribute: value = drawing-object['attribute']

    class -- <string> assigns one or more css-class-names to an element
        see http://www.w3.org/TR/SVG11/interact.html#ClassAttribute
    style -- <string> allows per-element css-style rules to be specified directly
        on a given element
        see http://www.w3.org/TR/SVG11/interact.html#StyleAttribute
    x -- <coordinate> x-coordinate, if <svg> is enbedded into another <svg>-element
    y -- <coordinate> y-coordinate, if <svg> is enbedded into another <svg>-element
    width -- <length> canvas-width - default is '100%'
    height -- <length> canvas-height - default is '100%'
    viewBox -- use IViewBox interface
    preserveAspectRatio -- use IViewBox interface
    zoomAndPan -- "disable|magnify" : default is 'magnify'
        see http://www.w3.org/TR/SVG11/interact.html#ZoomAndPanAttribute
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true
        see http://www.w3.org/TR/SVG11/interact.html#ExternalResourcesRequiredAttribute

    supported but do not set or change following svg-attributes:
    version, baseProfile, contentScriptType, contentStyleType
    """
    def __init__(self, insert=None, size=None, attribs=None, **extra):
        """ Constructor

        Arguments:
        ----------
        insert -- <2-tuple> insert position
        size -- <2-tuple> width, height
        attribs -- <dict> additional attributes as dict
        **extra -- additional attributs
        """
        super(SVG, self).__init__(attribs=attribs, **extra)
        debug = parameter.debug_mode
        profile = parameter.profile
        if insert:
            if debug:
                check_coordinate(insert[0], profile)
                check_coordinate(insert[1], profile)
            self.attribs['x'] = insert[0]
            self.attribs['y'] = insert[1]
        if size:
            if debug:
                check_coordinate(size[0], profile)
                check_coordinate(size[1], profile)
            self.attribs['width'] = size[0]
            self.attribs['height'] = size[1]

        self.defs = Defs() # defs container
        self.add(self.defs) # add defs as first element

    def _elementname(self):
        return 'svg'

class Use(BaseElement, ITransform):
    """ The <use /> element.

    Re-use basic-shapes, groups, symbols or svg elements. Link to objects by
    href='#object-id' or use the object itself as href-argument - has to have
    an 'id'-attribute.

    Supported Interfaces:
    ---------------------
    ITransform: translate, rotate, scale, skewX, skewY, matrix, rev, del_transform
    """
    def __init__(self, href, insert=None, size=None, attribs=None, **extra):
        """ Constructor

        Arguments:
        ----------
        href -- object link <string> (link to id) or an object with an id-attribute
        insert -- <2-tuple> insert point (x,y)
        size -- <2-tuple> (width, height)
        attribs -- <dict> additional attributes as dict
        **extra -- additional attributs
        """
        super(Use, self).__init__(attribs, **extra)
        if isinstance(href, BaseElement):
            try:
                href = "#%s" % href['id']
            except KeyError:
                raise KeyError("<href> should have an id attribute or has to be a <string>.")
        debug = parameter.debug_mode
        profile = parameter.profile
        self.attribs['xlink:href'] = href
        if insert:
            if debug:
                check_coordinate(insert[0], profile)
                check_coordinate(insert[1], profile)
            self.attribs['x'] = insert[0]
            self.attribs['y'] = insert[1]
        if size:
            if debug:
                check_coordinate(size[0], profile)
                check_coordinate(size[1], profile)
            self.attribs['width'] = size[0]
            self.attribs['height'] = size[1]
