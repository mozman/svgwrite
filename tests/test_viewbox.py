#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ITransform interface
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.params import Parameter
from svgwrite.base import BaseElement
from svgwrite.mixins import ViewBox

class Mock(BaseElement, ViewBox):
    elementname = 'svg'
    _parameter = Parameter(True, 'full')

class TestViewBox(unittest.TestCase):
    def test_mock_class(self):
        m = Mock()
        self.assertEqual(m.tostring(), '<svg />')

    def test_viewbox(self):
        m = Mock()
        m.viewbox(minx=1, miny=2, width=10, height=20)
        self.assertEqual(m.tostring(), '<svg viewBox="1,2,10,20" />')

    def test_viewbox_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.viewbox, '10cm')

    def test_strech(self):
        m = Mock()
        m.stretch()
        self.assertEqual(m.tostring(), '<svg preserveAspectRatio="none" />')

    def test_fit_horiz(self):
        m = Mock()
        for align, expected in [('left', 'xMin'), ('center', 'xMid'), ('right', 'xMax')]:
            m.fit(align, 'top', 'meet')
            self.assertEqual(m.tostring(), '<svg preserveAspectRatio="%sYMin meet" />' % expected)

    def test_fit_vert(self):
        m = Mock()
        for align, expected in [('top', 'YMin'), ('middle', 'YMid'), ('bottom', 'YMax')]:
            m.fit('left', align, 'slice')
            self.assertEqual(m.tostring(), '<svg preserveAspectRatio="xMin%s slice" />' % expected)

    def test_fit_err(self):
        m = Mock()
        self.assertRaises(ValueError, m.fit, scale='invalid')
        self.assertRaises(KeyError, m.fit, horiz='invalid')
        self.assertRaises(KeyError, m.fit, vert='invalid')

if __name__=='__main__':
    unittest.main()
