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


class TestSetup(unittest.TestCase):
    """Test setup method"""
    def test_setup(self):
        parameter.setup(baseProfile='TINY', debug=False)
        self.assertEqual(parameter.profile, 'tiny')
        self.assertFalse(parameter.debug_mode)


if __name__=='__main__':
    unittest.main()