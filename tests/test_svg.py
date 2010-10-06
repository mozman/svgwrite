#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import SVG, Symbol
from svgwrite.params import parameter

class TestSVG(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        svg = SVG()
        self.assertTrue(isinstance(svg, Symbol))
        self.assertEqual(svg.tostring(), "<svg><defs /></svg>")

    def test_add_svg_as_subelement(self):
        svg = SVG(id='svg')
        subsvg = SVG(id='subsvg')
        svg.add(subsvg)
        self.assertEqual(svg.tostring(), '<svg id="svg"><defs /><svg id="subsvg"><defs /></svg></svg>')

if __name__=='__main__':
    unittest.main()