#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test pattern module
# Created: 29.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.pattern import Pattern

class TestPattern(unittest.TestCase):
    def test_constructor(self):
        pattern = Pattern(insert=(10, 20), size=(30, 40), inherit='#test',
                          debug=True, profile='full')
        self.assertEqual(
            pattern.tostring(),
            '<pattern height="40" width="30" x="10" xlink:href="#test" y="20" />')

    def test_get_paint_server(self):
        pattern = Pattern(id="testpattern", debug=True, profile='full')
        self.assertEqual(pattern.get_paint_server(), "url(#testpattern) none")

    def test_inherit_from_pattern(self):
        parent = Pattern(id='test')
        pattern = Pattern(insert=(10, 20), size=(30, 40), inherit=parent,
                          debug=True, profile='full')
        self.assertEqual(
            pattern.tostring(),
            '<pattern height="40" width="30" x="10" xlink:href="#test" y="20" />')



if __name__=='__main__':
    unittest.main()
