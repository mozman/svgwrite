#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svg types
# Created: 30.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

class SVGAttribute(object):
    def __init__(self, name, anim, types, const):
        self.name = name
        self.anim = anim
        self.valid_types = types
        self.valid_const = const

class SVGElement(object):
    def __init__(self, name, attributes, properties, children):
        self.name = name
        s = set()
        if attributes:
            s.update(attributes)
        if properties:
            s.update(properties)
        self.valid_attributes = frozenset(s)
        s =set()
        if children:
            s.update(children)
        self.valid_children = frozenset(s)
