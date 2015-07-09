#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test gradients module
# Created: 26.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest
import re

from svgwrite.gradients import _GradientStop, LinearGradient, RadialGradient

class TestGradientStop(unittest.TestCase):
    def test_constructor1(self):
        stop = _GradientStop(offset=0.5, color='red', opacity=1.0, debug=True, profile='full')
        self.assertEqual(stop.tostring(), '<stop offset="0.5" stop-color="red" stop-opacity="1.0" />')

    def test_constructor2(self):
        stop = _GradientStop(offset='50%', color='red', opacity=0.63, debug=True, profile='full')
        self.assertEqual(stop.tostring(), '<stop offset="50%" stop-color="red" stop-opacity="0.63" />')

    def test_constructor3(self):
        stop = _GradientStop(debug=True, profile='full')
        self.assertEqual(stop.tostring(), '<stop />')

class TestLinearGradient(unittest.TestCase):
    def test_constructor(self):
        lg = LinearGradient(start=(1, 2), end=(10, 20), inherit='#test', debug=True, profile='full')
        self.assertEqual(
            '<linearGradient x1="1" x2="10" xlink:href="#test" y1="2" y2="20" />',
            lg.tostring())

    def test_get_paint_server(self):
        lg = LinearGradient()
        self.assertTrue(re.match("^url\(#id\d+\) none$", lg.get_paint_server()))
        self.assertTrue(re.match("^url\(#id\d+\) red$", lg.get_paint_server(default='red')))

    def test_add_stop_color(self):
        lg = LinearGradient()
        lg.add_stop_color(offset=0.5, color='red', opacity=1.0)
        self.assertEqual(lg.tostring(), '<linearGradient><stop offset="0.5" stop-color="red" stop-opacity="1.0" /></linearGradient>')

    def test_add_colors(self):
        lg = LinearGradient()
        lg.add_colors(['white', 'red', 'blue', 'green'], opacity=0.5)
        result = '<linearGradient>' \
                 '<stop offset="0.0" stop-color="white" stop-opacity="0.5" />' \
                 '<stop offset="0.333" stop-color="red" stop-opacity="0.5" />' \
                 '<stop offset="0.667" stop-color="blue" stop-opacity="0.5" />' \
                 '<stop offset="1.0" stop-color="green" stop-opacity="0.5" />' \
                 '</linearGradient>'
        self.assertEqual(lg.tostring(), result)

    def test_inherit(self):
        inherit_from = LinearGradient(id='test')
        lg = LinearGradient(inherit=inherit_from)
        self.assertTrue('<linearGradient xlink:href="#test"/>', lg.tostring())

class TestRadialGradient(unittest.TestCase):
    def test_constructor(self):
        rg = RadialGradient(center=(10, 20), r=10, focal=(15, 25), inherit='#test', debug=True, profile='full')
        self.assertEqual(rg.tostring(),
            '<radialGradient cx="10" cy="20" fx="15" fy="25" r="10" xlink:href="#test" />')

    def test_get_paint_server(self):
        rg = RadialGradient()
        self.assertTrue(re.match("^url\(#id\d+\) none$", rg.get_paint_server()))
        self.assertTrue(re.match("^url\(#id\d+\) red$", rg.get_paint_server(default='red')))

    def test_add_stop_color(self):
        rg = RadialGradient()
        rg.add_stop_color(offset=0.5, color='red', opacity=1.0)
        self.assertEqual(rg.tostring(), '<radialGradient><stop offset="0.5" stop-color="red" stop-opacity="1.0" /></radialGradient>')

if __name__=='__main__':
    unittest.main()
