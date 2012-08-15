#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test tiny12 typechecker
# Created: 08.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.data.typechecker import Tiny12TypeChecker

class TestTiny12TypeChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Tiny12TypeChecker()

    def test_is_bool(self):
        self.assertTrue(self.checker.is_boolean(True))
        self.assertTrue(self.checker.is_boolean(False))
        self.assertTrue(self.checker.is_boolean(' true '))
        self.assertTrue(self.checker.is_boolean(' false '))
        self.assertTrue(self.checker.is_boolean('True'))
        self.assertTrue(self.checker.is_boolean('False'))
    def test_is_not_bool(self):
        self.assertFalse(self.checker.is_boolean(1))
        self.assertFalse(self.checker.is_boolean(0))
        self.assertFalse(self.checker.is_boolean((1, 1)))
        self.assertFalse(self.checker.is_boolean(dict(a=1, b=1)))

    def test_is_number(self):
        """ Integer and Float, also as String '100' or '3.1415'. """
        # big numbers only valid for full profile
        self.assertTrue(self.checker.is_number(10000))
        self.assertTrue(self.checker.is_number(-10000))
        self.assertTrue(self.checker.is_number(3.141592))
        self.assertTrue(self.checker.is_number('10000'))
        self.assertTrue(self.checker.is_number('-10000'))
        self.assertTrue(self.checker.is_number('3.141592'))
    def test_is_not_number(self):
        self.assertFalse(self.checker.is_number( (1,2) ))
        self.assertFalse(self.checker.is_number('manfred'))
        self.assertFalse(self.checker.is_number( dict(a=1, b=2) ))
        self.assertFalse(self.checker.is_number(100000))
        self.assertFalse(self.checker.is_number(-100000))
        self.assertFalse(self.checker.is_number('100000'))
        self.assertFalse(self.checker.is_number('-100000'))

    def test_is_focus(self):
        for focus in  [' nav-next ', ' nav-prev ', ' nav-up ', ' nav-down ',
                       ' nav-left ', ' nav-right ', ' nav-up-left ', ' nav-up-right ',
                       'nav-down-left', 'nav-down-right']:
            self.assertTrue(self.checker.is_focus(focus))
    def test_is_not_focus(self):
        self.assertFalse(self.checker.is_focus('mozman'))
        self.assertFalse(self.checker.is_focus(1))
        self.assertFalse(self.checker.is_focus((1,1)))

if __name__=='__main__':
    unittest.main()
