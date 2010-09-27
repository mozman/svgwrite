#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.validator import TinyProfileValidator, FullProfileValidator

class TestGetCoordinate(unittest.TestCase):
    def test_valid_units(self):
        validator = TinyProfileValidator()
        for value, number, unit in [(' 100px ', 100, 'px'),
                                    (' -100ex ', -100, 'ex'),
                                    (' 100em ', 100, 'em'),
                                    (' -100pt ', -100, 'pt'),
                                    (' 100pc ', 100, 'pc'),
                                    (' 100mm', 100, 'mm'),
                                    (' 100cm', 100, 'cm'),
                                    (' 100in', 100, 'in'),
                                    (' 5%', 5, '%')]:
            number2, unit2 = validator.get_coordinate(value)
        self.assertEqual(number2, number)
        self.assertEqual(unit2, unit)

    def test_not_valid_numbers(self):
        validator = TinyProfileValidator()
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(ValueError, validator.get_coordinate, value)

    def test_not_valid_units(self):
        validator = TinyProfileValidator()
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(ValueError, validator.get_coordinate, value)

    def test_not_valid_tiny_values(self):
        validator = TinyProfileValidator()
        for value in (100000, '100000', -100000, '-100000'):
            self.assertRaises(ValueError, validator.get_coordinate, value)
        # but valid for full profile - do not raise an error
        validator = FullProfileValidator()
        for value in (100000, '100000', -100000, '-100000'):
            validator.get_coordinate(value)

class TestCheckCoordinate(unittest.TestCase):
    def test_valid_units(self):
        validator = TinyProfileValidator()
        for value, number, unit in [(' 100px ', 100, 'px'),
                                    (' -100ex ', -100, 'ex'),
                                    (' 100em ', 100, 'em'),
                                    (' -100pt ', -100, 'pt'),
                                    (' 100pc ', 100, 'pc'),
                                    (' 100mm', 100, 'mm'),
                                    (' 100cm', 100, 'cm'),
                                    (' 100in', 100, 'in'),
                                    (' 5%', 5, '%')]:
            value2 = validator.check_coordinate(value) # checks also value pass through
            self.assertEqual(value, value2)

    def test_not_valid_numbers(self):
        validator = TinyProfileValidator()
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(ValueError, validator.check_coordinate, value)

    def test_not_valid_units(self):
        validator = TinyProfileValidator()
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(ValueError, validator.check_coordinate, value)

    def test_not_valid_tiny_values(self):
        validator = TinyProfileValidator()
        for value in (100000, '100000', -100000, '-100000'):
            self.assertRaises(ValueError, validator.check_coordinate, value)
        # but valid for full profile - do not raise an error
        validator = FullProfileValidator()
        for value in (100000, '100000', -100000, '-100000'):
            validator.check_coordinate(value)

class TestCheckTiny(unittest.TestCase):
    def test_valid_tiny(self):
        validator = TinyProfileValidator()
        for value in (10000, 0, -10000., -32767.9999, +32767.9999):
            validator.check_tiny(value) # no exception should raised

    def test_invalid_tiny(self):
        validator = TinyProfileValidator()
        for value in (100000, -100000., -32768, 32768):
            self.assertRaises(ValueError, validator.check_tiny, value)

class TestCheckAngle(unittest.TestCase):
    def test_valid_angle(self):
        validator = TinyProfileValidator()
        for value in ('100deg', '0.5grad', '-1.5rad'):
            validator.check_angle(value) # no exception should raised

    def test_invalid_angle(self):
        validator = TinyProfileValidator()
        for value in ('10cm', '-10px', '10in', '1gon', '3°'):
            self.assertRaises(ValueError, validator.check_angle, value)

if __name__=='__main__':
    unittest.main()