#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test BaseElement
# Created: 18.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.base import BaseElement
from svgwrite import parameter

class MockBase(BaseElement):
    elementname = 'svg' # necessary for validator

class TestBaseElement(unittest.TestCase):
    def setUp(self):
        parameter.set_debug()
        parameter.set_profile('full')


    def test_constructor_valid(self):
        # valid attributes
        m = MockBase(width=100, height=200)
        self.assertEqual(m['width'], 100)
        self.assertEqual(m['height'], 200)

        # use attribs-dict
        m = MockBase(attribs={'width':100, 'height':200})
        self.assertEqual(m['width'], 100)
        self.assertEqual(m['height'], 200)

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



if __name__=='__main__':
    unittest.main()