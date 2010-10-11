#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: transform list parser
# Created: 10.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
# depend on: spark.py module - http://pages.cpsc.ucalgary.ca/~aycock/spark/

import unittest

from svgwrite.data.transformlistparser import TransformParser, TransformScanner
from svgwrite.data.spark import ParseError, LexicalError

class TestTransformScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = TransformScanner()

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


    def test_valid_commands(self):
        tokens = self.scanner.tokenize("translate(10, 10)")
        self.assertEqual(len(tokens), 9)
        self.assertEqual(tokens[0], "translate")

        tokens = self.scanner.tokenize("rotate(10 10)")
        self.assertEqual(tokens[0], "rotate")

        tokens = self.scanner.tokenize("matrix(10 10)")
        self.assertEqual(tokens[0], "matrix")

        tokens = self.scanner.tokenize("scale(10 10)")
        self.assertEqual(tokens[0], "scale")

        tokens = self.scanner.tokenize("skewX(10)")
        self.assertEqual(tokens[0], "skewX")

        tokens = self.scanner.tokenize("skewY(10)")
        self.assertEqual(tokens[0], "skewY")

    def test_invalid_commands(self):
        self.assertRaises(LexicalError, self.scanner.tokenize, "unknown(10.0 , 10.5)")


class TestTransformParser(unittest.TestCase):
    def setUp(self):
        self.parser = TransformParser()
        self.scanner = TransformScanner()

    def scan(self, text):
        return self.scanner.tokenize(text)

    def test_integer(self):
        self.cmd("translate(+100, -100)")

    def test_integer_error(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("translate(+100e, -100)"))

    def test_float(self):
        self.cmd("translate(+10.00, -10.00)")
        self.cmd("translate( +10., -10.)")
        self.cmd("translate(+.00, -.00)")
        self.cmd("translate(+10.00e10, -10.00e-30)")
        self.cmd("translate(+10.00E10, -10.00E-30)")
        self.cmd("translate(+10E10, -10E-30)")
        self.cmd("translate(+.10E10, -.10E-30)")

    def test_float_error(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("translate(+100e, -100)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("translate(+1.0.0, -10-0)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("translate( +1.0.0, -10e-1.0)"))

    def cmd(self, command):
        try:
            self.parser.parse(self.scan(command))
        except ParseError:
            self.assertTrue(False, "ParseError: %s" % command)
        except LexicalError:
            self.assertTrue(False, "LexicalError: %s" % command)

    def test_matrix_1(self):
        self.cmd("matrix(1 2 3 4 5 6)")

    def test_matrix_2(self):
        self.cmd("matrix(1, 2, 3, 4, 5, 6)")

    def test_translate_1(self):
        self.cmd("translate(1)")
    def test_translate_2(self):
        self.cmd("translate(1 2)")
    def test_translate_3(self):
        self.cmd("translate(1,2)")

    def test_rotate_1(self):
        self.cmd("rotate(1)")
    def test_rotate_3(self):
        self.cmd("rotate(1 2 3)")

    def test_scale_1(self):
        self.cmd("scale(1)")
    def test_scale_2(self):
        self.cmd("scale(2)")

    def test_skewX(self):
        self.cmd("skewX(30)")

    def test_skewY(self):
        self.cmd("skewY(30)")

    def test_parse_skewX_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX()"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(30 30)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(30,30)"))

    def test_parse_skewY_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewY()"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewY(30 30)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewY(30,30)"))

    def test_parse_matrix_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("matrix()"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("matrix(1, 2, 3, 4, 5, 6,)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("matrix(1, 2, 3, 4, 5, )"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("matrix(1, 2, 3, 4)"))

    def test_multi_command(self):
        self.cmd("matrix(1 2 3 4 5 6) skewX(30)")
        self.cmd("skewY(15), matrix(1 2 3 4 5 6) skewX(30)")

    def test_multi_command_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(15),, skewY(15)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(15), skewY(15) ,"))

if __name__=='__main__':
    unittest.main()