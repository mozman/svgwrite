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


class TestInit(unittest.TestCase):
    """Test init method"""
    def test_init(self):
        parameter.set_debug()
        parameter.set_profile('TINY')
        self.assertEqual(parameter.profile, 'tiny')
        self.assertTrue(parameter.debug)


if __name__=='__main__':
    unittest.main()