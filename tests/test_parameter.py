#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parameter module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.parameter import verify, check_tiny, get_coordinate, _split_coordinate
import svgwrite.parameter as params


class TestVerify(unittest.TestCase):
    """Test verify method"""
    def test_verify(self):
        verify(baseProfile='TINY', debug=False)
        self.assertEqual(params.profile, 'tiny')
        self.assertFalse(params.debug_mode)


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

if __name__=='__main__':
    unittest.main()