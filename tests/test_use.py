#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import Use, Group, parameter

from svgwrite.interface import ITransform, IXLink

class TestUse(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        use = Use('an_id')
        self.assertTrue(isinstance(use, ITransform))
        self.assertTrue(isinstance(use, IXLink))
        self.assertEqual(use.tostring(), '<use xlink:href="#an_id" />')

    def test_object_link(self):
        g = Group(id='test')
        use = Use(g)
        self.assertEqual(use.tostring(), '<use xlink:href="#test" />')

    def test_object_link_auto_id(self):
        parameter._set_auto_id(999) # only for testing !!!!
        g = Group()
        use = Use(g)
        self.assertEqual(use.tostring(), '<use xlink:href="#id999" />')

    def test_object_link_change_id(self):
        g = Group(id=999)
        self.assertEqual(g['id'], 999)
        use = Use(g)
        # change 'id' after assigning to <Use> object
        g['id'] = 'newid'
        self.assertEqual(use.tostring(), '<use xlink:href="#newid" />')

if __name__=='__main__':
    unittest.main()