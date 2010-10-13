#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svg image element
# Created: 09.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from params import parameter
from base import BaseElement
from interface import ITransform, _vert, _horiz

class Image(BaseElement, ITransform):
    """ The <image> element indicates that the contents of a complete file are
    to be rendered into a given rectangle within the current user coordinate
    system. The <image> element can refer to raster image files such as PNG
    or JPEG or to files with MIME type of "image/svg+xml".

    **Methods**

    .. automethod:: svgwrite.Image.__init__(href ,[insert=None, size=None, attribs=None, \*\*extra])

    .. automethod:: svgwrite.Image.stretch()

    .. automethod:: svgwrite.Image.fit([horiz="center", vert="middle", scale="meet"])

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    **Inherited Methods**

    .. automethod:: svgwrite.Image.add(element)

    .. automethod:: svgwrite.Image.tostring()

    .. automethod:: svgwrite.Image.get_xml()

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    **Supported svg-attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **x** -- `coordinate` insert x-coordinate, insert[0] parameter at
      :meth:`__init__`, default=0
    * **y** -- `coordinate` insert y-coordinate, insert[1] parameter at
      :meth:`__init__`, default=0
    * **width** -- `length` width - size[0] parameter at :meth:`__init__`
    * **height** -- `length` height - size[1] parameter at :meth:`__init__`
    * **transform** -- :class:`svgwrite.interface.ITransform` interface
    * **xlink:href** -- `string` hyperlink to the image resource,
      href parameter at :meth:`__init__`
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`
    * :doc:`XLink Attributes </attributes/xlink>`

    """
    elementname = 'image'

    def __init__(self, href, insert=None, size=None, attribs=None, **extra):
        """
        :param string href: hyperlink to the image resource
        :param 2-tuple insert: insert point (x, y)
        :param 2-tuple size: width, height
        :param dict attribs: additional SVG attributes
        :param extra: additional SVG attributs as keyword-arguments
        """
        super(Image, self).__init__(attribs, **extra)
        self['xlink:href'] = href
        if insert:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size:
            self['width'] = size[0]
            self['height'] = size[1]

    def stretch(self):
        """ Stretch viewBox in x and y direction to fill viewport, does not
        preserve aspect ratio.
        """
        self['preserveAspectRatio'] = 'none'

    def fit(self, horiz="center", vert="middle", scale="meet"):
        """ Set the preserveAspectRatio attribute.

        :param string horiz: horizontal alignment ``'left'|'center'|'right'``
        :param string vert: vertical alignment ``'top'|'middle'|'bottom'``
        :param string scale: scale method ``'meet'|'slice'``

        ============= ===========
        Scale methods Description
        ============= ===========
        ``meet``      preserve aspect ration and zoom to limits of viewBox
        ``slice``     preserve aspect ration and viewBox touch viewport on all bounds, viewBox will extend beyond the bounds of the viewport
        ============= ===========

        """
        if parameter.debug and scale not in ('meet', 'slice'):
            raise ValueError("Invalid scale parameter '%s'" % scale)
        self.attribs['preserveAspectRatio'] = "%s%s %s" % (_horiz[horiz],_vert[vert], scale)
