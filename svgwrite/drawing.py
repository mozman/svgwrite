#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: drawing
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
The :class:`~svgwrite.Drawing` object is the overall container for all SVG
elements. It provides the methods to store the drawing into a file or a
file-like object. If you want to use stylesheets, the reference links
to this stylesheets were also stored (:meth:`~Drawing.add_stylesheet`)
in the :class:`~svgwrite.Drawing` object.

set/get SVG attributes::

    element['attribute'] = value
    value = element['attribute']

.. seealso::
   :ref:`Common SVG Attributs <Common-SVG-Attributs>`

The *Drawing* class inherits from: :class:`~svgwrite.SVG`
"""

from container import SVG, Defs

class Drawing(SVG):
    """ This is the SVG drawing represented by the top level <svg /> element.

    A drawing consists of any number of SVG elements contained within the drawing
    element, stored in the :attr:`elements` attribute.

    A drawing can range from an empty drawing (i.e., no content inside of the drawing),
    to a very simple drawing containing a single SVG element such as a <rect>,
    to a complex, deeply nested collection of container elements and graphics elements.

    .. automethod:: svgwrite.Drawing.__init__([filename="noname.svg", size=('100%', '100%'), **extra])

    **Attributes**

    .. attribute:: filename

       `string` should be valid for :func:`open`.

    **Inherited Attributes**

    .. attribute:: attribs

       `dict` of SVG attributes

    .. attribute:: elements

       `list` of SVG subelements

    .. attribute:: defs

       `Defs` container for referenced SVG elements

    **Methods**

    .. automethod:: write(fileobj)

    .. automethod:: save()

    .. automethod:: saveas(filename)

    .. automethod:: add_stylesheet(href, title, alternate, media)

    .. automethod:: get_xml()

    **Inherited Methods**

    .. automethod:: add(element)


    .. automethod:: tostring()

    **Supported Interfaces**

    :class:`~svgwrite.interface.IViewBox`

    """
    def __init__(self, filename="noname.svg", size=('100%', '100%'), **extra):
        """
        :param string filename: filesystem filename valid for :func:`open`
        :param 2-tuple size: width, height
        :param keywords extra: additional svg-attributs for the *SVG* object

        """
        super(Drawing, self).__init__(size=size, **extra)
        self.filename = filename
        self._stylesheets = [] # list of stylesheets appended

    def get_xml(self):
        """ Get the XML representation as `ElementTree` object.

        :return: XML `ElementTree` of this object and all its subelements

        """
        profile = self.profile
        version = self.get_version()
        self.attribs['xmlns'] = "http://www.w3.org/2000/svg"
        self.attribs['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
        self.attribs['xmlns:ev'] = "http://www.w3.org/2001/xml-events"

        self.attribs['baseProfile'] = profile
        self.attribs['version'] = version
        return super(Drawing, self).get_xml()

    def add_stylesheet(self, href, title, alternate="no", media="screen"):
        """ Add a stylesheet reference.

        :param string href: link to stylesheet <URI>
        :param string title: name of stylesheet
        :param string alternate: ``'yes'|'no'``
        :param string media: ``'all'|'aureal'|'braille'|'embossed'|'handheld'|
            'print'|'projection'|'screen'|'tty'|'tv'``

        """
        self._stylesheets.append( (href, title, alternate, media) )

    def write(self, fileobj):
        """ Write the ``utf-8`` encoded XML string to *fileobj*.

        :param fileobj: a *file-like* object

        """
        # write xml header
        fileobj.write('<?xml version="1.0" encoding="utf-8" ?>\n')


        # don't use DOCTYPE. It's useless. see also:
        # http://tech.groups.yahoo.com/group/svg-developers/message/48562
        # write stylesheets
        for stylesheet in self._stylesheets:
            stylestr = u'<?xml-stylesheet href="%s" type="text/css" title="%s" ' \
                     'alternate="%s" media="%s"?>\n' % stylesheet
            fileobj.write(stylestr.encode('utf-8'))

        xmlstr = self.tostring()
        fileobj.write(xmlstr)

    def save(self):
        """ Write the ``utf-8`` encoded XML string to :attr:`filename`. """
        fileobj = open(self.filename, mode='w')
        self.write(fileobj)
        fileobj.close()

    def saveas(self, filename):
        """ Write the ``utf-8`` encoded XML string to *filename*.

        :param string filename: filesystem filename valid for :func:`open`
        """
        self.filename = filename
        self.save()
