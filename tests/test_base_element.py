#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test BaseElement
# Created: 18.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.base import BaseElement
from svgwrite.params import Parameter
from svgwrite.utils import is_string


class MockBase(BaseElement):
    elementname = 'svg' # necessary for validator
    _parameter = Parameter(True, 'full')


class TestBaseElement(unittest.TestCase):

    def test_constructor_valid(self):
        # valid attributes
        m = MockBase(width=100, height=200)
        self.assertEqual(m['width'], 100)
        self.assertEqual(m['height'], 200)

    def test_trailing_underscore(self):
        m = MockBase(class_='test')
        self.assertEqual(m['class'], 'test')

    def test_inner_underscore(self):
        m = MockBase(stroke_width='1.0')
        self.assertEqual(m['stroke-width'], '1.0')

    def test_constructor_invalid(self):
        self.assertRaises(ValueError, MockBase, mozman=100)
        self.assertRaises(ValueError, MockBase, attribs={'mozman':100})

    def test_tostring(self):
        # valid attributes
        m = MockBase(width=100, height=200)
        self.assertEqual(m.tostring(), '<svg height="200" width="100" />')

    def test_attribute_access(self):
        m = MockBase()
        m['id'] = 'test'
        self.assertEqual(m['id'], 'test')

    def test_get_funciri(self):
        m = MockBase()
        m['id'] = 'test'
        self.assertEqual(m.get_funciri(), "url(#test)")

    def test_copy(self):
        # valid attributes
        m = MockBase(width=100, height=200)
        m.add(MockBase(width=100, height=200))
        copy = m.copy()
        m['width'] = 999
        self.assertEqual(copy.tostring(), '<svg height="200" width="100"><svg height="200" width="100" /></svg>')


class TestValueToString(unittest.TestCase):
    def test_full_profile(self):
        element = MockBase()
        self.assertEqual(u'test', element.value_to_string('test'))
        self.assertEqual(u'süß', element.value_to_string('süß'))
        self.assertEqual(u'10', element.value_to_string(10))

    def test_tiny_profile(self):
        element = MockBase()
        element.set_parameter(Parameter(True, 'tiny'))

        # value out of range
        self.assertRaises(TypeError, element.value_to_string, 100000)
        self.assertEqual('3.1416', element.value_to_string(3.141592))

    def test_is_unicode(self):
        element = MockBase()
        self.assertTrue(is_string(element.value_to_string(10)))
        self.assertTrue(is_string(element.value_to_string('test')))


if __name__ == '__main__':
    unittest.main()
