#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test TextArea class
# Created: 14.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.text import TextArea
from svgwrite.text import TBreak


class TestTBreak(unittest.TestCase):
    def test_tostring(self):
        br = TBreak(profile='tiny')
        self.assertEqual(br.tostring(), "<tbreak />")

    def test_errors(self):
        br = TBreak()
        self.assertRaises(NotImplementedError, br.add, None)
        self.assertRaises(NotImplementedError, br.__getitem__, 'key')
        self.assertRaises(NotImplementedError, br.__setitem__, 'key', 'value')


class TestTextAreaFullProfile(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(KeyError, TextArea, (0, 0))


class TestTextAreaTinyProfile(unittest.TestCase):
    def test_constructor(self):
        textarea = TextArea(insert=(1, 2), size=(10,20), profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea height="20" width="10" x="1" y="2" />')

    def test_write_one_line(self):
        textarea = TextArea(profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea />')
        textarea.write('a line.')
        self.assertEqual(textarea.tostring(), '<textArea><tspan>a line.</tspan></textArea>')

    def test_write_linebreaks(self):
        textarea = TextArea('\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /></textArea>')
        textarea = TextArea('\n\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /><tbreak /></textArea>')

    def test_write_lines(self):
        textarea = TextArea('line1\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tspan>line1</tspan><tbreak /></textArea>')

        textarea = TextArea('line1\nline2', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tspan>line1</tspan><tbreak />'
                         '<tspan>line2</tspan></textArea>')

        textarea = TextArea('line1\nline2\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tspan>line1</tspan><tbreak />'
                         '<tspan>line2</tspan><tbreak /></textArea>')

        textarea = TextArea('line1\n \nline2\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tspan>line1</tspan><tbreak />'
                         '<tspan> </tspan><tbreak /><tspan>line2</tspan><tbreak /></textArea>')

    def test_line_increment(self):
        textarea = TextArea('line1\n', profile='tiny')
        textarea.line_increment('14')
        self.assertEqual(textarea.tostring(), '<textArea line-increment="14"><tspan>line1</tspan><tbreak /></textArea>')

    def test_write_lines_prepending_linebreak(self):
        textarea = TextArea('\nline1\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /><tspan>line1</tspan><tbreak /></textArea>')

        textarea = TextArea('\nline1\nline2', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /><tspan>line1</tspan><tbreak />'
                         '<tspan>line2</tspan></textArea>')

        textarea = TextArea('\nline1\nline2\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /><tspan>line1</tspan><tbreak />'
                         '<tspan>line2</tspan><tbreak /></textArea>')

        textarea = TextArea('\nline1\n\nline2\n', profile='tiny')
        self.assertEqual(textarea.tostring(), '<textArea><tbreak /><tspan>line1</tspan><tbreak />'
                         '<tbreak /><tspan>line2</tspan><tbreak /></textArea>')


if __name__ == '__main__':
    unittest.main()
