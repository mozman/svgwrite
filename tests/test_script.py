#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test script element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.container import Script

class TestScript(unittest.TestCase):
    def test_link(self):
        script = Script('test.js')
        self.assertEqual(script.tostring(), '<script xlink:href="test.js" />')

    def test_type(self):
        script = Script('test.py', type='application/python')
        self.assertEqual(script.tostring(), '<script type="application/python" xlink:href="test.py" />')

    def test_content(self):
        script = Script(content='function test(){return "<>"};')
        result = script.tostring()
        self.assertEqual(result, '<script><![CDATA[function test(){return "<>"};]]></script>')

if __name__=='__main__':
    unittest.main()
