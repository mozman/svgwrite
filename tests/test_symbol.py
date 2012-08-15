#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test symbol element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.container import Symbol, Group

class TestSymbol(unittest.TestCase):
    def test_constructor(self):
        symbol = Symbol()
        self.assertEqual(symbol.tostring(), "<symbol />")

    def test_add_subelement(self):
        symbol = Symbol(id='symbol')
        group = Group(id='group')
        symbol.add(group)
        self.assertEqual(symbol.tostring(), '<symbol id="symbol"><g id="group" /></symbol>')

    def test_add_group(self):
        symbol = Symbol(id='symbol')
        group = symbol.add(Group(id='group')) # implicit call of add
        self.assertEqual(symbol.tostring(), '<symbol id="symbol"><g id="group" /></symbol>')

if __name__=='__main__':
    unittest.main()
