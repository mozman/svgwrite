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
* :class:`svgwrite.Hyperlink`

set/get SVG attributes::

    element['attribute'] = value
    value = element['attribute']

.. seealso::
   :ref:`Common SVG Attributs <Common-SVG-Attributs>`
"""

from base import BaseElement
from interface import IViewBox, ITransform, IXLink

class Group(BaseElement, ITransform):
    """ The <g> element is a container element for grouping together
    related graphics elements.

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.container.Group.add(element)

    .. automethod:: svgwrite.container.Group.tostring()

    .. automethod:: svgwrite.container.Group.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    **Supported SVG attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*
    * **transform** -- use :class:`svgwrite.interface.ITransform` interface

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    elementname = 'g'

class Defs(Group):
    """ The <defs> element is a container element for referenced elements. For
    understandability and accessibility reasons, it is recommended that, whenever
    possible, referenced elements be defined inside of a *defs*.
    """
    elementname= 'defs'

class Symbol(BaseElement, IViewBox):
    """ The <symbol> element is used to define graphical template objects which
    can be instantiated by a <use> element. The use of <symbol> elements for
    graphics that are used multiple times in the same document adds structure and
    semantics. Documents that are rich in structure may be rendered graphically,
    as speech, or as braille, and thus promote accessibility.

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.container.Symbol.add(element)

    .. automethod:: svgwrite.container.Symbol.tostring()

    .. automethod:: svgwrite.container.Symbol.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.IViewBox`
        :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*
    * **viewBox** -- use :class:`svgwrite.interface.IViewBox` interface
    * **preserveAspectRatio** -- use :class:`svgwrite.interface.IViewBox`
      interface

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    elementname = 'symbol'

class SVG(Symbol):
    """ An SVG document fragment consists of any number of SVG elements contained
    within an <svg> element.

    An SVG document fragment can range from an empty fragment (i.e., no content
    inside of the <svg> element), to a very simple SVG document fragment containing
    a single SVG graphics element such as a <rect>, to a complex, deeply nested
    collection of container elements and graphics elements.

    .. automethod:: svgwrite.container.SVG.__init__([insert=None, size=None, attribs=None, \*\*extra])

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

    .. automethod:: svgwrite.container.SVG.add(element)

    .. automethod:: svgwrite.container.SVG.tostring()

    .. automethod:: svgwrite.container.SVG.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.IViewBox`
        :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

    **Supported SVG Attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **x** -- `coordinate` x-coordinate, if <svg> is enbedded into another
      <svg>-element
    * **y** -- `coordinate` y-coordinate, if <svg> is enbedded into another
      <svg>-element
    * **width** -- `length` canvas-width - default is '100%'
    * **height** -- `length` canvas-height - default is '100%'
    * **viewBox** -- :class:`svgwrite.interface.IViewBox` interface
    * **preserveAspectRatio**  -- :class:`svgwrite.interface.IViewBox` interface
    * **zoomAndPan** -- ``"disable"|"magnify"`` : default is ``"magnify"``
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*

    .. note::
       do not set or change following SVG attributes:
       version, baseProfile, contentScriptType, contentStyleType

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Document Event Attributes </attributes/document_event>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    elementname = 'svg'

    def __init__(self, insert=None, size=None, attribs=None, **extra):
        """
        :param 2-tuple insert: insert position
        :param 2-tuple size: width, height
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(SVG, self).__init__(attribs=attribs, **extra)
        if insert:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size:
            self['width'] = size[0]
            self['height'] = size[1]

        self.defs = Defs(factory=self) # defs container
        self.add(self.defs) # add defs as first element

class Use(BaseElement, ITransform, IXLink):
    """ The <use> element references another element and indicates that the graphical
    contents of that element is included/drawn at that given point in the document.

    Link to objects by href = ``'#object-id'`` or use the object itself as
    href-argument, if the given element has no *id* attribute it gets an
    automatic generated id.

    .. automethod:: svgwrite.container.Use.__init__(href, [insert=None, size=None, attribs=None, \*\*extra])

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.container.Use.add(element)

    .. automethod:: svgwrite.container.Use.tostring()

    .. automethod:: svgwrite.container.Use.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    :class:`svgwrite.interface.IXLink`
        :meth:`set_href`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **x** -- `coordinate` insert x-coordinate, set on __init__(insert)
    * **y** -- `coordinate` insert y-coordinate, set on __init__(insert)
    * **width** -- `length` width - default is ``'100%'``, set on __init__(size)
    * **height** -- `length` height - default is ``'100%'``, set on __init__(size)
    * **transform** -- :class:`svgwrite.interface.ITransform` interface
    * **xlink:href** -- `string` set on __init__(href)
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`
    * :doc:`XLink Attributes </attributes/xlink>`

    """
    elementname = 'use'

    def __init__(self, href, insert=None, size=None, attribs=None, **extra):
        """
        :param string href: object link (id-string) or an object with an id-attribute
        :param 2-tuple insert: insert point (x, y)
        :param 2-tuple size: width, height
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Use, self).__init__(attribs, **extra)
        self.set_href(href)
        if insert:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size:
            self['width'] = size[0]
            self['height'] = size[1]

    def get_xml(self):
        self.update_id() # if href is an object - 'id' - attribute may be changed!
        return super(Use, self).get_xml()

