#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test group element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import Group, parameter
from svgwrite.interface import ITransform

class TestGroup(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        g = Group()
        self.assertTrue(isinstance(g, ITransform))
        self.assertEqual(g.tostring(), "<g />")

    def test_add_subelement(self):
        group = Group(id='group')
        subgroup = Group(id='subgroup')
        group.add(subgroup)
        self.assertEqual(group.tostring(), '<g id="group"><g id="subgroup" /></g>')

    def test_add_group(self):
        group = Group(id='group')
        subgroup = group.group(id='subgroup') # implicit call of add
        self.assertEqual(group.tostring(), '<g id="group"><g id="subgroup" /></g>')


if __name__=='__main__':
    unittest.main()