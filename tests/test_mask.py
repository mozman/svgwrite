#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test Mask
# Created: 31.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.masking import Mask
from svgwrite.shapes import Circle

class TestMask(unittest.TestCase):
    def test_constructor(self):
        mask = Mask(start=('-10%', '-20%'), size=('120%', '140%'), debug=True, profile='full')
        self.assertEqual(mask.tostring(), '<mask height="140%" width="120%" x="-10%" y="-20%" />')

    def test_add_subelement(self):
        mask = Mask(debug=True, profile='full')
        mask.add(Circle((50,60), 70))
        self.assertEqual(mask.tostring(), '<mask><circle cx="50" cy="60" r="70" /></mask>')

if __name__=='__main__':
    unittest.main()
