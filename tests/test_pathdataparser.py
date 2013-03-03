#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: transform list parser
# Created: 10.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.data.svgparser import is_valid_pathdata

class TestPathDataParser(unittest.TestCase):
    def test_moveto(self):
        self.assertTrue(is_valid_pathdata("m 0, 0"))
        self.assertTrue(is_valid_pathdata("m 0,0"))
        self.assertTrue(is_valid_pathdata("m 0, 0"))
        self.assertTrue(is_valid_pathdata("m 0 ,0"))
        self.assertTrue(is_valid_pathdata("m 0 , 0"))
        self.assertTrue(is_valid_pathdata("m0,0"))
        self.assertTrue(is_valid_pathdata("M0,0,1,1"))
        self.assertTrue(is_valid_pathdata("M 0,0 1,1"))
        self.assertTrue(is_valid_pathdata("M 0 0 1 1"))
        self.assertTrue(is_valid_pathdata("M 0 0 , 1 1"))

    def test_moveto_errors(self):
        self.assertFalse(is_valid_pathdata("m m"))
        self.assertFalse(is_valid_pathdata("m 1 2 3"))

    def test_lineto(self):
        self.assertTrue(is_valid_pathdata("m0,0L0,0"))
        self.assertTrue(is_valid_pathdata("m0,0 L0,0"))
        self.assertTrue(is_valid_pathdata("m0,0 L 0.5 0.5"))
        self.assertTrue(is_valid_pathdata("m0,0 L 0.5 0.5 99,88"))
        self.assertTrue(is_valid_pathdata("m0,0l0,0"))
        self.assertTrue(is_valid_pathdata("m0,0 l0,0"))
        self.assertTrue(is_valid_pathdata("m0,0 l 0.5 0.5"))
        self.assertTrue(is_valid_pathdata("m0,0 l 0.5 0.5 99,88"))

    def test_lineto_errors(self):
        # error: 0 lineto args
        self.assertFalse(is_valid_pathdata("m0,0 l"))
        # error: 1 lineto args
        self.assertFalse(is_valid_pathdata("m0,0 l0"))
        # error: 3 lineto args
        self.assertFalse(is_valid_pathdata("m0,0 l0,0,0"))

    def test_horizontal_lineto(self):
        self.assertTrue(is_valid_pathdata("m0,0h1"))
        self.assertTrue(is_valid_pathdata("m0,0H1,2"))
        self.assertTrue(is_valid_pathdata("m0,0h1,2,3"))
        self.assertTrue(is_valid_pathdata("m0,0H1,2 3,4 5 6 7"))
        self.assertTrue(is_valid_pathdata("m0,0h1."))
        self.assertTrue(is_valid_pathdata("m0,0H1.,2."))
        self.assertTrue(is_valid_pathdata("m0,0h.1,.2,.3"))
        self.assertTrue(is_valid_pathdata("m0,0H1.,.2 3.,.4 .5 .6 7."))

    def test_horizontal_lineto_errors(self):
        # error: 0 horizontal-lineto args
        self.assertFalse(is_valid_pathdata("m0,0 h"))

    def test_vertical_lineto(self):
        self.assertTrue(is_valid_pathdata("m0,0v1"))
        self.assertTrue(is_valid_pathdata("m0,0V1,2"))
        self.assertTrue(is_valid_pathdata("m0,0v1,2,3"))
        self.assertTrue(is_valid_pathdata("m0,0V1,2 3,4 5 6 7"))
        self.assertTrue(is_valid_pathdata("m0,0v1."))
        self.assertTrue(is_valid_pathdata("m0,0V1.,2."))
        self.assertTrue(is_valid_pathdata("m0,0v.1,.2,.3"))
        self.assertTrue(is_valid_pathdata("m0,0V1.,.2 3.,.4 .5 .6 7."))

    def test_vertical_lineto_errors(self):
        # error: 0 vertical-lineto args
        self.assertFalse(is_valid_pathdata("m0,0 v"))

    def test_closepath(self):
        self.assertTrue(is_valid_pathdata("m0,0h1z"))
        self.assertTrue(is_valid_pathdata("m0,0h1Z"))
        self.assertTrue(is_valid_pathdata("m0,0v1 z"))
        self.assertTrue(is_valid_pathdata("m0,0v1 Z"))

    def test_closepath_errors(self):
        # error: 1 closepath arg
        self.assertFalse(is_valid_pathdata("m0,0 z 1"))

    def test_curveto(self):
        self.assertTrue(is_valid_pathdata("m0,0 c 1 2 3 4 5 6"))
        self.assertTrue(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7 8 9 10 11 12"))

    def test_curveto_errors(self):
        self.assertFalse(is_valid_pathdata("m0,0 c 1 2 3 4 5"))
        self.assertFalse(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7 8 9 10 11"))
        self.assertFalse(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7 8 9 10"))
        self.assertFalse(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7 8 9"))
        self.assertFalse(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7 8"))
        self.assertFalse(is_valid_pathdata("m0,0 C 1 2 3 4 5 6, 7"))

    def test_smooth_curveto(self):
        self.assertTrue(is_valid_pathdata("m0,0 s 3 4 5 6"))
        self.assertTrue(is_valid_pathdata("m0,0 S 3 4 5 6, 9 10 11 12"))

    def test_smooth_curveto_errors(self):
        self.assertFalse(is_valid_pathdata("m0,0 s 3 4 5"))
        self.assertFalse(is_valid_pathdata("m0,0 S 1 2 3 4, 7 8 9"))
        self.assertFalse(is_valid_pathdata("m0,0 S 1 2 3 4, 7 8"))
        self.assertFalse(is_valid_pathdata("m0,0 S 1 2 3 4, 7"))

    def test_quadratic_bezier_curveto(self):
        self.assertTrue(is_valid_pathdata("m0,0 q 1 2 3 4"))
        self.assertTrue(is_valid_pathdata("m0,0 Q 1 2 3 4, 5 6 7 8"))

    def test_quadratic_bezier_curveto_errors(self):
        self.assertFalse(is_valid_pathdata("m0,0 q 1 2 3"))
        self.assertFalse(is_valid_pathdata("m0,0 q 1 2 3 4, 5 6 7"))
        self.assertFalse(is_valid_pathdata("m0,0 q 1 2 3 4, 5 6"))
        self.assertFalse(is_valid_pathdata("m0,0 q 1 2 3 4, 5"))

    def test_smooth_quadratic_bezier_curveto(self):
        self.assertTrue(is_valid_pathdata("m0,0 t 1 2"))
        self.assertTrue(is_valid_pathdata("m0,0 T 1 2 3 4 5 6"))

    def test_smooth_quadratic_bezier_curveto_errors(self):
        self.assertFalse(is_valid_pathdata("m0,0 t 1"))
        self.assertFalse(is_valid_pathdata("m0,0 t 1 2 3"))

    def test_elliptical_arc(self):
        self.assertTrue(is_valid_pathdata("m0,0 a 1 1 0 0 0 10 10"))
        self.assertTrue(is_valid_pathdata("m0,0 a 1 1 0 1 1 10 10"))
        self.assertTrue(is_valid_pathdata("m0,0 A 1 1 0 0 0 10 10, 1 1 0 0 0 10 10"))

    def test_elliptical_arc_errors(self):
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1 45 0 0 10"))
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1 45 0 0"))
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1 45 0"))
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1 45"))
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1"))
        self.assertFalse(is_valid_pathdata("m0,0 a 1"))
        self.assertFalse(is_valid_pathdata("m0,0 a"))
        # flag errors flags != [01]
        self.assertFalse(is_valid_pathdata("m0,0 a 1 1 45 2 2 10 10"))

if __name__ == '__main__':
    unittest.main()
