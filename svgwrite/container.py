#coding:utf-8
# Author:  mozman
# Purpose: svg container classes
# Created: 15.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
The :mod:`container` module provides following structural objects:

* :class:`svgwrite.Group`
* :class:`svgwrite.SVG`
* :class:`svgwrite.Defs`
* :class:`svgwrite.Symbol`
* :class:`svgwrite.Use`

set/get SVG attributes::

    element['attribute'] = value
    value = element['attribute']

.. seealso::
   :ref:`Common SVG Attributs <Common-SVG-Attributs>`
"""

from svgwrite import parameter
from svgwrite.base import BaseElement
from svgwrite.interface import IViewBox, ITransform
from svgwrite.validator import check_coordinate


class Group(BaseElement, ITransform):
    """ The <g> element is a container element for grouping together
    related graphics elements.

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Methods**

    .. automethod:: svgwrite.Group.group(attributes)

    **Inherited Methods**

    .. automethod:: svgwrite.Group.add(element)

    .. automethod:: svgwrite.Group.tostring()

    .. automethod:: svgwrite.Group.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    **Supported SVG attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
        can proceed even if external resources are unavailable else: *True*
    * **transform** -- use :class:`svgwrite.interface.ITransform` interface

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    def _elementname(self):
        return 'g'

    def group(self, **attributes):
        """ Create a new group with SVG *attributs* and add the new group as subelement.

        :param attributes: SVG attributes as keyword arguments
        :return: the new created group element

        """
        g = Group(**attributes)
        self.add(g)
        return g

class Defs(Group):
    """ The <defs> element is a container element for referenced elements. For
    understandability and accessibility reasons, it is recommended that, whenever
    possible, referenced elements be defined inside of a *defs*.
    """
    def _elementname(self):
        return 'defs'

class Symbol(BaseElement, IViewBox):
    """ The <symbol> element is used to define graphical template objects which
    can be instantiated by a <use> element. The use of <symbol> elements for
    graphics that are used multiple times in the same document adds structure and
    semantics. Documents that are rich in structure may be rendered graphically,
    as speech, or as braille, and thus promote accessibility.

    **Methods**

    .. automethod:: svgwrite.Symbol.group(attributes)

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.Symbol.add(element)

    .. automethod:: svgwrite.Symbol.tostring()

    .. automethod:: svgwrite.Symbol.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.IViewBox`
        :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering can proceed
                                       even if external resources are unavailable else: *True*
    * **viewBox** -- use :class:`svgwrite.interface.IViewBox` interface
    * **preserveAspectRatio** -- use :class:`svgwrite.interface.IViewBox` interface

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    def _elementname(self):
        return 'symbol'

    def group(self, **attributes):
        """ Create a new group with SVG *attributs* and add the new group as subelement.

        :param attributes: SVG attributes as keyword arguments
        :return: the new created group element

        """
        g = Group(**attributes)
        self.add(g)
        return g

class SVG(Symbol):
    """ An SVG document fragment consists of any number of SVG elements contained
    within an <svg> element.

    An SVG document fragment can range from an empty fragment (i.e., no content
    inside of the <svg> element), to a very simple SVG document fragment containing
    a single SVG graphics element such as a <rect>, to a complex, deeply nested
    collection of container elements and graphics elements.

    .. automethod:: svgwrite.SVG.__init__([insert=None, size=None, attribs=None, \*\*extra])

    **Attributes**

    .. attribute:: defs

       `Defs` container for referenced elements

       adding SVG elements to *defs*::

         svgobject.defs.add(element)

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.SVG.add(element)

    .. automethod:: svgwrite.SVG.tostring()

    .. automethod:: svgwrite.SVG.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.IViewBox`
        :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

    **Supported SVG Attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **x** -- `coordinate` x-coordinate, if <svg> is enbedded into another <svg>-element
    * **y** -- `coordinate` y-coordinate, if <svg> is enbedded into another <svg>-element
    * **width** -- `length` canvas-width - default is '100%'
    * **height** -- `length` canvas-height - default is '100%'
    * **viewBox** -- :class:`svgwrite.interface.IViewBox` interface
    * **preserveAspectRatio**  -- :class:`svgwrite.interface.IViewBox` interface
    * **zoomAndPan** -- ``"disable"|"magnify"`` : default is ``"magnify"``
    * **externalResourcesRequired** -- `bool` *False*: if document rendering can proceed
        even if external resources are unavailable else: *True*

    .. note::
       do not set or change following SVG attributes:
       version, baseProfile, contentScriptType, contentStyleType

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Document Event Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    def __init__(self, insert=None, size=None, attribs=None, **extra):
        """
        :param 2-tuple insert: insert position
        :param 2-tuple size: width, height
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
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
    """ The <use> element references another element and indicates that the graphical
    contents of that element is included/drawn at that given point in the document.

    Link to objects by href = ``'#object-id'`` or use the object itself as href-argument,
    the object has to have an ``'id'`` attribute.

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.Use.add(element)

    .. automethod:: svgwrite.Use.tostring()

    .. automethod:: svgwrite.Use.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **x** -- `coordinate` insert x-coordinate, set on __init__(insert)
    * **y** -- `coordinate` insert y-coordinate, set on __init__(insert)
    * **width** -- `length` width - default is ``'100%'``, set on __init__(size)
    * **height** -- `length` height - default is ``'100%'``, set on __init__(size)
    * **transform** -- :class:`svgwrite.interface.ITransform` interface
    * **xlink:href** -- , set on __init__(href)
    * **externalResourcesRequired** -- `bool` *False*: if document rendering can proceed
        even if external resources are unavailable else: *True*

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    * XLink Attributes
    """
    def __init__(self, href, insert=None, size=None, attribs=None, **extra):
        """
        :param string href: object link (link to id) or an object with an id-attribute
        :param 2-tuple insert: insert point (x, y)
        :param 2-tuple size: width, height
        :param attribs dict: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
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
