#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.container import SVG, Symbol

class TestSVG(unittest.TestCase):
    def test_constructor(self):
        svg = SVG(insert=(10,20), size=(100,200))
        self.assertTrue(isinstance(svg, Symbol))
        self.assertEqual(svg.tostring(), '<svg height="200" width="100" x="10" y="20"><defs /></svg>')

    def test_add_svg_as_subelement(self):
        svg = SVG(id='svg')
        subsvg = SVG(id='subsvg')
        svg.add(subsvg)
        self.assertEqual(svg.tostring(), '<svg id="svg"><defs /><svg id="subsvg"><defs /></svg></svg>')

if __name__=='__main__':
    unittest.main()
