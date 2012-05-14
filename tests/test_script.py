#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test svg element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite.container import Script

class TestUse(unittest.TestCase):
    def test_constructor(self):
        script = Script('test.js', "text/ecmascript")
        self.assertEqual(script.tostring(), '<script type="text/ecmascript" xlink:href="test.js" />')

if __name__=='__main__':
    unittest.main()