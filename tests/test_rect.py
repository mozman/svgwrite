#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test rect object
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.shapes import Rect

class TestRect(unittest.TestCase):
    def test_numbers(self):
        rect = Rect(insert=(0,0), size=(10,20))
        self.assertEqual(rect.tostring(), '<rect height="20" width="10" x="0" y="0" />')

    def test_coordinates(self):
        rect = Rect(insert=('10cm','11cm'), size=('20cm', '30cm'))
        self.assertEqual(rect.tostring(), '<rect height="30cm" width="20cm" x="10cm" y="11cm" />')

    def test_corners_numbers(self):
        rect = Rect(rx=1, ry=1)
        self.assertEqual(rect.tostring(), '<rect height="1" rx="1" ry="1" width="1" x="0" y="0" />')

    def test_corners_length(self):
        rect = Rect(rx='1mm', ry='1mm')
        self.assertEqual(rect.tostring(), '<rect height="1" rx="1mm" ry="1mm" width="1" x="0" y="0" />')

    def test_errors(self):
        self.assertRaises(TypeError, Rect, insert=1)
        self.assertRaises(TypeError, Rect, size=1)
        self.assertRaises(TypeError, Rect, insert=None)
        self.assertRaises(TypeError, Rect, size=None)
        self.assertRaises(TypeError, Rect, size=(None, None))
        self.assertRaises(TypeError, Rect, insert=(None, None))

if __name__=='__main__':
    unittest.main()
