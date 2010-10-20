#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: transform list parser
# Created: 10.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import unittest

from svgwrite.data.svgparser import TransformListParser

class TestTransformListParser(unittest.TestCase):
    def test_matrix_1(self):
        self.assertTrue(TransformListParser.is_valid("matrix(1 2 3 4 5 6)"))

    def test_matrix_2(self):
        self.assertTrue(TransformListParser.is_valid("matrix(1, 2, 3, 4, 5, 6)"))

    def test_translate_1(self):
        self.assertTrue(TransformListParser.is_valid("translate(1)"))
    def test_translate_2(self):
        self.assertTrue(TransformListParser.is_valid("translate(1 2)"))
    def test_translate_3(self):
        self.assertTrue(TransformListParser.is_valid("translate(1,2)"))

    def test_rotate_1(self):
        self.assertTrue(TransformListParser.is_valid("rotate(1)"))
    def test_rotate_3(self):
        self.assertTrue(TransformListParser.is_valid("rotate(1 2 3)"))

    def test_scale_1(self):
        self.assertTrue(TransformListParser.is_valid("scale(1)"))
    def test_scale_2(self):
        self.assertTrue(TransformListParser.is_valid("scale(2)"))

    def test_skewX(self):
        self.assertTrue(TransformListParser.is_valid("skewX(30)"))

    def test_skewY(self):
        self.assertTrue(TransformListParser.is_valid("skewY(30)"))

    def test_parse_skewX_errors(self):
        self.assertFalse(TransformListParser.is_valid("skewX()"))
        self.assertFalse(TransformListParser.is_valid("skewX(30 30)"))
        self.assertFalse(TransformListParser.is_valid("skewX(30,30)"))

    def test_parse_skewY_errors(self):
        self.assertFalse(TransformListParser.is_valid("skewY()"))
        self.assertFalse(TransformListParser.is_valid("skewY(30 30)"))
        self.assertFalse(TransformListParser.is_valid("skewY(30,30)"))

    def test_parse_matrix_errors(self):
        self.assertFalse(TransformListParser.is_valid("matrix()"))
        self.assertFalse(TransformListParser.is_valid("matrix(1, 2, 3, 4, 5, 6,)"))
        self.assertFalse(TransformListParser.is_valid("matrix(1, 2, 3, 4, 5, )"))
        self.assertFalse(TransformListParser.is_valid("matrix(1, 2, 3, 4)"))

    def test_multi_command(self):
        self.assertTrue(TransformListParser.is_valid("matrix(1 2 3 4 5 6) skewX(30)"))
        self.assertTrue(TransformListParser.is_valid("skewY(15), matrix(1 2 3 4 5 6) skewX(30)"))

    def test_multi_command_errors(self):
        self.assertFalse(TransformListParser.is_valid("skewX(15),, skewY(15)"))
        self.assertFalse(TransformListParser.is_valid("skewX(15), skewY(15) ,"))

    def test_parse(self):
        self.assertRaises(NotImplementedError, TransformListParser.parse, 'test')

if __name__=='__main__':
    unittest.main()