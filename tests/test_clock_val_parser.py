#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test clock_val_parser
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

import svgwrite.data.pyparsing as pp
from svgwrite.data.svgparser import _build_clock_val_parser

class TestClockValParser(unittest.TestCase):
    clock_val_parser = _build_clock_val_parser()

    def is_valid(self, value):
        try:
            self.clock_val_parser.parseString(value, parseAll=True)
            return True
        except pp.ParseException:
            return False

    def test_full_clock_values(self):
        self.assertTrue(self.is_valid("02:30:03"))
        self.assertTrue(self.is_valid("50:00:10.25"))

    def test_partial_clock_values(self):
        self.assertTrue(self.is_valid("02:33"))
        self.assertTrue(self.is_valid("00:10.5"))

    def test_time_count_values(self):
        self.assertTrue(self.is_valid("3.2h"))
        self.assertTrue(self.is_valid("45min"))
        self.assertTrue(self.is_valid("30s"))
        self.assertTrue(self.is_valid("5ms"))
        self.assertTrue(self.is_valid("12.467"))

if __name__=='__main__':
    unittest.main()