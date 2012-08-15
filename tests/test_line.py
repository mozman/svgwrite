#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test line object
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.shapes import Line

class TestLine(unittest.TestCase):
    def test_numbers(self):
        line = Line(start=(0,0), end=(10,20))
        self.assertEqual(line.tostring(), '<line x1="0" x2="10" y1="0" y2="20" />')

    def test_coordinates(self):
        line = Line(start=('10cm','11cm'), end=('20cm', '30cm'))
        self.assertEqual(line.tostring(), '<line x1="10cm" x2="20cm" y1="11cm" y2="30cm" />')

    def test_errors(self):
        self.assertRaises(TypeError, Line, start=1)
        self.assertRaises(TypeError, Line, end=1)
        self.assertRaises(TypeError, Line, start=None)
        self.assertRaises(TypeError, Line, end=None)
        self.assertRaises(TypeError, Line, end=(None, None))
        self.assertRaises(TypeError, Line, start=(None, None))

if __name__=='__main__':
    unittest.main()
