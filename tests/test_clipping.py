#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test mixin Clipping
# Created: 31.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.mixins import Clipping
from svgwrite.base import BaseElement

class SVGMock(BaseElement, Clipping):
    elementname = 'svg'

class TestClipping(unittest.TestCase):
    def test_clip_rect_numbers(self):
        obj = SVGMock(debug=True)
        obj.clip_rect(1, 2, 3, 4)
        self.assertEqual(obj['clip'], 'rect(1,2,3,4)')

    def test_clip_rect_auto(self):
        obj = SVGMock(debug=True)
        obj.clip_rect('auto', 'auto', 'auto', 'auto')
        self.assertEqual(obj['clip'], 'rect(auto,auto,auto,auto)')

if __name__=='__main__':
    unittest.main()
