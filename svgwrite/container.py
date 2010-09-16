#coding:utf-8
# Author:  mozman
# Purpose: svg container classes
# Created: 15.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from interface import IViewBox, ITransform
from validator import check_coordinate

class Defs(BaseElement, ITransform):
    """ The <defs /> element> """
    pass

class Group(BaseElement, ITransform):
    """ The <g /> svg element. """
    def _elementname(self):
        return 'g'

    def group(self, **kwargs):
        g = Group(**kwargs)
        self.add(g)
        return g

class Symbol(BaseElement, IViewBox):
    """ The <symbol /> svg element. """
    # ITransform interface is not valid for Symbol -> do not inherit from Group
    def _elementname(self):
        return 'symbol'

    def group(self, **kwargs):
        g = Group(**kwargs)
        self.add(g)
        return g

class Use(BaseElement, ITransform):
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
