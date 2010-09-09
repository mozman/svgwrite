#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg base element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

class BaseElement(object):
    def __init__(self, attribs=None, **kwargs):
        if attribs == None:
            self.attribs = dict()
        else:
            self.attribs = dict(attribs)
        self.update(kwargs)
        self.elements = list()

    def __getitem__(self, key):
        return self.attribs[key]

    def __setitem__(self, key, value):
        self.attribs[key] = value

    def tostring(self, profile="tiny"):
        """ get XML as string representation. """
        etree = self.get_etree(profile)
        return etree.tostring()

    def add(self, element):
        """ add subelement """
        self.elements.append(element)

    def get_etree(self, profile="tiny"):
        """ get XML as ElementTree object. """

    def add_to_etree(self, etree, profile="tiny"):
        """ add XML to etree object. """
        etree.add(self.get_etree(profile))

    def name(self):
        return self.__class__.__name__.lower()