class Hyperlink(BaseElement, ITransform):
    """ The <a> element indicate links (also known as Hyperlinks or Web links).

    The remote resource (the destination for the link) is defined by a <IRI>
    specified by the XLink ``xlink:href`` attribute. The remote resource may be
    any Web resource (e.g., an image, a video clip, a sound bite, a program,
    another SVG document, an HTML document, an element within the current
    document, an element within a different document, etc.). By activating
    these links (by clicking with the mouse, through keyboard input, voice
    commands, etc.), users may visit these resources.

    A :class:`Hyperlink` is defined for each separate rendered element
    contained within the :class:`Hyperlink` class; add sublements as usual with
    the :meth:`add` method.

    .. automethod:: svgwrite.container.Hyperlink.__init__(href, [target='_blank', attribs=None, \*\*extra])

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.container.Hyperlink.add(element)

    .. automethod:: svgwrite.container.Hyperlink.tostring()

    .. automethod:: svgwrite.container.Hyperlink.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **transform** -- :class:`svgwrite.interface.ITransform` interface
    * **xlink:href** -- `string` set on :meth:`__init__`
    * **xlink:show** -- ``'new|replace'`` use the **target** attribute
    * **xlink:acuate** -- `string` ``'onRequest'`` This attribute provides
      documentation to XLink-aware processors that an application should
      traverse from the starting resource to the ending resource only on a
      post-loading event triggered for the purpose of traversal.
    * **target** -- `string` This attribute specifies the name or portion of
      the target window, frame, pane, tab, or other relevant presentation
      context (e.g., an HTML or XHTML frame, iframe, or object element)
      into which a document is to be opened when the link is activated.

      - ``_replace``: The current SVG image is replaced by the linked
        content in the same rectangular area in the same frame as the
        current SVG image.
      - ``_self``: The current SVG image is replaced by the linked content
         in the same frame as the current SVG image. This is the lacuna
         value, if the target attribute is not specified.
      - ``_parent``: The immediate frameset parent of the SVG image is
        replaced by the linked content.
      - ``_top``: The content of the full window or tab, including any
        frames, is replaced by the linked content
      - ``_blank``: A new un-named window or tab is requested for the
        display of the linked content. If this fails, the result is the
        same as ``_top``
      - ``<XML-Name>``: Specifies the name of the frame, pane, or other
        relevant presentation context for display of the linked content.
        If this already exists, it is re-used, replacing the existing
        content. If it does not exist, it is created (the same as ``_blank``,
        except that it now has a name).

    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`
    * :doc:`XLink Attributes </attributes/xlink>`

    """
    elementname = 'a'
    def __init__(self, href, target='_blank', attribs=None, **extra):
        """
        :param string href: hyperlink to the target resource
        :param string target: ``'_blank|_replace|_self|_parent|_top|<XML-name>'``
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Hyperlink, self).__init__(attribs, **extra)
        self['xlink:href'] = href
        self['target'] = target
        if self.debug:
            self.validator.check_all_svg_attribute_values(self.elementname, self.attribs)
