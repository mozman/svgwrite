#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test circle object
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.shapes import Circle

class TestCircle(unittest.TestCase):
    def test_numbers(self):
        circle = Circle(center=(0,0), r=2)
        self.assertEqual(circle.tostring(), '<circle cx="0" cy="0" r="2" />')

    def test_coordinates(self):
        circle = Circle(center=('1cm','1cm'), r='2mm')
        self.assertEqual(circle.tostring(), '<circle cx="1cm" cy="1cm" r="2mm" />')

    def test_errors(self):
        self.assertRaises(TypeError, Circle, center=1)
        self.assertRaises(TypeError, Circle, r=None)
        self.assertRaises(TypeError, Circle, center=None)
        self.assertRaises(TypeError, Circle, center=(None, None))

if __name__=='__main__':
    unittest.main()
