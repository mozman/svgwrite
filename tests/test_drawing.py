#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test drawing module
# Created: 11.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.parameter import init
from svgwrite.drawing import Drawing

class TestDrawingFullProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='full', debug=True)

    def test_empty_drawing(self):
        dwg = Drawing()
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="full" height="100%" version="1.1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" />')

class TestDrawingTinyProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='tiny', debug=True)

    def test_empty_drawing(self):
        dwg = Drawing()
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="tiny" height="100%" version="1.2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" />')

if __name__=='__main__':
    unittest.main()