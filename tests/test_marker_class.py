#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test marker element
# Created: 24.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest
import re

from svgwrite.container import Marker, Group

class TestMarker(unittest.TestCase):
    def test_constructor(self):
        marker = Marker(id='test', orient='auto', debug=True, profile='full')
        self.assertEqual(marker.tostring(), '<marker id="test" orient="auto" />')

    def test_add_subelement(self):
        marker = Marker(id='test', debug=True, profile='full')
        marker.add(Group())
        self.assertEqual(marker.tostring(), '<marker id="test"><g /></marker>')

    def test_add_subelement_with_autoid(self):
        marker = Marker(debug=True, profile='full')
        marker.add(Group())
        self.assertTrue(
            re.match('^<marker id="id\d+"><g /></marker>$',
                     marker.tostring()), "getting an autoid for class Marker failed.")

    def test_insert(self):
        marker = Marker(id='test', insert=(1, 2), debug=True, profile='full')
        self.assertEqual(marker.tostring(), '<marker id="test" refX="1" refY="2" />')

    def test_size(self):
        marker = Marker(id='test', size=(1, 2), debug=True, profile='full')
        self.assertEqual(marker.tostring(), '<marker id="test" markerHeight="2" markerWidth="1" />')

    def test_orient_rad(self):
        marker = Marker(id='test', orient='3.1415rad', debug=True, profile='full')
        self.assertEqual(marker.tostring(), '<marker id="test" orient="3.1415rad" />')

    def test_orient_number(self):
        marker = Marker(id='test', orient=30, debug=True, profile='full')
        self.assertEqual(marker.tostring(), '<marker id="test" orient="30" />')

if __name__=='__main__':
    unittest.main()
