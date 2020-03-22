#!/usr/bin/env python
# coding:utf-8
# Author:  mozman <me@mozman.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (c) 2010-2020, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.utils import rgb, AutoID, get_unit
from svgwrite.utils import strlist, rect_top_left_corner
from svgwrite.utils import split_angle, split_coordinate
from svgwrite import cm


class TestRgb(unittest.TestCase):
    def test_rgb_8bit(self):
        self.assertEqual(rgb(128, 128, 128), "rgb(128,128,128)")
        self.assertEqual(rgb(), "rgb(0,0,0)")
        # value overflow
        self.assertEqual(rgb(256, 256, 256), "rgb(0,0,0)")
        self.assertEqual(rgb(257, 257, 257), "rgb(1,1,1)")

    def test_rgb_percent(self):
        self.assertEqual(rgb(50, 50, 50, '%'), "rgb(50%,50%,50%)")
        self.assertEqual(rgb(mode='%'), "rgb(0%,0%,0%)")
        # value overflow
        self.assertEqual(rgb(101, -1, 101, '%'), "rgb(100%,0%,100%)")

    def test_rgb_invalid_mode(self):
        self.assertRaises(ValueError, rgb, mode='$')


class TestStrList(unittest.TestCase):
    def test_basic_types(self):
        self.assertEqual(strlist([1, 2, 3]), "1,2,3")
        self.assertEqual(strlist([1, None, 3]), "1,3")
        self.assertEqual(strlist([1, 2, None]), "1,2")

    def test_seperator(self):
        self.assertEqual(strlist([1, 2, 3], ' '), "1 2 3")
        self.assertEqual(strlist([1, None, 3], ';'), "1;3")
        self.assertEqual(strlist([1, 2, None], ':'), "1:2")

    def test_list(self):
        self.assertEqual(strlist([(5, 'abc', None), (1, 2, None)]), "5,abc,1,2")
        self.assertEqual(strlist([(1, None, 3), 4]), "1,3,4")

    def test_string(self):
        self.assertEqual(strlist("5,abc,1,2"), "5,abc,1,2")


class TestRectTopLeftCorner(unittest.TestCase):
    def test_top_left(self):
        res = rect_top_left_corner(insert=(10, 10), size=(10, 10))
        self.assertEqual(res, (10, 10))

    def test_top_center(self):
        res = rect_top_left_corner(insert=(10, 10), size=(10, 10), pos='top-center')
        self.assertEqual(res, (5, 10))

    def test_top_right(self):
        res = rect_top_left_corner(insert=(10, 10), size=(10, 10), pos='top-right')
        self.assertEqual(res, (0, 10))

    def test_middle_center(self):
        res = rect_top_left_corner(insert=(10, 10), size=(10, 10), pos='middle-center')
        self.assertEqual(res, (5, 5))

    def test_bottom_center(self):
        res = rect_top_left_corner(insert=(10, 10), size=(10, 10), pos='bottom-center')
        self.assertEqual(res, (5, 0))

    def test_valid_units(self):
        res = rect_top_left_corner(insert=('10mm', '10mm'), size=('10mm', '10mm'), pos='middle-center')
        # numbers converted to floats
        self.assertEqual(res, ('5.0mm', '5.0mm'))
        res = rect_top_left_corner(insert=('10in', '10in'), size=('10in', '10in'), pos='bottom-center')
        self.assertEqual(res, ('5.0in', '0.0in'))

    def test_invalid_units(self):
        # insert and size has to have the same units
        self.assertRaises(ValueError, rect_top_left_corner, insert=('10cm', '10cm'), size=(10, 10), pos='middle-center')
        self.assertRaises(ValueError, rect_top_left_corner, insert=('10mm', '10mm'), size=('10cm', '10cm'),
                          pos='middle-center')
        self.assertRaises(ValueError, rect_top_left_corner, insert=('10mm', '10mm'), size=('10mm', '10cm'),
                          pos='middle-center')

    def test_invalid_pos(self):
        # insert and size has to have the same units
        self.assertRaises(ValueError, rect_top_left_corner, insert=(1, 1), size=(1, 1), pos='middle-mitte')
        self.assertRaises(ValueError, rect_top_left_corner, insert=(1, 1), size=(1, 1), pos='mitte-center')


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
        self.assertRaises(ValueError, split_angle, '100km')
        self.assertRaises(ValueError, split_angle, '100ccm')
        self.assertRaises(ValueError, split_angle, '10,0deg')
        self.assertRaises(ValueError, split_angle, '1.0.0deg')


class TestAutoID(unittest.TestCase):
    def test_next_id(self):
        getter = AutoID(1)
        self.assertEqual('id1', getter.next_id())
        getter = AutoID()
        self.assertEqual('id2', getter.next_id())
        self.assertEqual('id3', AutoID.next_id())

    def test_set_next_id(self):
        # getter = AutoID()
        self.assertEqual('id7', AutoID.next_id(7))
        self.assertEqual('id8', AutoID.next_id())


class TestGetUnit(unittest.TestCase):
    def test_number(self):
        self.assertEqual(None, get_unit(1))
        self.assertEqual(None, get_unit(1.0))

    def test_valid_units(self):
        self.assertEqual('cm', get_unit('1cm'))
        self.assertEqual('mm', get_unit('3.1415mm'))
        self.assertEqual('%', get_unit('300%'))

    def test_invalid_units(self):
        self.assertRaises(ValueError, get_unit, '1m')


class TestUnit(unittest.TestCase):
    def test_cm(self):
        self.assertEqual('5cm', 5 * cm)

    def test_call_cm(self):
        self.assertEqual('5cm,7cm', cm(5, 7))


if __name__ == '__main__':
    unittest.main()
