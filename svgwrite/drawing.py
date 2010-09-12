#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: drawing
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite import parameter
from svgwrite.validator import check_coordinate
from svgwrite.base import BaseElement

class Drawing(BaseElement):
    def __init__(self, filename="noname.svg", width='100%', height='100%', **kwargs):
        super(Drawing, self).__init__(xmlns="http://www.w3.org/2000/svg",
                                      width=width, height=height, **kwargs)
        self.filename = filename

    def get_xml(self):
        profile = parameter.profile
        if profile == 'tiny':
            version = '1.2' # only tiny
        else:
            version = '1.1' # basic or full
        self.attribs['baseProfile'] = profile
        self.attribs['version'] = version
        return super(Drawing, self).get_xml()

    def viewbox(self, x1=0, y1=0, x2=0, y2=0):
        for value in (x1, y1, x2, y2):
            check_coordinate(value)
        self.attribs['viewBox'] = "%s,%s,%s,%s" % (x1, y1, x2, y2)

    def _elementname(self):
        return 'svg'

    def write(self, fileobj):
        xmlstr = self.tostring()
        fileobj.write(xmlstr)

    def save(self):
        fileobj = open(self.name, mode='w')
        self.write(fileobj)
        fileobj.close

    def saveas(self, filename):
        self.filename = filename
        self.save()