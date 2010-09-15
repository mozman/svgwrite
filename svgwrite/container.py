#coding:utf-8
# Author:  mozman
# Purpose: svg container classes
# Created: 15.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
from base import BaseElement, IViewBox
from validator import check_coordinate

class Group(BaseElement):
    """ The <g /> svg element. """
    def _elementname(self):
        return 'g'

class Symbol(BaseElement, IViewBox):
    """ The <symbol /> svg element. """
    pass

class Use(BaseElement):
    """ The <use /> svg element. """
    def __init__(self, href, insert=None, size=None, attribs=None, **extra):
        """ Constructor

        Attribute:
        ----------
        href -- object link (link to id)
        insert -- <2-tuple> insert point (x,y)
        size -- <2-tuple> (width, height)
        """
        super(Use, self).__init__(attribs, **extra)
        self.attribs['xlink:href'] = href
        if insert:
            self.attribs['x'] = check_coordinate(insert[0])
            self.attribs['y'] = check_coordinate(insert[1])
        if size:
            self.attribs['width'] = check_coordinate(size[0])
            self.attribs['height'] = check_coordinate(size[1])
