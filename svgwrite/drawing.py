#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: drawing
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from svgwrite.parameter import check_coordinate, profile

from svgwrite.base import BaseElement

_svg_attribs = ['width', 'height', 'version', 'xmlns', 'viewBox', 'x', 'y',
                'preserveAspectRatio', 'baseProfile', 'zoomAndPan',
                'snapshottime', 'playbackOrder', 'timelineBegin',
                'contentScriptType', 'contentStyleType']

class Drawing(BaseElement):
    def __init__(self, filename="noname.svg", width='100%', height='100%'):
        super(Drawing, self).__init__(version="1.2",
                                      xmlns="http://www.w3.org/2000/svg",
                                      width=width, height=height)
        self.filename = name

    def get_xml(self):
        self.attribs['baseProfile'] = profile
        return super(Drawing, self).get_xml()

    def viewbox(self, x1=0, y1=0, x2=0, y2=0):
        for value in (x1, y1, x2, y2):
            check_coordinate(value)
        self.attribs['viewBox'] = "%s,%s,%s,%s" % (x1, y1, x2, y2)

    def _element_name(self):
        return 'svg'

    def _valid_attribs(self):
        return _svg_attribs

    def write(self, fileobj):
        xmlstr = self.tostring().encode('utf-8')
        fileobj.write(xmlstr)

    def save(self):
        fileobj = open(self.name, mode='w')
        self.write(fileobj)
        fileobj.close

    def saveas(self, filename):
        self.filename = filename
        self.save()