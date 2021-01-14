#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test drawing module
# Created: 11.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License
import unittest
from io import StringIO
from pathlib import Path

from svgwrite.drawing import Drawing
from svgwrite.container import Group


class TestDrawingFullProfile(unittest.TestCase):
    def test_empty_drawing(self):
        dwg = Drawing()
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="full" height="100%" version="1.1" '
                                 'width="100%" xmlns="http://www.w3.org/2000/svg" '
                                 'xmlns:ev="http://www.w3.org/2001/xml-events" '
                                 'xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

    def test_stylesheet(self):
        dwg = Drawing()
        dwg.add_stylesheet('test.css', 'Test')
        f = StringIO()
        dwg.write(f)
        result = f.getvalue()
        f.close()
        self.assertEqual(result, '<?xml version="1.0" encoding="utf-8" ?>\n'
                                 '<?xml-stylesheet href="test.css" type="text/css" title="Test" alternate="no" media="screen"?>\n'
                                 '<svg baseProfile="full" height="100%" version="1.1" width="100%" '
                                 'xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" '
                                 'xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

    def test_save(self):
        fn = Path('test_drawing.svg')
        if fn.exists():
            fn.unlink()
        dwg = Drawing(fn)
        dwg.save()
        self.assertTrue(fn.exists())
        fn.unlink()

    def test_save_as(self):
        fn = Path('test_drawing.svg')
        if fn.exists():
            fn.unlink()
        dwg = Drawing()
        dwg.saveas(str(fn))
        self.assertTrue(fn.exists())
        fn.unlink()

    def test_non_us_ascii_chars(self):
        dwg = Drawing()
        dwg.set_desc('öäü')
        f = StringIO()
        dwg.write(f)
        result = f.getvalue()
        f.close()
        self.assertEqual(result,
                         '<?xml version="1.0" encoding="utf-8" ?>\n'
                         '<svg baseProfile="full" height="100%" version="1.1" width="100%" '
                         'xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" '
                         'xmlns:xlink="http://www.w3.org/1999/xlink">'
                         '<title>öäü</title><defs /></svg>')


class TestDrawingTinyProfile(unittest.TestCase):
    def test_empty_drawing(self):
        dwg = Drawing(profile="tiny")
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="tiny" height="100%" version="1.2" '
                                 'width="100%" xmlns="http://www.w3.org/2000/svg" '
                                 'xmlns:ev="http://www.w3.org/2001/xml-events" '
                                 'xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')

    def test_stylesheet(self):
        dwg = Drawing(profile="tiny")
        dwg.add_stylesheet('test.css', 'Test')
        f = StringIO()
        dwg.write(f)
        result = f.getvalue()
        f.close()
        self.assertEqual(result, '<?xml version="1.0" encoding="utf-8" ?>\n'
                                 '<?xml-stylesheet href="test.css" type="text/css" title="Test" alternate="no" media="screen"?>\n'
                                 '<svg baseProfile="tiny" height="100%" version="1.2" width="100%" '
                                 'xmlns="http://www.w3.org/2000/svg" '
                                 'xmlns:ev="http://www.w3.org/2001/xml-events" '
                                 'xmlns:xlink="http://www.w3.org/1999/xlink"><defs /></svg>')


class TestDefs(unittest.TestCase):
    def test_simple_defs(self):
        dwg = Drawing()
        g = dwg.defs.add(Group(id='test'))
        inner_g = g.add(Group(id='innerTest'))
        result = dwg.tostring()
        self.assertEqual(result, '<svg baseProfile="full" height="100%" version="1.1" '
                                 'width="100%" xmlns="http://www.w3.org/2000/svg" '
                                 'xmlns:ev="http://www.w3.org/2001/xml-events" '
                                 'xmlns:xlink="http://www.w3.org/1999/xlink">'
                                 '<defs><g id="test"><g id="innerTest" /></g></defs></svg>')


if __name__ == '__main__':
    unittest.main()
