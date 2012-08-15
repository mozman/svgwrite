#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parsing basic types
# Created: 17.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest
PYTHON3 = sys.version_info[0] > 2

if PYTHON3:
    import svgwrite.data.pyparsing_py3 as pp
else:
    import svgwrite.data.pyparsing_py2 as pp

from svgwrite.data.svgparser import exponent, fractional_constant, \
     scientific_constant, number

class TestBasicTypes(unittest.TestCase):
    def is_valid(self, parser, value):
        try:
            parser.parseString(value, parseAll=True)
            return True
        except pp.ParseException:
            return False

    def test_exponent(self):
        self.assertTrue(self.is_valid(exponent, "e1"))
        self.assertTrue(self.is_valid(exponent, "E1"))
        self.assertTrue(self.is_valid(exponent, "e10"))
        self.assertTrue(self.is_valid(exponent, "E10"))
        self.assertTrue(self.is_valid(exponent, "e-1"))
        self.assertTrue(self.is_valid(exponent, "E-1"))
        self.assertTrue(self.is_valid(exponent, "e-10"))
        self.assertTrue(self.is_valid(exponent, "E-10"))
        self.assertTrue(self.is_valid(exponent, "e+1"))
        self.assertTrue(self.is_valid(exponent, "E+1"))
        self.assertTrue(self.is_valid(exponent, "e+10"))
        self.assertTrue(self.is_valid(exponent, "E+10"))

    def test_exponent_error(self):
        self.assertFalse(self.is_valid(exponent, "e"))
        self.assertFalse(self.is_valid(exponent, "e1."))
        self.assertFalse(self.is_valid(exponent, "e1.0"))

    def test_fractional_constant(self):
        self.assertTrue(self.is_valid(fractional_constant, "1."))
        self.assertTrue(self.is_valid(fractional_constant, "1.0"))
        self.assertTrue(self.is_valid(fractional_constant, ".1"))

    def test_fractional_constant_error(self):
        self.assertFalse(self.is_valid(fractional_constant, "1"), "missing '.' is not valid")
        self.assertFalse(self.is_valid(fractional_constant, "-1.0"), "a sign is not valid")
        self.assertFalse(self.is_valid(fractional_constant, "+1.0"), "a sign is not valid")
        self.assertFalse(self.is_valid(fractional_constant, "1.0.0"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(fractional_constant, "1..0"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(fractional_constant, "."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(fractional_constant, "-."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(fractional_constant, "+."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(fractional_constant, "1,0"), "',' is not valid comma")

    def test_scientific_constant(self):
        self.assertTrue(self.is_valid(scientific_constant, "3.1415"))
        self.assertTrue(self.is_valid(scientific_constant, "3.1415e10"))
        self.assertTrue(self.is_valid(scientific_constant, "3.1415e-10"))
        self.assertTrue(self.is_valid(scientific_constant, "3.1415e+10"))

    def test_scientific_constant_error(self):
        self.assertFalse(self.is_valid(scientific_constant, "-3.1415"), "leading sign is not valid")
        self.assertFalse(self.is_valid(scientific_constant, "+3.1415"), "leading sign is not valid")
        self.assertFalse(self.is_valid(scientific_constant, "1.0.0e10"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(scientific_constant, "1..0e10"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(scientific_constant, "."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(scientific_constant, "-."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(scientific_constant, "+."), "only a '.' are not valid")

    def test_number(self):
        self.assertTrue(self.is_valid(number, "3.1415"))
        self.assertTrue(self.is_valid(number, "3."))
        self.assertTrue(self.is_valid(number, "3.e10"))
        self.assertTrue(self.is_valid(number, ".1415"))
        self.assertTrue(self.is_valid(number, "-.1415"))
        self.assertTrue(self.is_valid(number, ".1415e10"))
        self.assertTrue(self.is_valid(number, "-.1415e10"))
        self.assertTrue(self.is_valid(number, "-3.1415"))
        self.assertTrue(self.is_valid(number, "+3.1415"))

        self.assertTrue(self.is_valid(number, "3.1415e10"))
        self.assertTrue(self.is_valid(number, "-3.1415e10"))
        self.assertTrue(self.is_valid(number, "-3.e10"))
        self.assertTrue(self.is_valid(number, "-.1415e10"))
        self.assertTrue(self.is_valid(number, "+3.1415e10"))
        self.assertTrue(self.is_valid(number, "+.1415e10"))

        self.assertTrue(self.is_valid(number, "3.1415e-10"))
        self.assertTrue(self.is_valid(number, "-3.1415e-10"))
        self.assertTrue(self.is_valid(number, "+3.1415e-10"))
        self.assertTrue(self.is_valid(number, "3.1415e+10"))
        self.assertTrue(self.is_valid(number, "-3.1415e+10"))
        self.assertTrue(self.is_valid(number, "+3.1415e+10"))

        self.assertTrue(self.is_valid(number, "31415e+10"))
        self.assertTrue(self.is_valid(number, "-31415e+10"))
        self.assertTrue(self.is_valid(number, "+31415e+10"))

    def test_number_error(self):
        self.assertFalse(self.is_valid(number, "1.0.0e10"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(number, "1..0e10"), "two or more '.' are not valid")
        self.assertFalse(self.is_valid(number, "."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(number, "-."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(number, "+."), "only a '.' are not valid")
        self.assertFalse(self.is_valid(number, "1.0e1-0"), "exponent 'e1-0' is not valid")
        self.assertFalse(self.is_valid(number, "1.0e1+0"), "exponent 'e1+0' is not valid")
        self.assertFalse(self.is_valid(number, "1.0e1.0"), "exponent 'e1.0' is not valid")
        self.assertFalse(self.is_valid(number, "1.0e"), "only 'e' is not valid")
        self.assertFalse(self.is_valid(number, "e10"), "only an exponent is not valid")

if __name__=='__main__':
    unittest.main()
