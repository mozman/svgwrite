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
    """ The *g* element is a container element for grouping together related graphics elements.

    Methods:
    --------
    group(**attributes) -- create a new group element with attributes

    Inherited Attributes:
    ---------------------
    attribs -- <dict> svg attributes dictionary
    elements -- <list> list of containing svg-elements

    Inherited Methods:
    ------------------
    add(svg-element) -- add an svg-element
    tostring() -- get the xml-representation as <string> 'utf-8' encoded
    get_xml() -- get the xml-representation as ElementTree object

    Supported Interfaces:
    ---------------------
    ITransform: translate, rotate, scale, skewX, skewY, matrix, rev, del_transform

    Supported svg-attributes:
    -------------------------
    class -- <string> assigns one or more css-class-names to an element
    style -- <string> allows per-element css-style rules to be specified directly on a given element
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true
    transform -- use ITransform interface

    Standard SVG Attributes:
    ------------------------
    see description in  **base.py**

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    def _elementname(self):
        return 'g'

    def group(self, **attributes):
        """ Create a new group with attributs."""
        g = Group(**attributes)
        self.add(g)
        return g

class Defs(Group):
    """ The *defs* element is a container element for referenced elements. For
    understandability and accessibility reasons, it is recommended that, whenever
    possible, referenced elements be defined inside of a *defs*.
    """
    def _elementname(self):
        return 'defs'

class Symbol(BaseElement, IViewBox):
    """ The *symbol* element is used to define graphical template objects which
    can be instantiated by a *use* element. The use of *symbol* elements for
    graphics that are used multiple times in the same document adds structure and
    semantics. Documents that are rich in structure may be rendered graphically,
    as speech, or as braille, and thus promote accessibility.

    methods:
    --------
    group(**attributes) -- create a new group element with attributes

    Inherited Attributes:
    ---------------------
    attribs -- <dict> svg attributes dictionary
    elements -- <list> list of containing svg-elements

    Inherited Methods:
    ------------------
    add(svg-element) -- add an svg-element
    tostring() -- get the xml-representation as <string> 'utf-8' encoded
    get_xml() -- get the xml-representation as ElementTree object

    Supported Interfaces:
    ---------------------
    IViewBox: viewboy, strech, fit

    Supported svg-attributes:
    -------------------------
    class -- <string> assigns one or more css-class-names to an element
    style -- <string> allows per-element css-style rules to be specified directly on a given element
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true
    viewBox -- use IViewBox interface
    preserveAspectRatio -- use IViewBox interface

    Standard SVG Attributes:
    ------------------------
    see description in  **base.py**

    * Core Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    def _elementname(self):
        return 'symbol'

    def group(self, **attributes):
        """ Create a new group with attributs. """
        g = Group(**attributes)
        self.add(g)
        return g

class SVG(Symbol):
    """ An SVG document fragment consists of any number of SVG elements contained
    within an *svg* element.

    An SVG document fragment can range from an empty fragment (i.e., no content
    inside of the *svg* element), to a very simple SVG document fragment containing
    a single SVG graphics element such as a *rect*, to a complex, deeply nested
    collection of container elements and graphics elements.

    Attributes:
    -----------
    defs -- <Defs> container for referenced elements
        you got direct access: defs.add( svg-class )

    Supported Interfaces:
    ---------------------
    IViewBox: viewbox, stretch, fit

    Supported svg-attributes:
    -------------------------
    class -- <string> assigns one or more css-class-names to an element
    style -- <string> allows per-element css-style rules to be specified directly on a given element
    x -- <coordinate> x-coordinate, if <svg> is enbedded into another <svg>-element
    y -- <coordinate> y-coordinate, if <svg> is enbedded into another <svg>-element
    width -- <length> canvas-width - default is '100%'
    height -- <length> canvas-height - default is '100%'
    viewBox -- use IViewBox interface
    preserveAspectRatio -- use IViewBox interface
    zoomAndPan -- "disable|magnify" : default is 'magnify'
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true

    supported but do not set or change following svg-attributes:
    version, baseProfile, contentScriptType, contentStyleType

    Standard SVG Attributes:
    ------------------------
    see description in  **base.py**

    * Core Attributes
    * Conditional Processing Attributes
    * Document Event Attributes
    * Graphical Event Attributes
    * Presentation Attributes
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
    """ The *use* element references another element and indicates that the graphical
    contents of that element is included/drawn at that given point in the document.

    Link to objects by href='#object-id' or use the object itself as href-argument,
    the object has to have an 'id'-attribute.

    Inherited Attributes:
    ---------------------
    attribs -- <dict> svg attributes dictionary
    elements -- <list> list of containing svg-elements

    Inherited Methods:
    ------------------
    add(svg-element) -- add an svg-element
    tostring() -- get the xml-representation as <string> 'utf-8' encoded
    get_xml() -- get the xml-representation as ElementTree object

    Supported Interfaces:
    ---------------------
    ITransform: translate, rotate, scale, skewX, skewY, matrix, rev, del_transform

    Supported svg-attributes:
    -------------------------
    class -- <string> assigns one or more css-class-names to an element
    style -- <string> allows per-element css-style rules to be specified directly on a given element
    x -- <coordinate> insert x-coordinate, set on __init__(insert)
    y -- <coordinate> insert y-coordinate, set on __init__(insert)
    width -- <length> width - default is '100%', set on __init__(size)
    height -- <length> height - default is '100%', set on __init__(size)
    transform -- use ITransform interface
    xlink:href -- , set on __init__(href)
    externalResourcesRequired -- "true|false" false: if document rendering can proceed
        even if external resources are unavailable else: true

    Standard SVG Attributes:
    ------------------------
    see description in **base.py**

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    * XLink Attributes
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
