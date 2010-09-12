#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parameter module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

import svgwrite.parameter as parameter


class TestInit(unittest.TestCase):
    """Test init method"""
    def test_init(self):
        parameter.init(baseProfile='TINY', debug=True)
        self.assertEqual(parameter.profile, 'tiny')
        self.assertTrue(parameter.debug_mode)


if __name__=='__main__':
    unittest.main()