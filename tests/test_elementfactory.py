#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test elementfactory
# Created: 15.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

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

    def test_line(self):
        element = self.factory.line((0,0), (1,1))
        self.assertEqual(element.elementname, 'line')

    def test_rect(self):
        element = self.factory.rect((0,0), (1,1))
        self.assertEqual(element.elementname, 'rect')

    def test_circle(self):
        element = self.factory.circle((0,0), 5)
        self.assertEqual(element.elementname, 'circle')

    def test_ellipse(self):
        element = self.factory.ellipse((0,0), (5, 5))
        self.assertEqual(element.elementname, 'ellipse')

    def test_polygon(self):
        element = self.factory.polygon([(0, 0), (5, 5)])
        self.assertEqual(element.elementname, 'polygon')

    def test_polyline(self):
        element = self.factory.polyline([(0, 0), (5, 5)])
        self.assertEqual(element.elementname, 'polyline')

    def test_AttributeError(self):
        try:
            self.factory.test()
            self.fail('AttributeError not raised.')
        except AttributeError:
            self.assertTrue(True)

if __name__=='__main__':
    unittest.main()
