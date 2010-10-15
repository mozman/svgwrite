#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: element factory
# Created: 15.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import container
import shapes
import path
import image
import text

factoryelements = {
    'g': container.Group,
    'svg': container.SVG,
    'defs': container.Defs,
    'symbol': container.Symbol,
    'use': container.Use,
    'a': container.Hyperlink,
    'line': shapes.Line,
    'rect': shapes.Rect,
    'circle': shapes.Circle,
    'ellipse': shapes.Ellipse,
    'polyline': shapes.Polyline,
    'polygon': shapes.Polygon,
    'path': path.Path,
    'image': image.Image,
    'text': text.Text,
    'tspan': text.TSpan,
    'tref': text.TRef,
    'textPath': text.TextPath,
    'textArea': text.TextArea,
}

class ElementBuilder(object):
    def __init__(self, cls, post_creation):
        self.cls = cls
        self.post_creation = post_creation

    def __call__(self, *args, **kwargs):
        element = self.cls(*args, **kwargs) # create an object of type 'cls'
        self.post_creation(element) # do something after the object creation
        return element # return the modified object

class ElementFactory(object):
    def __getattr__(self, name):
        if name in factoryelements:
            return ElementBuilder(factoryelements[name], self.post_creation)
        else:
            raise AttributeError("'%s' has no attribute '%s'" % (self.__class__.__name__, name))

    def post_creation(self, element):
        # every object get the same debug and profile parameters
        element.set_parameter(self._parameter)
