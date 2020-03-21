#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test clock_val_parser
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.data.svgparser import is_valid, clock_val_re, wall_clock_val_re

clock_val_parser = is_valid(clock_val_re())
wallclock_parser = is_valid(wall_clock_val_re())

class TestClockValParser(unittest.TestCase):

    def is_valid(self, value):
        return clock_val_parser(value)

    def test_full_clock_values(self):
        self.assertTrue(self.is_valid("02:30:03"))
        self.assertTrue(self.is_valid("01:00:00"))
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

class TestWallClockValParser(unittest.TestCase):

    def is_valid(self, value):
        return wallclock_parser(value)

    def test_date_plus_hhmm(self):
        # Complete date plus hours and minutes:
        # YYYY-MM-DDThh:mmTZD (e.g. 1997-07-16T19:20+01:00)
        self.assertTrue(self.is_valid("1997-07-16T19:20+01:00"))

    def test_date_plus_hhmmss(self):
        # Complete date plus hours, minutes and seconds:
        # YYYY-MM-DDThh:mm:ssTZD (e.g. 1997-07-16T19:20:30+01:00)
        self.assertTrue(self.is_valid("1997-07-16T19:20:30+01:00"))

    def test_date_plus_hhmmss_frac(self):
        # Complete date plus hours, minutes, seconds and a decimal fraction of a second
        # YYYY-MM-DDThh:mm:ss.sTZD (e.g. 1997-07-16T19:20:30.45+01:00)
        self.assertTrue(self.is_valid("1997-07-16T19:20:30.45+01:00"))



if __name__=='__main__':
    unittest.main()
