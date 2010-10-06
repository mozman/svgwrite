#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test polyline object
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import Polyline, parameter

class TestPolyline(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_numbers(self):
        polyline = Polyline(points=[(0,0), (1,1)])
        self.assertEqual(polyline.tostring(), '<polyline points="0,0 1,1" />')

    def test_coordinates(self):
        # list of points is a list of numbers not coordinates -> no units allowed!!
        self.assertRaises(TypeError, Polyline, [('1cm','1cm'), ('2mm', '1mm')])

    def test_errors(self):
        self.assertRaises(TypeError, Polyline, 0)
        self.assertRaises(TypeError, Polyline, None)
        self.assertRaises(TypeError, Polyline, [(None, None)])

if __name__=='__main__':
    unittest.main()