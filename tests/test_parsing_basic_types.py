#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parsing basic types
# Created: 17.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.data.svgparser import is_valid, exponent, number

is_valid_exponent = is_valid(exponent)
is_valid_number = is_valid(number)

class TestBasicTypes(unittest.TestCase):

    def test_exponent(self):
        self.assertTrue(is_valid_exponent("e1"))
        self.assertTrue(is_valid_exponent("E1"))
        self.assertTrue(is_valid_exponent("e10"))
        self.assertTrue(is_valid_exponent("E10"))
        self.assertTrue(is_valid_exponent("e-1"))
        self.assertTrue(is_valid_exponent("E-1"))
        self.assertTrue(is_valid_exponent("e-10"))
        self.assertTrue(is_valid_exponent("E-10"))
        self.assertTrue(is_valid_exponent("e+1"))
        self.assertTrue(is_valid_exponent("E+1"))
        self.assertTrue(is_valid_exponent("e+10"))
        self.assertTrue(is_valid_exponent("E+10"))

    def test_exponent_error(self):
        self.assertFalse(is_valid_exponent("e"))
        self.assertFalse(is_valid_exponent("e1."))
        self.assertFalse(is_valid_exponent("e1.0"))

    def test_fractional_constant(self):
        self.assertTrue(is_valid_number("1."))
        self.assertTrue(is_valid_number("1.0"))
        self.assertTrue(is_valid_number(".1"))

    def test_fractional_constant_error(self):
        #self.assertFalse(is_valid_number("1"), "missing '.' is not valid")
        #self.assertFalse(is_valid_number("-1.0"), "a sign is not valid")
        #self.assertFalse(is_valid_number("+1.0"), "a sign is not valid")
        self.assertFalse(is_valid_number("1.0.0"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("1..0"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("-."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("+."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("1,0"), "',' is not valid comma")

    def test_scientific_constant(self):
        self.assertTrue(is_valid_number("3.1415"))
        self.assertTrue(is_valid_number("3.1415e10"))
        self.assertTrue(is_valid_number("3.1415e-10"))
        self.assertTrue(is_valid_number("3.1415e+10"))

    def test_scientific_constant_error(self):
        #self.assertFalse(is_valid_number("-3.1415"), "leading sign is not valid")
        #self.assertFalse(is_valid_number("+3.1415"), "leading sign is not valid")
        self.assertFalse(is_valid_number("1.0.0e10"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("1..0e10"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("-."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("+."), "only a '.' are not valid")

    def test_number(self):
        self.assertTrue(is_valid_number("3.1415"))
        self.assertTrue(is_valid_number("3."))
        self.assertTrue(is_valid_number("3.e10"))
        self.assertTrue(is_valid_number(".1415"))
        self.assertTrue(is_valid_number("-.1415"))
        self.assertTrue(is_valid_number(".1415e10"))
        self.assertTrue(is_valid_number("-.1415e10"))
        self.assertTrue(is_valid_number("-3.1415"))
        self.assertTrue(is_valid_number("+3.1415"))

        self.assertTrue(is_valid_number("3.1415e10"))
        self.assertTrue(is_valid_number("-3.1415e10"))
        self.assertTrue(is_valid_number("-3.e10"))
        self.assertTrue(is_valid_number("-.1415e10"))
        self.assertTrue(is_valid_number("+3.1415e10"))
        self.assertTrue(is_valid_number("+.1415e10"))

        self.assertTrue(is_valid_number("3.1415e-10"))
        self.assertTrue(is_valid_number("-3.1415e-10"))
        self.assertTrue(is_valid_number("+3.1415e-10"))
        self.assertTrue(is_valid_number("3.1415e+10"))
        self.assertTrue(is_valid_number("-3.1415e+10"))
        self.assertTrue(is_valid_number("+3.1415e+10"))

        self.assertTrue(is_valid_number("31415e+10"))
        self.assertTrue(is_valid_number("-31415e+10"))
        self.assertTrue(is_valid_number("+31415e+10"))

    def test_number_error(self):
        self.assertFalse(is_valid_number("1.0.0e10"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("1..0e10"), "two or more '.' are not valid")
        self.assertFalse(is_valid_number("."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("-."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("+."), "only a '.' are not valid")
        self.assertFalse(is_valid_number("1.0e1-0"), "exponent 'e1-0' is not valid")
        self.assertFalse(is_valid_number("1.0e1+0"), "exponent 'e1+0' is not valid")
        self.assertFalse(is_valid_number("1.0e1.0"), "exponent 'e1.0' is not valid")
        self.assertFalse(is_valid_number("1.0e"), "only 'e' is not valid")
        self.assertFalse(is_valid_number("e10"), "only an exponent is not valid")

if __name__=='__main__':
    unittest.main()
