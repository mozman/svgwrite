#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test solidcolor module
# Created: 26.10.2016
# Copyright (C) 2016, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.solidcolor import SolidColor


class TestPattern(unittest.TestCase):
    def test_constructor(self):
        color = SolidColor(debug=True, profile='tiny')
        self.assertEqual(
            color.tostring(),
            '<solidColor solid-color="currentColor" />')

    def test_parameters(self):
        color = SolidColor(color='red', opacity=0.5, debug=True, profile='tiny')
        self.assertEqual(
            color.tostring(),
            '<solidColor solid-color="red" solid-opacity="0.5" />')

    def test_valid_profile(self):
        with self.assertRaises(TypeError):
            SolidColor(profile='full')

    def test_get_paint_server(self):
        color = SolidColor(id="mysolidcolor", debug=True, profile='tiny')
        self.assertEqual(color.get_paint_server(), "url(#mysolidcolor) none")


if __name__ == '__main__':
    unittest.main()
