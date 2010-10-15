#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parameter module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import parameter
from svgwrite.params import Parameter

parameter = Parameter()

class TestGlobalVariable(unittest.TestCase):
    """Test init method"""
    def test_init(self):
        parameter.set_debug(True)
        parameter.set_profile('TINY')
        self.assertEqual(parameter.get_profile(), 'tiny')
        self.assertTrue(parameter.debug)

    def test_get_auto_id(self):
        parameter._set_auto_id(9) # only for testing !!!
        self.assertEqual(parameter.get_auto_id(), "id9")
        self.assertEqual(parameter.get_auto_id(), "id10")
        self.assertEqual(parameter.get_auto_id(), "id11")

class testParameterClass(unittest.TestCase):
    def test_init(self):
        p = Parameter(debug=True, profile='TINY')
        self.assertEqual(p.get_profile(), 'tiny')
        self.assertTrue(p.debug)

    def test_get_auto_id(self):
        p = Parameter(debug=False)
        p._set_auto_id(9) # only for testing !!!
        self.assertEqual(parameter.get_auto_id(), "id9")
        p2 = Parameter(debug=False)
        self.assertEqual(parameter.get_auto_id(), "id10")
        p3 = Parameter(debug=False)
        self.assertEqual(parameter.get_auto_id(), "id11")


if __name__=='__main__':
    unittest.main()