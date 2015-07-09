#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ellipse object
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.shapes import Ellipse

class TestEllipse(unittest.TestCase):
    def test_numbers(self):
        ellipse = Ellipse(center=(0,0), r=(2,1))
        self.assertEqual(ellipse.tostring(), '<ellipse cx="0" cy="0" rx="2" ry="1" />')

    def test_coordinates(self):
        ellipse = Ellipse(center=('1cm','1cm'), r=('2mm', '1mm'))
        self.assertEqual(ellipse.tostring(), '<ellipse cx="1cm" cy="1cm" rx="2mm" ry="1mm" />')

    def test_errors(self):
        self.assertRaises(TypeError, Ellipse, center=1)
        self.assertRaises(TypeError, Ellipse, center=None)
        self.assertRaises(TypeError, Ellipse, center=(None, None))
        self.assertRaises(TypeError, Ellipse, r=1)
        self.assertRaises(TypeError, Ellipse, r=None)
        self.assertRaises(TypeError, Ellipse, r=(None, None))

if __name__=='__main__':
    unittest.main()
