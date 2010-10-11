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
from svgwrite.data.transformlistparser import ParseError, LexicalError

class TestTransformScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = TransformScanner()

    def test_valid_numbers(self):
        tokens = self.scanner.tokenize("(10.0 , 10.5)")
        self.assertEqual(len(tokens), 5)
        self.assertAlmostEqual(tokens[1].attr, 10.)
        self.assertAlmostEqual(tokens[3].attr, 10.5)

        tokens = self.scanner.tokenize("(-.0 , -.5)")
        self.assertEqual(len(tokens), 5)
        self.assertAlmostEqual(tokens[1].attr, 0.)
        self.assertAlmostEqual(tokens[3].attr, -.5)

        tokens = self.scanner.tokenize("(-1e3 , .5e-3)")
        self.assertEqual(len(tokens), 5)
        self.assertAlmostEqual(tokens[1].attr, -1000)
        self.assertAlmostEqual(tokens[3].attr, .0005)

    def test_invalid_numbers(self):
        # this should NOT be a lexical error, caused by regex for t_number
        self.assertRaises(LexicalError, self.scanner.tokenize, "(10. , 10.)")
        self.assertRaises(LexicalError, self.scanner.tokenize, "(txt1 , txt2)")

    def test_valid_commands(self):
        tokens = self.scanner.tokenize("translate(10, 10)")
        self.assertEqual(len(tokens), 6)
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

    def transform_command(self, command):
        try:
            self.parser.parse(self.scan(command))
        except ParseError:
            self.assertTrue(False, "ParseError: %s" % command)
        except LexicalError:
            self.assertTrue(False, "LexicalError: %s" % command)

    def test_matrix_1(self):
        self.transform_command("matrix(1 2 3 4 5 6)")

    def test_matrix_2(self):
        self.transform_command("matrix(1, 2, 3, 4, 5, 6)")

    def test_translate_1(self):
        self.transform_command("translate(1)")
    def test_translate_2(self):
        self.transform_command("translate(1 2)")
    def test_translate_3(self):
        self.transform_command("translate(1,2)")

    def test_rotate_1(self):
        self.transform_command("rotate(1)")
    def test_rotate_3(self):
        self.transform_command("rotate(1 2 3)")

    def test_scale_1(self):
        self.transform_command("scale(1)")
    def test_scale_2(self):
        self.transform_command("scale(2)")

    def test_skewX(self):
        self.transform_command("skewX(30)")

    def test_skewY(self):
        self.transform_command("skewY(30)")

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
        self.transform_command("matrix(1 2 3 4 5 6) skewX(30)")
        self.transform_command("skewY(15), matrix(1 2 3 4 5 6) skewX(30)")

    def test_multi_command_errors(self):
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(15),, skewY(15)"))
        self.assertRaises(ParseError, self.parser.parse, self.scan("skewX(15), skewY(15) ,"))

if __name__=='__main__':
    unittest.main()