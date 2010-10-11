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
        self.assertAlmostEqual(tokens[0], '-')
        self.assertAlmostEqual(tokens[1], '1')

    def test_float(self):
        tokens = self.scanner.tokenize("-1.e3")
        self.assertEqual(len(tokens), 5)
        self.assertAlmostEqual(tokens[0], '-')
        self.assertAlmostEqual(tokens[1], '1')
        self.assertAlmostEqual(tokens[2], '.')
        self.assertAlmostEqual(tokens[3], 'e')
        self.assertAlmostEqual(tokens[4], '3')

    def test_special_chars(self):
        tokens = self.scanner.tokenize("-+ ,.E")
        self.assertEqual(len(tokens), 6)
        self.assertAlmostEqual(tokens[0], '-')
        self.assertAlmostEqual(tokens[1], '+')
        self.assertAlmostEqual(tokens[2], 'wsp+')
        self.assertAlmostEqual(tokens[3], ',')
        self.assertAlmostEqual(tokens[4], '.')
        self.assertAlmostEqual(tokens[5], 'e')

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

    def test_integer(self):
        self.cmd("m +100, -100")

    def test_integer_error(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("m +100e, -100"))

    def test_float(self):
        self.cmd("m +10.00, -10.00")
        self.cmd("m +10., -10.")
        self.cmd("m +.00, -.00")
        self.cmd("m +10.00e10, -10.00e-30")
        self.cmd("m +10.00E10, -10.00E-30")
        self.cmd("m +10E10, -10E-30")
        self.cmd("m +.10E10, -.10E-30")

    def test_float_error(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("m +100e, -100"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("m +1.0.0, -10-0"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("m +1.0.0, -10e-1.0"))

    def test_moveto_1(self):
        self.cmd("m 0, 0")
        self.cmd("m 0,0")
        self.cmd("m 0, 0")
        self.cmd("m 0 ,0")
        self.cmd("m 0 , 0")
        self.cmd("m0,0")

    def test_moveto_2(self):
        self.cmd("M0,0,1,1")
        self.cmd("M 0,0 1,1")
        self.cmd("M 0 0 1 1")
        self.cmd("M 0 0 , 1 1")

    def test_moveto_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("m m"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("m 1 2 3"))

    def test_lineto_1(self):
        self.cmd("m0,0l0,0")
        self.cmd("m0,0 l0,0")
        self.cmd("M 0 0 L 0.5 0.5")

if __name__=='__main__':
    unittest.main()