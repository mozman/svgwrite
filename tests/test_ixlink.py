#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ITransform interface
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest
import re

from svgwrite.container import Group
from svgwrite.params import Parameter
from svgwrite.base import BaseElement
from svgwrite.interface import IXLink

class Mock(BaseElement, IXLink):
    elementname = 'use'
    _parameter = Parameter(True, 'full')

    def next_id(self):
        return "id999"

class TestIXLink(unittest.TestCase):
    def test_mock_class(self):
        m = Mock()
        self.assertEqual(m.tostring(), '<use />')

    def test_href(self):
        m = Mock()
        m.set_href('#an_id')
        self.assertEqual(m.tostring(), '<use xlink:href="#an_id" />')

    def test_object_link(self):
        g = Group(id='test')
        m = Mock()
        m.set_href(g)
        self.assertEqual(m.tostring(), '<use xlink:href="#test" />')

    def test_object_link_auto_id(self):
        g = Group()
        m = Mock()
        m.set_href(g)
        self.assertTrue(re.match('^<use xlink:href="#id\d+" />$', m.tostring()))

if __name__=='__main__':
    unittest.main()