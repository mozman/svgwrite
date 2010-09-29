#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test path class
# Created: 18.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.path import Path
from svgwrite import parameter

class TestPath(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)
        parameter.set_profile('full')

    def test_constructor(self):
        p = Path(pathLength=100)
        self.assertEqual(p['pathLength'], 100)
        self.assertEqual(p.tostring(), '<path pathLength="100" />')

        # init path with command-string
        p = Path(d='M 10,7')
        self.assertEqual(p.tostring(), '<path d="M 10,7" />')

        # init path with a tuple of values
        p = Path(d=('M', 9, 9))
        self.assertEqual(p.tostring(), '<path d="M 9 9" />')

    def test_flat_commands(self):
        p = Path()
        self.assertEqual(p.tostring(), '<path />')
        # push separated commands and values
        p.push('M', 100, 100, 100, 200)
        self.assertEqual(p.tostring(), '<path d="M 100 100 100 200" />')

        # push commands strings
        p = Path()
        p.push('M 100 100 100 200')
        self.assertEqual(p.tostring(), '<path d="M 100 100 100 200" />')


        p = Path(d=('M 10', 7))
        p.push('l', 100., 100.)
        p.push('v 100.7 200.1')
        self.assertEqual(p.tostring(), '<path d="M 10 7 l 100.0 100.0 v 100.7 200.1" />')

    def test_nested_commands(self):
        p = Path(d=('M 1,2', ['L', (7, 7, 'H 1 2 3 4 5')]))
        self.assertEqual(p.tostring(), '<path d="M 1,2 L 7 7 H 1 2 3 4 5" />')

if __name__=='__main__':
    unittest.main()