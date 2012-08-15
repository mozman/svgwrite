#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test presentation mixin
# Created: 24.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.base import BaseElement
from svgwrite.mixins import Presentation
from svgwrite import rgb

class PresentationClass(BaseElement, Presentation):
    elementname = "line" # element with valid presentation attributes

class MockPaintServer:
    def get_paint_server(self):
        return "url(#mockpaintserver)"

class TestPresentationMixin(unittest.TestCase):
    def test_fill(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.fill(color='red', rule="evenodd", opacity=1.0)
        self.assertEqual(obj.tostring(),
                         '<line fill="red" fill-opacity="1.0" fill-rule="evenodd" />')

    def test_fill_rgb_values(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.fill(color=rgb(10, 20, 30), rule="evenodd", opacity=1.0)
        self.assertEqual(obj.tostring(),
                         '<line fill="rgb(10,20,30)" fill-opacity="1.0" fill-rule="evenodd" />')

    def test_fill_rgb_percentage(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.fill(color=rgb(10, 20, 30, '%'), rule="evenodd", opacity=1.0)
        self.assertEqual(obj.tostring(),
                         '<line fill="rgb(10%,20%,30%)" fill-opacity="1.0" fill-rule="evenodd" />')

    def test_fill_paintserver(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.fill(color=MockPaintServer())
        self.assertEqual(obj.tostring(),
                         '<line fill="url(#mockpaintserver)" />')

    def test_stroke(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.stroke(color='red', width=2, opacity=0.5, linecap='round',
                   linejoin='round', miterlimit='1.5')
        self.assertEqual(obj.tostring(),
                         '<line stroke="red" ' \
                         'stroke-linecap="round" ' \
                         'stroke-linejoin="round" ' \
                         'stroke-miterlimit="1.5" ' \
                         'stroke-opacity="0.5" ' \
                         'stroke-width="2" />')

    def test_stroke_paintserver(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.stroke(color=MockPaintServer())
        self.assertEqual(obj.tostring(),
                         '<line stroke="url(#mockpaintserver)" />')

    def test_dasharray(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.dasharray([1., 0.5], offset=0.5)
        self.assertEqual(obj.tostring(),
                         '<line stroke-dasharray="1.0 0.5" stroke-dashoffset="0.5" />')

        obj.dasharray('1.0 0.5', offset=0.5)
        self.assertEqual(obj.tostring(),
                         '<line stroke-dasharray="1.0 0.5" stroke-dashoffset="0.5" />')

    def test_combi_call(self):
        obj = PresentationClass(debug=True, profile='full')
        obj.fill('red').stroke('blue')
        self.assertEqual(obj.tostring(),
                         '<line fill="red" stroke="blue" />')

if __name__=='__main__':
    unittest.main()
