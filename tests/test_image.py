#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test image object
# Created: 09.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.image import Image

class TestImage(unittest.TestCase):
    def test_constructor(self):
        image = Image("http://localhost/test.jpg")
        self.assertEqual(image.tostring(), '<image xlink:href="http://localhost/test.jpg" />')

    def test_constructor2(self):
        image = Image("test.jpg", insert=(10,20), size=(30,40))
        self.assertEqual(image.tostring(), '<image height="40" width="30" x="10" xlink:href="test.jpg" y="20" />')

    def test_errors(self):
        self.assertRaises(TypeError, Image, 1)
        self.assertRaises(TypeError, Image, 3.1415)
        self.assertRaises(TypeError, Image, (1,2))
        self.assertRaises(TypeError, Image, dict(a=1))

    def test_strech(self):
        image = Image("http://test.jpg")
        image.stretch()
        self.assertEqual(image.tostring(), '<image preserveAspectRatio="none" xlink:href="http://test.jpg" />')

    def test_fit_horiz(self):
        image = Image("http://test.jpg")
        for align, expected in [('left', 'xMin'), ('center', 'xMid'), ('right', 'xMax')]:
            image.fit(align, 'top', 'meet')
            self.assertEqual(image.tostring(), '<image preserveAspectRatio="%sYMin meet" xlink:href="http://test.jpg" />' % expected)

    def test_fit_vert(self):
        image = Image("http://test.jpg")
        for align, expected in [('top', 'YMin'), ('middle', 'YMid'), ('bottom', 'YMax')]:
            image.fit('left', align, 'slice')
            self.assertEqual(image.tostring(), '<image preserveAspectRatio="xMin%s slice" xlink:href="http://test.jpg" />' % expected)

    def test_fit_err(self):
        image = Image("http://test.jpg")
        self.assertRaises(ValueError, image.fit, scale='invalid')
        self.assertRaises(KeyError, image.fit, horiz='invalid')
        self.assertRaises(KeyError, image.fit, vert='invalid')

if __name__=='__main__':
    unittest.main()
