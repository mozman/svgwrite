#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test animation_timing_parser
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.data.svgparser import is_valid_animation_timing

class TestAnimationTimingParser(unittest.TestCase):
    def test_offset_value(self):
        self.assertTrue(is_valid_animation_timing("+5min"))
        self.assertTrue(is_valid_animation_timing("-5s"))
        self.assertTrue(is_valid_animation_timing("1s"))
        self.assertTrue(is_valid_animation_timing("0.1s"))

    def test_syncbase_value(self):
        self.assertTrue(is_valid_animation_timing("#001.begin+5min"))
        self.assertTrue(is_valid_animation_timing("#001.end-5min"))
        self.assertTrue(is_valid_animation_timing("#0A1.begin"))
        self.assertTrue(is_valid_animation_timing("#0A1.end"))

    def test_event_value(self):
        # Id-Value does not start with '#'
        self.assertTrue(is_valid_animation_timing("shape.click+5min"))
        # Id-Value starts with '#'
        self.assertTrue(is_valid_animation_timing("#001.click+5min"))
        self.assertTrue(is_valid_animation_timing("#001.mouseover-5min"))
        self.assertTrue(is_valid_animation_timing("mouseup-5min"))
        self.assertTrue(is_valid_animation_timing("mousedown+5min"))
        self.assertTrue(is_valid_animation_timing("mouseout"))
        self.assertTrue(is_valid_animation_timing("focusout"))
        self.assertTrue(is_valid_animation_timing("focusin"))

    def test_repeat_value(self):
        self.assertTrue(is_valid_animation_timing("#001.repeat(1)+5min"))
        self.assertTrue(is_valid_animation_timing("repeat(1)-5min"))

    def test_accessKey_value(self):
        self.assertTrue(is_valid_animation_timing("accessKey(a)+5min"))
        self.assertTrue(is_valid_animation_timing("accessKey(Z)-5min"))
        self.assertTrue(is_valid_animation_timing("accessKey(a)"))
        self.assertTrue(is_valid_animation_timing("accessKey(Z)"))

    def test_wallclock(self):
        self.assertTrue(is_valid_animation_timing("wallclock(1997-07-16T19:20:30.45+01:00)"))
        self.assertTrue(is_valid_animation_timing("wallclock(1997-07-16T19:20:30+01:00)"))
        self.assertTrue(is_valid_animation_timing("wallclock(1997-07-16T19:20:30)"))
        self.assertTrue(is_valid_animation_timing("wallclock(1997-07-16T19:20)"))

    def test_invalid_value(self):
        self.assertFalse(is_valid_animation_timing("xyz"))
        self.assertFalse(is_valid_animation_timing("repeat(0"))
        self.assertFalse(is_valid_animation_timing("repeat0)"))
        self.assertFalse(is_valid_animation_timing("accessKeya)"))
        self.assertFalse(is_valid_animation_timing("accessKey(Z"))
        self.assertFalse(is_valid_animation_timing("001sec"))
        self.assertFalse(is_valid_animation_timing("wallclock(1997-07-16T19:2)"))
        self.assertFalse(is_valid_animation_timing("wallclock(1997-07-16T19:)"))
        self.assertFalse(is_valid_animation_timing("wallclock(1997-07-16T19)"))

if __name__ == '__main__':
    unittest.main()
