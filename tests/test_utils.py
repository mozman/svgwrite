#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.parameter import init
from svgwrite.utils import rgb, value_to_string, points_to_string

class TestRgb(unittest.TestCase):
    def test_rgb_8bit(self):
        self.assertEqual(rgb(128, 128, 128), "rgb(128,128,128)")
        self.assertEqual(rgb(), "rgb(0,0,0)")
        # value overflow
        self.assertEqual(rgb(256, 256, 256), "rgb(0,0,0)")
        self.assertEqual(rgb(257, 257, 257), "rgb(1,1,1)")

    def test_rgb_percent(self):
        self.assertEqual(rgb(50, 50, 50, '%'), "rgb(50.000%,50.000%,50.000%)")
        self.assertEqual(rgb(mode='%'), "rgb(0.000%,0.000%,0.000%)")
        # value overflow
        self.assertEqual(rgb(101, -1, 101, '%'), "rgb(100.000%,0.000%,100.000%)")

    def test_rgb_invalid_mode(self):
        self.assertRaises(ValueError, rgb, mode='$')

class TestValueToString(unittest.TestCase):
    def test_full_profile(self):
        init(baseProfile='full', debug=True)
        self.assertEqual(u'test', value_to_string('test'))
        self.assertEqual(u'10', value_to_string(10))

    def test_tiny_profile(self):
        init(baseProfile='tiny', debug=True)
        # value out of range
        self.assertRaises(ValueError, value_to_string, 100000)

    def test_is_unicode(self):
        self.assertTrue(isinstance(value_to_string(10), unicode))
        self.assertTrue(isinstance(value_to_string('test'), unicode))

class TestPointsToStringFullProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='full', debug=True)

    def test_valid_points(self):
        # valid units: cm|em|ex|in|mm|pc|pt|px|%
        # dont't know if '%' is valid for points?
        result = points_to_string([(10,10), ('20cm', '20em'), ('30ex', '30in'), ('40mm', '40pc'), ('50pt', '50px'), ('60%', '60%')])
        # it's an unicode string
        self.assertTrue(isinstance(result, unicode))
        self.assertEqual(result, u"10,10 20cm,20em 30ex,30in 40mm,40pc 50pt,50px 60%,60%")
        # e-notation is valid
        result = points_to_string([('1e10pt','1e-10in')])
        self.assertEqual(result, u"1e10pt,1e-10in")

    def test_invalid_points(self):
        # invalid unit #'p'
        self.assertRaises(ValueError, points_to_string, [(10,10), ('20p', '20px')])

    def test_invalid_tuple_count(self):
        # 3-tuple not allowed
        self.assertRaises(ValueError, points_to_string, [(10,10), ('20px', '20px', '20px')])
        # 1-tuple not allowed
        self.assertRaises(ValueError, points_to_string, [(10,10), ('20px', )])

class TestPointsToStringTinyProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='tiny', debug=True)

    def test_valid_points(self):
        # valid units: cm|em|ex|in|mm|pc|pt|px|%
        # dont't know if '%' is valid for points?
        result = points_to_string([(10,10), ('20cm', '20em'), ('30ex', '30in'), ('40mm', '40pc'), ('50pt', '50px'), ('60%', '60%')])
        # it's an unicode string
        self.assertTrue(isinstance(result, unicode))
        self.assertEqual(result, u"10,10 20cm,20em 30ex,30in 40mm,40pc 50pt,50px 60%,60%")

    def test_value_range(self):
        # invalid unit #'p'
        self.assertRaises(ValueError, points_to_string, [(100000,10)])
        self.assertRaises(ValueError, points_to_string, [(-100000,10)])
        self.assertRaises(ValueError, points_to_string, [(10,100000)])
        self.assertRaises(ValueError, points_to_string, [(-10,-100000)])

if __name__=='__main__':
    unittest.main()