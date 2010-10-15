#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ITransform interface
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import parameter, Group
from svgwrite.base import BaseElement
from svgwrite.interface import IXLink

class Mock(BaseElement, IXLink):
    elementname = 'use'
    def nextid(self):
        return "id999"

class TestIXLink(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_mock_class(self):
        m = Mock()
        self.assertEqual(m.tostring(), '<use />')

    def test_href(self):
        m = Mock()
        m.set_href('an_id')
        self.assertEqual(m.tostring(), '<use xlink:href="#an_id" />')

    def test_object_link(self):
        g = Group(id='test')
        m = Mock()
        m.set_href(g)
        self.assertEqual(m.tostring(), '<use xlink:href="#test" />')

    def test_object_link_auto_id(self):
        parameter._set_auto_id(999) # only for testing !!!!
        g = Group()
        m = Mock()
        m.set_href(g)
        self.assertEqual(m.tostring(), '<use xlink:href="#id999" />')

if __name__=='__main__':
    unittest.main()