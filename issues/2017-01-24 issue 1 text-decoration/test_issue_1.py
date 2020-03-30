#!/usr/bin/env python
#coding:utf-8
# Author:  mozman <mozman@gmx.at>
# Copyright (C) 2017, Manfred Moitzi
# License: MIT License
import unittest
from svgwrite.text import Text


class TestIssue0001(unittest.TestCase):
    def test_text_decorator_full_profile(self):
        text = Text(
            "test",
            insert=(0, 0),
            font_size="30px",
            fill='black',
            text_decoration='underline',
            profile='full',
            )
        self.assertEqual(text.elementname, 'text')

    def test_text_decorator_tiny_profile(self):
        with self.assertRaises(ValueError):  # text-decoration is not supported in the DVG 1.2 Tiny profile
            Text(
                "test",
                insert=(0, 0),
                font_size="30px",
                fill='black',
                text_decoration='underline',
                profile='tiny',
                )


if __name__ == '__main__':
    unittest.main()
