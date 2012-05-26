#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import unittest

from svgwrite.container import Script

class TestScript(unittest.TestCase):
    def test_link(self):
        script = Script('test.js')
        self.assertEqual(script.tostring(), '<script xlink:href="test.js" />')

    def test_type(self):
        script = Script('test.py', type='application/python')
        self.assertEqual(script.tostring(), '<script type="application/python" xlink:href="test.py" />')


if __name__=='__main__':
    unittest.main()
