#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: filter module
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from interface import IXLink

class Filter(BaseElement, IXLink):
    elementname = 'filter'
    def __init__(self, insert=None, size=None, inherit=None, **extra):
        super(Filter, self).__init__(**extra)
        if insert is not None:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size is not None:
            self['width'] = size[0]
            self['height'] = size[1]
        if inherit is not None:
            self.href = inherit
            self.update_id()

    def get_xml(self):
        self.update_id()
        return super(Filter, self).get_xml()

class feOffset(Filter):
    elementname = 'feOffset'