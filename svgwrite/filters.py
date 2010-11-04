#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: filters module
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from interface import IXLink
from mixins import Presentation
from utils import strlist

class _FilterPrimitive(BaseElement, Presentation):
    pass

class _FilterRequireInput(_FilterPrimitive):
    def __init__(self, in_, start=None, size=None, **extra):
        super(_FilterRequireInput, self).__init__(**extra)
        self['in'] = in_
        if start is not None:
            self['x'] = start[0]
            self['y'] = start[1]
        if size is not None:
            self['width'] = size[0]
            self['height'] = size[1]

class _feBlend(_FilterRequireInput):
    elementname = 'feBlend'

class _feColorMatrix(_FilterRequireInput):
    elementname = 'feColorMatrix'

class _feComponentTransfer(_FilterRequireInput):
    elementname = 'feComponentTransfer'
    def feFuncR(self, *args, **kwargs):
        return self.add(_feFuncR(factory=self, *args, **kwargs))
    def feFuncG(self, *args, **kwargs):
        return self.add(_feFuncG(factory=self, *args, **kwargs))
    def feFuncB(self, *args, **kwargs):
        return self.add(_feFuncB(factory=self, *args, **kwargs))
    def feFuncA(self, *args, **kwargs):
        return self.add(_feFuncA(factory=self, *args, **kwargs))

class _feFuncR(_FilterPrimitive):
    elementname = 'feFuncR'
    def __init__(self, type_, **extra):
        super(_feFuncR, self).__init__(**extra)
        self['type'] = type_

class _feFuncG(_feFuncR):
    elementname = 'feFuncG'

class _feFuncB(_feFuncR):
    elementname = 'feFuncB'

class _feFuncA(_feFuncR):
    elementname = 'feFuncA'

class _feComposite(_FilterRequireInput):
    elementname = 'feComposite'

class _feConvolveMatrix(_FilterRequireInput):
    elementname = 'feConvolveMatrix'

class _feDiffuseLightning(_FilterRequireInput):
    elementname = 'feDiffuseLightning'

class _feDisplacementMap(_FilterRequireInput):
    elementname = 'feDisplacementMap'

class _feFlood(_FilterRequireInput):
    elementname = 'feFlood'

class _feGaussianBlur(_FilterRequireInput):
    elementname = 'feGaussianBlur'

class _feImage(_FilterRequireInput):
    elementname = 'feImage'

class _feMergeNode(_FilterRequireInput):
    elementname = 'feMergeNode'

class _feMerge(_FilterRequireInput):
    elementname = 'feMerge'
    def add_nodes(self, layernames):
        for layername in layernames:
            self.add(_feMergeNode(in_=layername, factory=self))

class _feMorphology(_FilterRequireInput):
    elementname = 'feMorphology'

class _feOffset(_FilterRequireInput):
    elementname = 'feOffset'

class _feSpecularLightning(_FilterRequireInput):
    elementname = 'feSpecularLightning'

class _feTile(_FilterRequireInput):
    elementname = 'feTile'

class _feTurbolance(_FilterRequireInput):
    elementname = 'feTurbolance'

filter_factory = {
    'feBlend': _feBlend,
    'feColorMatrix': _feColorMatrix,
    'feComponentTransfer': _feComponentTransfer,
    'feComposite': _feComposite,
    'feConvolveMatrix': _feConvolveMatrix,
    'feDiffuseLightning': _feDiffuseLightning,
    'feDisplacementMap': _feDisplacementMap,
    'feFlood': _feFlood,
    'feGaussianBlur': _feGaussianBlur,
    'feImage': _feImage,
    'feMerge': _feMerge,
    'feMorphology': _feMorphology,
    'feOffset': _feOffset,
    'feSpecularLightning': _feSpecularLightning,
    'feTile': _feTile,
    'feTurbolence': _feTurbolance,
}

class _FilterBuilder(object):
    def __init__(self, cls, parent):
        self.cls = cls # primitive filter class to build
        self.parent = parent # the parent Filter() object

    def __call__(self, *args, **kwargs):
        kwargs['factory'] = self.parent # to get the _paramters object
        obj = self.cls(*args, **kwargs) # create an object of type 'cls'
        self.parent.add(obj) # add primitive filter to parent Filter()
        return obj

class Filter(BaseElement, IXLink, Presentation):
    elementname = 'filter'
    def __init__(self, start=None, size=None, resolution=None, inherit=None, **extra):
        super(Filter, self).__init__(**extra)
        if start is not None:
            self['x'] = start[0]
            self['y'] = start[1]
        if size is not None:
            self['width'] = size[0]
            self['height'] = size[1]
        if resolution is not None:
            if isinstance(resolution, basestring):
                self['filterRes'] = resolution
            elif hasattr(resolution, '__iter__'):
                self['filterRes'] = strlist(resolution, ' ')
            else:
                self['filterRes'] = str(resolution)

        if inherit is not None:
            self.href = inherit
            self.update_id()

    def get_xml(self):
        self.update_id()
        return super(Filter, self).get_xml()

    def __getattr__(self, name):
        # create primitive filters by Filter.<filtername>(...)
        # and auto-add the new filter as subelement of Filter()
        if name in filter_factory:
            return _FilterBuilder(filter_factory[name], self)
        else:
            raise AttributeError("'%s' has no attribute '%s'" % (self.__class__.__name__, name))

