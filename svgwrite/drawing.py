#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: drawing
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite import parameter
from svgwrite.validator import check_coordinate
from container import SVG, Defs

class Drawing(SVG):
    """ This is the svg-drawing represented by the top level <svg /> element.

    A drawing consists of any number of SVG elements contained within the drawing
    element, stored in the element-attribute.

    A drawing can range from an empty drawing (i.e., no content inside of the drawing),
    to a very simple drawing containing a single svg-element such as a <rect>,
    to a complex, deeply nested collection of container elements and graphics elements.

    :param string filename: filesystem-filename, should be supported by the open-command
    :param 2-tuple size: width, height
    :param keywords extra: additional svg-attributs for th `<svg />` object

    **Attributes:**

    .. py:attribute:: filename

       `string` should be valid for open(filename, 'w')

    .. py:attribute:: attribs

       <inherited> `dict` svg attributes dictionary

    .. py:attribute:: elements

       <inherited> `list` of containing svg-elements

    .. py:attribute:: defs

       <inherited> `Defs` container for referenced elements

    **Methods:**

    .. py:method:: write(fileobj)

       write xml-string to fileobject, 'utf-8' encoded

    .. py:method:: save()

       store xml-string to the filesystem (uses self.filename)

    .. py:method:: saveas(filename)

       store xml-string to 'filename' resource

    .. py:method:: add_stylesheet(href, title, alternate, media)

       add a stylsheet reference

    .. py:method:: get_xml()

       get the xml-representation as ElementTree object

    Inherited Methods:

    .. py:method:: add(svg-element)

       add an svg-element

    .. py:method:: tostring()

       get the xml-representation as <string> 'utf-8' encoded

    Supported Interfaces:
    IViewBox: viewbox, stretch, fit

    Supported svg-attributes:
    see <SVG> class in container.py
    """
    def __init__(self, filename="noname.svg", size=('100%', '100%'), **extra):
        """ Constructor

        :param string filename: filesystem-filename, should be supported by the open-command
        :param 2-tuple size: width, height
        :param keywords extra: additional svg-attributs for th `<svg />` object

        """
        super(Drawing, self).__init__(size=size, **extra)
        self.filename = filename
        self._stylesheets = [] # list of stylesheets appended

    def get_xml(self):
        """ Get the xml-representation as ElementTree object. """
        profile = parameter.profile
        if profile == 'tiny':
            version = '1.2' # only tiny
        else:
            version = '1.1' # basic or full
        self.attribs['xmlns'] = "http://www.w3.org/2000/svg"
        self.attribs['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
        self.attribs['baseProfile'] = profile
        self.attribs['version'] = version
        return super(Drawing, self).get_xml()

    def add_stylesheet(self, href, title, alternate="no", media="screen"):
        """ Add a stylesheet reference.

        :param string href: link to stylesheet <URI>
        :param string title: name of stylesheet
        :param string alternate: 'yes' | 'no'
        :param string media: 'all' | 'aureal' | 'braille' | 'embossed' | 'handheld' | 'print' | 'projection' | 'screen' | 'tty' | 'tv'
        """
        self._stylesheets.append( (href, title, alternate, media) )

    def write(self, fileobj):
        """ Write the xml-string to 'fileobj', 'utf-8' encoded. """
        # write xml header
        fileobj.write('<?xml version="1.0" encoding="utf-8" ?>\n')
        if parameter.profile != 'tiny': # tiny profile has no DOCTYPE
            fileobj.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
                          '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
        # write stylesheets
        for stylesheet in self._stylesheets:
            stylestr = u'<?xml-stylesheet href="%s" type="text/css" title="%s" ' \
                     'alternate="%s" media="%s"?>\n' % stylesheet
            fileobj.write(stylestr.encode('utf-8'))

        xmlstr = self.tostring()
        fileobj.write(xmlstr)

    def save(self):
        """ Write the xml-representation as <string> to the 'self.filename'
        resource, 'utf-8' encoded.
        """
        fileobj = open(self.filename, mode='w')
        self.write(fileobj)
        fileobj.close()

    def saveas(self, filename):
        """ Write the xml-representation as <string> to the 'filename'
        resource, 'utf-8' encoded.
        """
        self.filename = filename
        self.save()
