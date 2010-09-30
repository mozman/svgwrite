#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svg properties
# Created: 30.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

class SVGProperty(object):
    def __init__(self, name, anim, inherit, types, strings):
        self.name = name
        self.anim = anim
        self.valid_types = types
        self.valid_strings = strings
