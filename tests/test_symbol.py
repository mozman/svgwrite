#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test symbol element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import Symbol, Group, parameter
from svgwrite.interface import IViewBox, ITransform

class TestSymbol(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        symbol = Symbol()
        self.assertTrue(isinstance(symbol, IViewBox))
        self.assertFalse(isinstance(symbol, ITransform))
        self.assertEqual(symbol.tostring(), "<symbol />")

    def test_add_subelement(self):
        symbol = Symbol(id='symbol')
        group = Group(id='group')
        symbol.add(group)
        self.assertEqual(symbol.tostring(), '<symbol id="symbol"><g id="group" /></symbol>')

    def test_add_group(self):
        symbol = Symbol(id='symbol')
        group = symbol.group(id='group') # implicit call of add
        self.assertEqual(symbol.tostring(), '<symbol id="symbol"><g id="group" /></symbol>')


if __name__=='__main__':
    unittest.main()