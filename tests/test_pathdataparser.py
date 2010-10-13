#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: transform list parser
# Created: 10.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
# depend on: spark.py module - http://pages.cpsc.ucalgary.ca/~aycock/spark/

import unittest

from svgwrite.data.pathdataparser import PathDataScanner, PathDataParser
from svgwrite.data.pathdataparser import path_commands
from svgwrite.data.spark import ParseError, LexicalError

class TestPathDataScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = PathDataScanner()

    def test_digits(self):
        digits = "0123456789"
        tokens = self.scanner.tokenize(digits)
        self.assertEqual(len(tokens), 10)
        for i, char in enumerate(digits):
            self.assertEqual(char, tokens[i])

    def test_digits_sign(self):
        tokens = self.scanner.tokenize("-1")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0], '-')
        self.assertEqual(tokens[1], '1')

    def test_float(self):
        tokens = self.scanner.tokenize("-1.e3")
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0], '-')
        self.assertEqual(tokens[1], '1')
        self.assertEqual(tokens[2], '.')
        self.assertEqual(tokens[3], 'e')
        self.assertEqual(tokens[4], '3')

    def test_special_chars(self):
        tokens = self.scanner.tokenize("-+ ,.E")
        self.assertEqual(len(tokens), 6)
        self.assertEqual(tokens[0], '-')
        self.assertEqual(tokens[1], '+')
        self.assertEqual(tokens[2], 'wsp+')
        self.assertEqual(tokens[3], ',')
        self.assertEqual(tokens[4], '.')
        self.assertEqual(tokens[5], 'e')

    def test_valid_commands_1(self):
        cmdstr = "mMlLhHvVqQcCsSqQtTaA"
        tokens = self.scanner.tokenize(cmdstr)
        self.assertEqual(len(tokens), len(cmdstr))
        for i, cmd in enumerate(cmdstr):
            self.assertEqual(tokens[i], path_commands[cmd.lower()])

    def test_valid_commands_2(self):
        cmdstr = "mMmM"
        tokens = self.scanner.tokenize(cmdstr)
        self.assertEqual(len(tokens), 4)
        for token in tokens:
            self.assertEqual(token, 'moveto-cmd')

    def test_invalid_commands(self):
        self.assertRaises(LexicalError, self.scanner.tokenize, "u 10.0 , 10.5")
        self.assertRaises(LexicalError, self.scanner.tokenize, "://")

