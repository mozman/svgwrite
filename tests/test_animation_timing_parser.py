#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test animation_timing_parser
# Created: 03.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.data.svgparser import AnimationTimingParser

class TestAnimationTimingParser(unittest.TestCase):
    def test_offset_value(self):
        self.assertTrue(AnimationTimingParser.is_valid("+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("-5s"))

    def test_syncbase_value(self):
        self.assertTrue(AnimationTimingParser.is_valid("#001.begin+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("#001.end-5min"))
        self.assertTrue(AnimationTimingParser.is_valid("#0A1.begin"))
        self.assertTrue(AnimationTimingParser.is_valid("#0A1.end"))

    def test_event_value(self):
        self.assertTrue(AnimationTimingParser.is_valid("#001.click+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("#001.mouseover-5min"))
        self.assertTrue(AnimationTimingParser.is_valid("mouseup-5min"))
        self.assertTrue(AnimationTimingParser.is_valid("mousedown+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("mouseout"))
        self.assertTrue(AnimationTimingParser.is_valid("focusout"))
        self.assertTrue(AnimationTimingParser.is_valid("focusin"))

    def test_repeat_value(self):
        self.assertTrue(AnimationTimingParser.is_valid("#001.repeat(1)+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("repeat(1)-5min"))

    def test_accessKey_value(self):
        self.assertTrue(AnimationTimingParser.is_valid("accessKey(a)+5min"))
        self.assertTrue(AnimationTimingParser.is_valid("accessKey(Z)-5min"))
        self.assertTrue(AnimationTimingParser.is_valid("accessKey(a)"))
        self.assertTrue(AnimationTimingParser.is_valid("accessKey(Z)"))

    def test_wallclock(self):
        self.assertTrue(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:20:30.45+01:00)"))
        self.assertTrue(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:20:30+01:00)"))
        self.assertTrue(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:20:30)"))
        self.assertTrue(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:20)"))

    def test_invalid_value(self):
        self.assertFalse(AnimationTimingParser.is_valid("xyz"))
        self.assertFalse(AnimationTimingParser.is_valid("repeat(0"))
        self.assertFalse(AnimationTimingParser.is_valid("repeat0)"))
        self.assertFalse(AnimationTimingParser.is_valid("accessKeya)"))
        self.assertFalse(AnimationTimingParser.is_valid("accessKey(Z"))
        self.assertFalse(AnimationTimingParser.is_valid("001"))
        self.assertFalse(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:2)"))
        self.assertFalse(AnimationTimingParser.is_valid("wallclock(1997-07-16T19:)"))
        self.assertFalse(AnimationTimingParser.is_valid("wallclock(1997-07-16T19)"))

if __name__=='__main__':
    unittest.main()
