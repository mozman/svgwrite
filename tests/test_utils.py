#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.utils import check_tiny, get_coordinate, _split_coordinate, rgb


class TestSplitCoordinate(unittest.TestCase):
    """Test _split_coordinate method"""
    def test_int(self):
        number, unit = _split_coordinate(100)
        self.assertEqual(number, 100)
        self.assertEqual(unit, None)

    def test_float(self):
        number, unit = _split_coordinate(100.)
        self.assertEqual(number, 100.)
        self.assertEqual(unit, None)

    def test_none(self):
        self.assertRaises(TypeError, _split_coordinate, None)

    def test_valid_units(self):
        for value, number, unit in [(' 100px ', 100, 'px'),
                                    (' -100ex ', -100, 'ex'),
                                    (' 100em ', 100, 'em'),
                                    (' -100pt ', -100, 'pt'),
                                    (' 100pc ', 100, 'pc'),
                                    (' 100mm', 100, 'mm'),
                                    (' 100cm', 100, 'cm'),
                                    (' 100in', 100, 'in'),
                                    (' 5%', 5, '%')]:
            number2, unit2 = _split_coordinate(value)
        self.assertEqual(number2, number)
        self.assertEqual(unit2, unit)

    def test_not_valid_numbers(self):
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(ValueError, _split_coordinate, value)

    def test_not_valid_units(self):
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(ValueError, _split_coordinate, value)

class TestGetCoordinate(unittest.TestCase):
    def test_valid_units(self):
        for value, number, unit in [(' 100px ', 100, 'px'),
                                    (' -100ex ', -100, 'ex'),
                                    (' 100em ', 100, 'em'),
                                    (' -100pt ', -100, 'pt'),
                                    (' 100pc ', 100, 'pc'),
                                    (' 100mm', 100, 'mm'),
                                    (' 100cm', 100, 'cm'),
                                    (' 100in', 100, 'in'),
                                    (' 5%', 5, '%')]:
            number2, unit2 = get_coordinate(value)
        self.assertEqual(number2, number)
        self.assertEqual(unit2, unit)

    def test_not_valid_numbers(self):
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(ValueError, get_coordinate, value)

    def test_not_valid_units(self):
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(ValueError, get_coordinate, value)

class TestCheckTiny(unittest.TestCase):
    def test_valid_tiny(self):
        for value in (10000, 0, -10000., -32767.9999, +32767.9999):
            check_tiny(value) # no exception should raised

    def test_invalid_tiny(self):
        for value in (100000, -100000., -32768, 32768):
            self.assertRaises(ValueError, check_tiny, value)

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

if __name__=='__main__':
    unittest.main()