class TestPathDataParser(unittest.TestCase):
    def setUp(self):
        self.parser = PathDataParser()
        self.scanner = PathDataScanner()

    def scan(self, text):
        return self.scanner.tokenize(text)

    def cmd(self, command):
        try:
            self.parser.parse(self.scan(command))
        except ParseError:
            self.assertTrue(False, "ParseError: %s" % command)
        except LexicalError:
            self.assertTrue(False, "LexicalError: %s" % command)

    def raise_parse_error(self, command):
        try:
            self.parser.parse(self.scan(command))
            self.assertTrue(False, "ParseError not raised: %s" % command)
        except ParseError:
            self.assertTrue(True)

    def test_integer(self):
        self.cmd("m +100, -100")

    def test_integer_error(self):
        self.raise_parse_error("m +100e, -100")

    def test_float(self):
        self.cmd("m +10.00, -10.00")
        self.cmd("m +10., -10.")
        self.cmd("m +.00, -.00")
        self.cmd("m +10.00e10, -10.00e-30")
        self.cmd("m +10.00E10, -10.00E-30")
        self.cmd("m +10E10, -10E-30")
        self.cmd("m +.10E10, -.10E-30")

    def test_float_error(self):
        self.raise_parse_error("m +100e, -100")
        self.raise_parse_error("m +1.0.0, -10-0")
        self.raise_parse_error("m +1.0.0, -10e-1.0")

    def test_moveto(self):
        self.cmd("m 0, 0")
        self.cmd("m 0,0")
        self.cmd("m 0, 0")
        self.cmd("m 0 ,0")
        self.cmd("m 0 , 0")
        self.cmd("m0,0")
        self.cmd("M0,0,1,1")
        self.cmd("M 0,0 1,1")
        self.cmd("M 0 0 1 1")
        self.cmd("M 0 0 , 1 1")

    def test_moveto_errors(self):
        self.raise_parse_error("m m")
        self.raise_parse_error("m 1 2 3")

    def test_lineto(self):
        self.cmd("m0,0L0,0")
        self.cmd("m0,0 L0,0")
        self.cmd("m0,0 L 0.5 0.5")
        self.cmd("m0,0 L 0.5 0.5 99,88")
        self.cmd("m0,0l0,0")
        self.cmd("m0,0 l0,0")
        self.cmd("m0,0 l 0.5 0.5")
        self.cmd("m0,0 l 0.5 0.5 99,88")

    def test_lineto_errors(self):
        # error: 0 lineto args
        self.raise_parse_error("m0,0 l")
        # error: 1 lineto args
        self.raise_parse_error("m0,0 l0")
        # error: 3 lineto args
        self.raise_parse_error("m0,0 l0,0,0")

    def test_horizontal_lineto(self):
        self.cmd("m0,0h1")
        self.cmd("m0,0H1,2")
        self.cmd("m0,0h1,2,3")
        self.cmd("m0,0H1,2 3,4 5 6 7")
        self.cmd("m0,0h1.")
        self.cmd("m0,0H1.,2.")
        self.cmd("m0,0h.1,.2,.3")
        self.cmd("m0,0H1.,.2 3.,.4 .5 .6 7.")

    def test_horizontal_lineto_errors(self):
        # error: 0 horizontal-lineto args
        self.raise_parse_error("m0,0 h")

    def test_vertical_lineto(self):
        self.cmd("m0,0v1")
        self.cmd("m0,0V1,2")
        self.cmd("m0,0v1,2,3")
        self.cmd("m0,0V1,2 3,4 5 6 7")
        self.cmd("m0,0v1.")
        self.cmd("m0,0V1.,2.")
        self.cmd("m0,0v.1,.2,.3")
        self.cmd("m0,0V1.,.2 3.,.4 .5 .6 7.")

    def test_vertical_lineto_errors(self):
        # error: 0 vertical-lineto args
        self.raise_parse_error("m0,0 v")

    def test_closepath(self):
        self.cmd("m0,0h1z")
        self.cmd("m0,0h1Z")
        self.cmd("m0,0v1 z")
        self.cmd("m0,0v1 Z")

    def test_closepath_errors(self):
        # error: 1 closepath arg
        self.raise_parse_error("m0,0 z 1")

    def test_curveto(self):
        self.cmd("m0,0 c 1 2 3 4 5 6")
        self.cmd("m0,0 C 1 2 3 4 5 6, 7 8 9 10 11 12")

    def test_curveto_errors(self):
        self.raise_parse_error("m0,0 c 1 2 3 4 5")
        self.raise_parse_error("m0,0 C 1 2 3 4 5 6, 7 8 9 10 11")
        self.raise_parse_error("m0,0 C 1 2 3 4 5 6, 7 8 9 10")
        self.raise_parse_error("m0,0 C 1 2 3 4 5 6, 7 8 9")
        self.raise_parse_error("m0,0 C 1 2 3 4 5 6, 7 8")
        self.raise_parse_error("m0,0 C 1 2 3 4 5 6, 7")

    def test_smooth_curveto(self):
        self.cmd("m0,0 s 3 4 5 6")
        self.cmd("m0,0 S 3 4 5 6, 9 10 11 12")

    def test_smooth_curveto_errors(self):
        self.raise_parse_error("m0,0 s 3 4 5")
        self.raise_parse_error("m0,0 S 1 2 3 4, 7 8 9")
        self.raise_parse_error("m0,0 S 1 2 3 4, 7 8")
        self.raise_parse_error("m0,0 S 1 2 3 4, 7")

    def test_quadratic_bezier_curveto(self):
        self.cmd("m0,0 q 1 2 3 4")
        self.cmd("m0,0 Q 1 2 3 4, 5 6 7 8")

    def test_quadratic_bezier_curveto_errors(self):
        self.raise_parse_error("m0,0 q 1 2 3")
        self.raise_parse_error("m0,0 q 1 2 3 4, 5 6 7")
        self.raise_parse_error("m0,0 q 1 2 3 4, 5 6")
        self.raise_parse_error("m0,0 q 1 2 3 4, 5")

    def test_smooth_quadratic_bezier_curveto(self):
        self.cmd("m0,0 t 1 2")
        self.cmd("m0,0 T 1 2 3 4 5 6")

    def test_smooth_quadratic_bezier_curveto_errors(self):
        self.raise_parse_error("m0,0 t 1")
        self.raise_parse_error("m0,0 t 1 2 3")

    def test_elliptical_arc(self):
        self.cmd("m0,0 a 1 1 0 0 0 10 10")
        self.cmd("m0,0 a 1 1 0 1 1 10 10")
        self.cmd("m0,0 A 1 1 0 0 0 10 10, 1 1 0 0 0 10 10")

    def test_elliptical_arc_errors(self):
        self.raise_parse_error("m0,0 a 1 1 45 0 0 10")
        self.raise_parse_error("m0,0 a 1 1 45 0 0")
        self.raise_parse_error("m0,0 a 1 1 45 0")
        self.raise_parse_error("m0,0 a 1 1 45")
        self.raise_parse_error("m0,0 a 1 1")
        self.raise_parse_error("m0,0 a 1")
        self.raise_parse_error("m0,0 a")
        # flag errors flags != [01]
        self.raise_parse_error("m0,0 a 1 1 45 2 2 10 10")

if __name__=='__main__':
    unittest.main()