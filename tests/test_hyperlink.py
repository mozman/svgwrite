#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test hyperlink object
# Created: 09.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.container import Hyperlink

class TestHyperlink(unittest.TestCase):

    def test_constructor(self):
        link = Hyperlink("http://localhost:8080")
        self.assertEqual(link.tostring(), '<a target="_blank" xlink:href="http://localhost:8080" />')

    def test_errors(self):
        self.assertRaises(TypeError, Hyperlink, 1)
        self.assertRaises(TypeError, Hyperlink, 3.1415)
        self.assertRaises(TypeError, Hyperlink, (1,2))
        self.assertRaises(TypeError, Hyperlink, dict(a=1))

if __name__=='__main__':
    unittest.main()
