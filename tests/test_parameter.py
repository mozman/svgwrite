#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test parameter module
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.params import Parameter


class TestParameterClass(unittest.TestCase):
    def test_init(self):
        p = Parameter(debug=True, profile='TINY')
        self.assertEqual(p.profile, 'tiny')
        self.assertTrue(p.debug)

    def test_default_values(self):
        p = Parameter()
        self.assertEqual(p.profile, 'full')
        self.assertTrue(p.debug)


if __name__ == '__main__':
    unittest.main()
