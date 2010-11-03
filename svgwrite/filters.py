#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: filters module
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

class FilterPrimitive(BaseElement):
    pass

class feBlend(FilterPrimitive):
    elementname = 'feBlend'

class feColorMatrix(FilterPrimitive):
    elementname = 'feColorMatrix'

class feComponentTransfer(FilterPrimitive):
    elementname = 'feComponentTransfer'

class feFuncR(FilterPrimitive):
    elementname = 'feFuncR'

class feFuncG(FilterPrimitive):
    elementname = 'feFuncG'

class feFuncB(FilterPrimitive):
    elementname = 'feFuncB'

class feFuncA(FilterPrimitive):
    elementname = 'feFuncA'

class feComposite(FilterPrimitive):
    elementname = 'feComposite'

class feConvolveMatrix(FilterPrimitive):
    elementname = 'feConvolveMatrix'

class feDiffuseLightning(FilterPrimitive):
    elementname = 'feDiffuseLightning'

class feDisplacementMap(FilterPrimitive):
    elementname = 'feDisplacementMap'

class feFlood(FilterPrimitive):
    elementname = 'feFlood'

class feGaussianBlur(FilterPrimitive):
    elementname = 'feGaussianBlur'

class feImage(FilterPrimitive):
    elementname = 'feImage'

class feMergeNode(FilterPrimitive):
    elementname = 'feMergeNode'

class feMerge(FilterPrimitive):
    elementname = 'feMerge'
    def add_nodes(self, layernames):
        for layername in layernames:
            self.add(feMergeNode(in_=layername, factory=self))

class feMorphology(FilterPrimitive):
    elementname = 'feMorphology'

class feOffset(FilterPrimitive):
    elementname = 'feOffset'

class feSpecularLightning(FilterPrimitive):
    elementname = 'feSpecularLightning'

class feTile(FilterPrimitive):
    elementname = 'feTile'

class feTurbolance(FilterPrimitive):
    elementname = 'feTurbolance'
