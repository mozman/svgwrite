#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test MediaGroup mixin
# Created: 24.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.base import BaseElement
from svgwrite.mixins import MediaGroup

class MediaGroupClass(BaseElement, MediaGroup):
    elementname = "image" # element with valid media group attributes

class TestMediaGroupMixin(unittest.TestCase):
    def test_viewport_fill(self):
        obj = MediaGroupClass(debug=True, profile='tiny')
        obj.viewport_fill(color='red', opacity=1.0)
        self.assertEqual(obj.tostring(),
                         '<image viewport-fill="red" viewport-fill-opacity="1.0" />')

if __name__=='__main__':
    unittest.main()
