#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test markers mixin
# Created: 24.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.base import BaseElement
from svgwrite.mixins import Markers

class MarkerMock(BaseElement, Markers):
    elementname = 'line' # has valid marker properties

class TestMarkers(unittest.TestCase):

    def test_with_one_string(self):
        e = MarkerMock(debug=True, profile='full')
        e.set_markers('#mozman')
        self.assertEqual(e.tostring(), '<line marker="url(#mozman)" />')

    def test_with_three_strings(self):
        e = MarkerMock(debug=True, profile='full')
        e.set_markers(('#mozman1', '#mozman2', '#mozman3'))
        self.assertEqual(e.tostring(), '<line marker-end="url(#mozman3)" ' \
                         'marker-mid="url(#mozman2)" marker-start="url(#mozman1)" />')

    def test_with_one_obj(self):
        marker = MarkerMock(id='mozman', debug=True, profile='full')
        e = MarkerMock(debug=True, profile='full')
        e.set_markers(marker)
        self.assertEqual(e.tostring(), '<line marker="url(#mozman)" />')

    def test_with_three_obj(self):
        m1 = MarkerMock(id='mozman1', debug=True, profile='full')
        m2 = MarkerMock(id='mozman2', debug=True, profile='full')
        m3 = MarkerMock(id='mozman3', debug=True, profile='full')
        e = MarkerMock(debug=True, profile='full')

        e.set_markers((m1, m2, m3))
        self.assertEqual(e.tostring(), '<line marker-end="url(#mozman3)" ' \
                         'marker-mid="url(#mozman2)" marker-start="url(#mozman1)" />')

    def test_unpack_error(self):
        e = MarkerMock(debug=True, profile='full')
        # one or three values not two
        self.assertRaises(ValueError, e.set_markers, (1, 2))

    def test_id_error(self):
        e = MarkerMock(debug=True, profile='full')
        # intergers not valid
        self.assertRaises(TypeError, e.set_markers, (1, 2, 3))

if __name__=='__main__':
    unittest.main()
