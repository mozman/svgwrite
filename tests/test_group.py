#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test group element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.container import Group

class TestGroup(unittest.TestCase):
    def test_constructor(self):
        g = Group()
        self.assertEqual(g.tostring(), "<g />")

    def test_add_subelement(self):
        group = Group(id='group')
        subgroup = Group(id='subgroup')
        group.add(subgroup)
        self.assertEqual(group.tostring(), '<g id="group"><g id="subgroup" /></g>')

    def test_add_group(self):
        group = Group(id='group')
        subgroup = group.add(Group(id='subgroup'))
        self.assertEqual(group.tostring(), '<g id="group"><g id="subgroup" /></g>')


if __name__=='__main__':
    unittest.main()
