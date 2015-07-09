#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.container import Use, Group
from svgwrite.utils import AutoID

class TestUse(unittest.TestCase):
    def test_constructor(self):
        use = Use('#an_id', x=10, y=20, width=100, height=200)
        self.assertEqual(use.tostring(), '<use height="200" width="100" x="10" xlink:href="#an_id" y="20" />')

    def test_constructor2(self):
        use = Use('#an_id', insert=(10, 20), size=(100, 200))
        self.assertEqual(use.tostring(), '<use height="200" width="100" x="10" xlink:href="#an_id" y="20" />')

    def test_object_link(self):
        g = Group(id='test')
        use = Use(g)
        self.assertEqual(use.tostring(), '<use xlink:href="#test" />')

    def test_object_link_auto_id(self):
        AutoID(999) # set next id to 999
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
