#coding:utf-8
# Author:  mozman
# Purpose: svg container classes
# Created: 15.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
The **container** module provides following structural objects:

* :class:`svgwrite.Group`
* :class:`svgwrite.SVG`
* :class:`svgwrite.Defs`
* :class:`svgwrite.Symbol`
* :class:`svgwrite.Marker`
* :class:`svgwrite.Use`
* :class:`svgwrite.Hyperlink`

set/get SVG attributes::

    element['attribute'] = value
    value = element['attribute']

"""

from svgwrite.base import BaseElement
from svgwrite.mixins import ViewBox, Transform, XLink
from svgwrite.mixins import Presentation, Clipping

class Group(BaseElement, Transform, Presentation):
    """ The **Group** (SVG **g**) element is a container element for grouping
    together related graphics elements.

    Grouping constructs, when used in conjunction with the **desc** and **title**
    elements, provide information about document structure and semantics.
    Documents that are rich in structure may be rendered graphically, as speech,
    or as braille, and thus promote accessibility.

    A group of elements, as well as individual objects, can be given a name using
    the **id** attribute. Named groups are needed for several purposes such as
    animation and re-usable objects.

    """
    elementname = 'g'

class Defs(Group):
    """ The **defs** element is a container element for referenced elements. For
    understandability and accessibility reasons, it is recommended that, whenever
    possible, referenced elements be defined inside of a **defs**.
    """
    elementname= 'defs'

class Symbol(BaseElement, ViewBox, Presentation, Clipping):
    """ The **symbol** element is used to define graphical template objects which
    can be instantiated by a **use** element. The use of **symbol** elements for
    graphics that are used multiple times in the same document adds structure and
    semantics. Documents that are rich in structure may be rendered graphically,
    as speech, or as braille, and thus promote accessibility.
    """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    elementname = 'symbol'

class Marker(BaseElement, ViewBox, Presentation):
    """ The **marker** element defines the graphics that is to be used for
    drawing arrowheads or polymarkers on a given **path**, **line**, **polyline**
    or **polygon** element.

    Add Marker definitions to a **defs** section, preferred to the **defs** section
    of the **main drawing**.

    """
    elementname = 'marker'
    def __init__(self, insert=None, size=None, orient=None, **extra):
        """
        :param 2-tuple insert: reference point (**refX**, **refY**)
        :param 2-tuple size: (**markerWidth**, **markerHeight**)
        :param orient: ``'auto'`` | `angle`
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Marker, self).__init__(**extra)
        if insert:
            self['refX'] = insert[0]
            self['refY'] = insert[1]
        if size:
            self['markerWidth'] = size[0]
            self['markerHeight'] = size[1]
        if orient is not None:
            self['orient'] = orient
        if 'id' not in self.attribs: # an 'id' is necessary
            self['id'] = self.next_id()

class SVG(Symbol):
    """ An SVG document fragment consists of any number of SVG elements contained
    within an **svg** element.

    An SVG document fragment can range from an empty fragment (i.e., no content
    inside of the **svg** element), to a very simple SVG document fragment containing
    a single SVG graphics element such as a **rect**, to a complex, deeply nested
    collection of container elements and graphics elements.
    """
    elementname = 'svg'

    def __init__(self, insert=None, size=None, **extra):
        """
        :param 2-tuple insert: insert position (**x**, **y**)
        :param 2-tuple size: (**width**, **height**)
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(SVG, self).__init__(**extra)
        if insert:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size:
            self['width'] = size[0]
            self['height'] = size[1]

        self.defs = Defs(factory=self) # defs container
        self.add(self.defs) # add defs as first element

class Use(BaseElement, Transform, XLink, Presentation):
    """ The **use** element references another element and indicates that the graphical
    contents of that element is included/drawn at that given point in the document.

    Link to objects by href = ``'#object-id'`` or use the object itself as
    href-argument, if the given element has no **id** attribute it gets an
    automatic generated id.

    """
    elementname = 'use'

    def __init__(self, href, insert=None, size=None, **extra):
        """
        :param string href: object link (id-string) or an object with an id-attribute
        :param 2-tuple insert: insert point (**x**, **y**)
        :param 2-tuple size: (**width**, **height**)
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Use, self).__init__(**extra)
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

class Hyperlink(BaseElement, Transform, Presentation):
    """ The **a** element indicate links (also known as Hyperlinks or Web links).

    The remote resource (the destination for the link) is defined by a `<IRI>`
    specified by the XLink **xlink:href** attribute. The remote resource may be
    any Web resource (e.g., an image, a video clip, a sound bite, a program,
    another SVG document, an HTML document, an element within the current
    document, an element within a different document, etc.). By activating
    these links (by clicking with the mouse, through keyboard input, voice
    commands, etc.), users may visit these resources.

    A **Hyperlink** is defined for each separate rendered element
    contained within the **Hyperlink** class; add sublements as usual with
    the `add` method.

    """
    elementname = 'a'
    def __init__(self, href, target='_blank', **extra):
        """
        :param string href: hyperlink to the target resource
        :param string target: ``'_blank|_replace|_self|_parent|_top|<XML-name>'``
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Hyperlink, self).__init__(**extra)
        self['xlink:href'] = href
        self['target'] = target
