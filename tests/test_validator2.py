#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test utils module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.validator2 import get_validator

class TestGetCoordinate(unittest.TestCase):
    def test_invalid_profile(self):
        self.assertRaises(ValueError, get_validator, profile='invalid')

    def test_get_none_coordinate(self):
        validator = get_validator('tiny', debug=True)
        self.assertRaises(TypeError, validator.get_coordinate, None)

    def test_valid_units(self):
        validator = get_validator('tiny', debug=True)
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
        validator = get_validator('tiny', debug=True)
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(ValueError, validator.get_coordinate, value)
            self.assertRaises(ValueError, validator.get_length, value)

    def test_not_valid_units(self):
        validator = get_validator('tiny', debug=True)
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(ValueError, validator.get_coordinate, value)

    def test_not_valid_tiny_values(self):
        validator = get_validator('tiny', debug=True)
        for value in (100000, '100000', -100000, '-100000'):
            self.assertRaises(ValueError, validator.get_coordinate, value)
        # but valid for full profile - do not raise an error
        validator = get_validator('full', debug=True)
        for value in (100000, '100000', -100000, '-100000'):
            validator.get_coordinate(value)

    def test_valid_elementname(self):
        validator = get_validator('full', debug=True)
        self.assertTrue(validator.is_valid_elementname('text'))

    def test_invalid_elementname(self):
        validator = get_validator('full', debug=True)
        self.assertFalse(validator.is_valid_elementname('textArea'))

    def test_valid_children(self):
        validator = get_validator('full', debug=True)
        self.assertTrue(validator.is_valid_children('text', 'tspan'))

    def test_invalid_children(self):
        validator = get_validator('full', debug=True)
        self.assertFalse(validator.is_valid_children('text', 'line'))

    def test_check_invalid_children(self):
        validator = get_validator('full', debug=True)
        self.assertRaises(ValueError, validator.check_valid_children, 'text', 'line')

class TestCheckCoordinate(unittest.TestCase):
    def test_valid_units(self):
        validator = get_validator('tiny', debug=True)
        for value, number, unit in [(' 100px ', 100, 'px'),
                                    (' -100ex ', -100, 'ex'),
                                    (' 100em ', 100, 'em'),
                                    (' -100pt ', -100, 'pt'),
                                    (' 100pc ', 100, 'pc'),
                                    (' 100mm', 100, 'mm'),
                                    (' 100cm', 100, 'cm'),
                                    (' 100in', 100, 'in'),
                                    (' 5%', 5, '%')]:
            value2 = validator.check_svg_type(value, 'coordinate') # checks also value pass through
            self.assertEqual(value, value2)

    def test_not_valid_numbers(self):
        validator = get_validator('tiny', debug=True)
        for value in (' 1s00in ', ' 1s00mm ', ' 1s00% '):
            self.assertRaises(TypeError, validator.check_svg_type, value, 'coordinate')

    def test_not_valid_units(self):
        validator = get_validator('tiny', debug=True)
        for value in (' 100km ', ' 100mi ', ' 100$ '):
            self.assertRaises(TypeError, validator.check_svg_type, value, 'coordinate')

    def test_not_valid_tiny_values(self):
        validator = get_validator('tiny', debug=True)
        for value in (100000, '100000', -100000, '-100000'):
            self.assertRaises(TypeError, validator.check_svg_type, value, 'coordinate')
        # but valid for full profile - do not raise an error
        validator = get_validator('full', debug=True)
        for value in (100000, '100000', -100000, '-100000'):
            validator.check_svg_type(value, 'coordinate')

class TestCheckTiny(unittest.TestCase):
    def test_valid_tiny(self):
        validator = get_validator('tiny', debug=True)
        for value in (10000, 0, -10000., -32767.9999, +32767.9999):
            validator.check_svg_type(value, 'number') # no exception should raised

    def test_invalid_tiny(self):
        validator = get_validator('tiny', debug=True)
        for value in (100000, -100000., -32768, 32768):
            self.assertRaises(TypeError, validator.check_svg_type, value, 'number')

class TestCheckAngle(unittest.TestCase):
    def test_valid_angle(self):
        validator = get_validator('tiny', debug=True)
        for value in ('100deg', '0.5grad', '-1.5rad'):
            validator.check_svg_type(value, 'angle') # no exception should raised

    def test_invalid_angle(self):
        validator = get_validator('tiny', debug=True)
        for value in ('10cm', '-10px', '10in', '1gon', '3°'):
            self.assertRaises(TypeError, validator.check_svg_type, value, 'angle')

if __name__=='__main__':
    unittest.main()
