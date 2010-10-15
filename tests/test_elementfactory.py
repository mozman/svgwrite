#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test elementfactory
# Created: 15.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.elementfactory import ElementFactory
from svgwrite.params import Parameter

class MockFactory(ElementFactory):
    _parameter = Parameter(debug=True, profile='full')
    debug = True
    profile = 'full'

class TestElementFactory(unittest.TestCase):
    def setUp(self):
        self.factory = MockFactory()

    def test_g(self):
        group = self.factory.g(id='test')
        self.assertEqual(group.elementname, 'g')
        self.assertEqual(group['id'], 'test')

    def test_svg(self):
        svg = self.factory.svg()
        self.assertEqual(svg.elementname, 'svg')

    def test_defs(self):
        defs = self.factory.defs()
        self.assertEqual(defs.elementname, 'defs')

    def test_symbol(self):
        element = self.factory.symbol()
        self.assertEqual(element.elementname, 'symbol')

    def test_use(self):
        element = self.factory.use('link')
        self.assertEqual(element.elementname, 'use')

    def test_a(self):
        element = self.factory.a('link')
        self.assertEqual(element.elementname, 'a')

if __name__=='__main__':
    unittest.main()