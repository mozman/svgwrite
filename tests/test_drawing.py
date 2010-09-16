#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test drawing module
# Created: 11.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest
from StringIO import StringIO

from svgwrite.parameter import init
from svgwrite.drawing import Drawing
from svgwrite.container import Group

class TestDrawingFullProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='full', debug=True)

    def test_empty_drawing(self):
        dwg = Drawing()
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="full" height="100%" version="1.1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

    def test_stylesheet(self):
        dwg = Drawing()
        dwg.add_stylesheet('test.css', 'Test')
        f = StringIO()
        dwg.write(f)
        result = f.getvalue()
        f.close()
        self.assertEqual(result, '<?xml version="1.0" encoding="utf-8" ?>\n' \
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n' \
            '<?xml-stylesheet href="test.css" type="text/css" title="Test" alternate="no" media="screen"?>\n'
            '<svg baseProfile="full" height="100%" version="1.1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

class TestDrawingTinyProfile(unittest.TestCase):
    def setUp(self):
        init(baseProfile='tiny', debug=True)

    def test_empty_drawing(self):
        dwg = Drawing()
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="tiny" height="100%" version="1.2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

    def test_stylesheet(self):
        dwg = Drawing()
        dwg.add_stylesheet('test.css', 'Test')
        f = StringIO()
        dwg.write(f)
        result = f.getvalue()
        f.close()
        # no DOCTYPE! for tiny profile
        self.assertEqual(result, '<?xml version="1.0" encoding="utf-8" ?>\n' \
            '<?xml-stylesheet href="test.css" type="text/css" title="Test" alternate="no" media="screen"?>\n'
            '<svg baseProfile="tiny" height="100%" version="1.2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')
class TestDefs(unittest.TestCase):
    def setUp(self):
        init(baseProfile='full', debug=True)

    def test_simple_defs(self):
        dwg = Drawing()
        g = dwg.defs.group(id='test')
        inner_g = g.group(id='innerTest')
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="full" height="100%" version="1.1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">' \
          '<defs><g id="test"><g id="innerTest" /></g></defs></svg>')


if __name__=='__main__':
    unittest.main()