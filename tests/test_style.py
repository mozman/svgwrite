#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test style element
# Created: 27.05.2012
# Copyright (C) 2012, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.container import Style

class TestScript(unittest.TestCase):
    def test_content(self):
        style = Style(content='.red {fill: red};')
        result = style.tostring()
        self.assertEqual(result, '<style type="text/css"><![CDATA[.red {fill: red};]]></style>')

if __name__=='__main__':
    unittest.main()
