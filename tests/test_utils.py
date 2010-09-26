#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import parameter
from svgwrite.utils import rgb, value_to_string, points_to_string
from svgwrite.utils import strlist, rect_top_left_corner
from svgwrite.utils import split_angle, split_coordinate

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
        parameter.set_debug()
        parameter.set_profile('full')
        self.assertEqual(u'test', value_to_string('test'))
        self.assertEqual(u'10', value_to_string(10))

    def test_tiny_profile(self):
        parameter.set_debug()
        parameter.set_profile('tiny')
        # value out of range
        self.assertRaises(ValueError, value_to_string, 100000)

    def test_is_unicode(self):
        self.assertTrue(isinstance(value_to_string(10), unicode))
        self.assertTrue(isinstance(value_to_string('test'), unicode))

class TestPointsToStringFullProfile(unittest.TestCase):
    def setUp(self):
        parameter.set_debug()
        parameter.set_profile('full')

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
        parameter.set_debug()
        parameter.set_profile('tiny')

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

class TestStrList(unittest.TestCase):
    def test_basic_types(self):
        self.assertEqual(strlist([1,2,3]), "1,2,3" )
        self.assertEqual(strlist([1,None,3]), "1,3")
        self.assertEqual(strlist([1,2,None]), "1,2")

    def test_seperator(self):
        self.assertEqual(strlist([1,2,3], ' '), "1 2 3" )
        self.assertEqual(strlist([1,None,3], ';'), "1;3")
        self.assertEqual(strlist([1,2,None], ':'), "1:2")

    def test_list(self):
        self.assertEqual(strlist( [(5, 'abc', None), (1, 2, None)] ), "5,abc,1,2")
        self.assertEqual(strlist( [(1,None,3), 4]), "1,3,4")

class TestRectTopLeftCorner(unittest.TestCase):
    def test_top_left(self):
        res = rect_top_left_corner(insert=(10,10), size=(10,10))
        self.assertEqual(res, (10,10))

    def test_top_center(self):
        res = rect_top_left_corner(insert=(10,10), size=(10,10), pos='top-center')
        self.assertEqual(res, (5,10))

    def test_top_right(self):
        res = rect_top_left_corner(insert=(10,10), size=(10,10), pos='top-right')
        self.assertEqual(res, (0,10))

    def test_middle_center(self):
        res = rect_top_left_corner(insert=(10,10), size=(10,10), pos='middle-center')
        self.assertEqual(res, (5,5))

    def test_bottom_center(self):
        res = rect_top_left_corner(insert=(10,10), size=(10,10), pos='bottom-center')
        self.assertEqual(res, (5,0))

    def test_valid_units(self):
        res = rect_top_left_corner(insert=('10mm','10mm'), size=('10mm','10mm'), pos='middle-center')
        # numbers converted to floats
        self.assertEqual(res, ('5.0mm','5.0mm'))
        res = rect_top_left_corner(insert=('10in','10in'), size=('10in','10in'), pos='bottom-center')
        self.assertEqual(res, ('5.0in','0.0in'))

    def test_ivalid_units(self):
        # insert and size has to have the same units
        self.assertRaises(ValueError, rect_top_left_corner, insert=('10cm','10cm'), size=(10,10), pos='middle-center')
        self.assertRaises(ValueError, rect_top_left_corner, insert=('10mm','10mm'), size=('10cm','10cm'), pos='middle-center')

class TestSplitCoordinate(unittest.TestCase):
    def test_int_coordinates(self):
        res = split_coordinate(10)
        self.assertEqual(res, (10, None))

    def test_float_coordinates(self):
        res = split_coordinate(7.9)
        self.assertEqual(res, (7.9, None))

    def test_valid_str_coordinates(self):
        res = split_coordinate('10cm')
        self.assertEqual(res, (10, 'cm'))
        res = split_coordinate('10.7in')
        self.assertEqual(res, (10.7, 'in'))

    def test_invalid_str_coordinates(self):
        self.assertRaises(ValueError, split_coordinate, '100km')
        self.assertRaises(ValueError, split_coordinate, '100ccm')
        self.assertRaises(ValueError, split_coordinate, '10,0cm')
        self.assertRaises(ValueError, split_coordinate, '1.0.0cm')

class TestSplitAngle(unittest.TestCase):
    def test_int_angle(self):
        res = split_angle(10)
        self.assertEqual(res, (10, None))

    def test_float_angle(self):
        res = split_angle(7.9)
        self.assertEqual(res, (7.9, None))

    def test_valid_str_angle(self):
        res = split_angle('10deg')
        self.assertEqual(res, (10, 'deg'))
        res = split_angle('10.7rad')
        self.assertEqual(res, (10.7, 'rad'))
        res = split_angle('10.7grad')
        self.assertEqual(res, (10.7, 'grad'))

    def test_invalid_str_angle(self):
        self.assertRaises(ValueError, split_coordinate, '100km')
        self.assertRaises(ValueError, split_coordinate, '100ccm')
        self.assertRaises(ValueError, split_coordinate, '10,0deg')
        self.assertRaises(ValueError, split_coordinate, '1.0.0deg')

if __name__=='__main__':
    unittest.main()