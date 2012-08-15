#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ClipPath
# Created: 31.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.masking import ClipPath
from svgwrite.shapes import Circle

class TestClipPath(unittest.TestCase):
    def test_constructor(self):
        clip_path = ClipPath(debug=True, profile='full')
        self.assertEqual(clip_path.tostring(), '<clipPath />')

    def test_transform(self):
        clip_path = ClipPath(debug=True, profile='full')
        clip_path.translate(10, 20)
        self.assertEqual(clip_path.tostring(), '<clipPath transform="translate(10,20)" />')

    def test_add_subelement(self):
        clip_path = ClipPath(debug=True, profile='full')
        clip_path.add(Circle((50,60), 70))
        self.assertEqual(clip_path.tostring(), '<clipPath><circle cx="50" cy="60" r="70" /></clipPath>')

if __name__=='__main__':
    unittest.main()
