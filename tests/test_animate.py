#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test animate
# Created: 31.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.animate import Set, Animate, AnimateColor, AnimateMotion, AnimateTransform


class TestSet(unittest.TestCase):
    def test_constructor(self):
        s = Set(debug=True)
        self.assertEqual(s.tostring(), '<set />')

    def test_set_href(self):
        s = Set(href='#test', debug=True)
        self.assertEqual(s.tostring(), '<set xlink:href="#test" />')


    def test_set_target(self):
        s = Set(debug=True)
        s.set_target('x', 'XML')
        self.assertEqual(s.tostring(), '<set attributeName="x" attributeType="XML" />')

    def test_set_event(self):
        s = Set(debug=True)
        s.set_event('test1', 'test2', 'test3', 'test4')
        self.assertEqual(s.tostring(), '<set onbegin="test1" onend="test2" onload="test4" onrepeat="test3" />')

    def test_set_timing(self):
        s = Set(debug=True)
        s.set_timing('indefinite', 'indefinite', 'indefinite', 'media', 'media',
                     'always', 'indefinite', 'indefinite')
        self.assertEqual(s.tostring(), '<set begin="indefinite" dur="indefinite" ' \
                        'end="indefinite" max="media" min="media" ' \
                        'repeatCount="indefinite" repeatDur="indefinite" restart="always" />')

    def test_set_timing_1s(self):
        s = Set(debug=True)
        s.set_timing('1s')
        result = s.tostring()
        self.assertEqual(result, '<set begin="1s" />')

    def test_freeze(self):
        s = Set(debug=True)
        s.freeze()
        self.assertEqual(s.tostring(), '<set fill="freeze" />')


class TestAnimate(unittest.TestCase):
    def test_constructor(self):
        a = Animate('x', debug=True)
        self.assertEqual(a.tostring(), '<animate attributeName="x" />')

    def test_freeze(self):
        a = Animate(debug=True)
        a.freeze()
        self.assertEqual(a.tostring(), '<animate fill="freeze" />')

    def test_set_value(self):
        a = Animate(debug=True)
        a.set_value('0;1;2', 'linear', '0', '0 0 0 0', 0, 0, 0)
        self.assertEqual(a.tostring(),
                         '<animate by="0" calcMode="linear" from="0" ' \
                         'keySplines="0 0 0 0" keyTimes="0" to="0" '\
                         'values="0;1;2" />')

    def test_values_string(self):
        s = Animate(values="1;2;3", debug=True)
        self.assertEqual(s.tostring(), '<animate values="1;2;3" />')

    def test_values_list(self):
        s = Animate(values=[1, 2, 3], debug=True)
        self.assertEqual(s.tostring(), '<animate values="1;2;3" />')

    def test_values_int(self):
        s = Animate(values=(3,), debug=True)
        self.assertEqual(s.tostring(), '<animate values="3" />')

    def test_values_colors(self):
        s = Animate(values='#000000;#0000ff;#00ff00;#ff0000', debug=True)
        self.assertEqual(s.tostring(), '<animate values="#000000;#0000ff;#00ff00;#ff0000" />')


class TestAnimateColor(unittest.TestCase):
    def test_freeze(self):
        s = AnimateColor(debug=True)
        s.freeze()
        self.assertEqual(s.tostring(), '<animateColor fill="freeze" />')


class TestAnimateMotion(unittest.TestCase):
    def test_freeze(self):
        s = AnimateMotion(debug=True)
        s.freeze()
        self.assertEqual(s.tostring(), '<animateMotion fill="freeze" />')

    def test_init_with_path(self):
        s = AnimateMotion('m 0 0', debug=True)
        self.assertEqual(s.tostring(), '<animateMotion path="m 0 0" />')

    def test_set_value(self):
        a = AnimateMotion(debug=True)
        a.set_value('m 0 0', 'linear', '0', 'auto')
        self.assertEqual(a.tostring(),
                         '<animateMotion calcMode="linear" ' \
                         'keyPoints="0" path="m 0 0" '\
                         'rotate="auto" />')


class TestAnimateTransform(unittest.TestCase):
    def test_freeze(self):
        s = AnimateTransform('translate', debug=True)
        s.freeze()
        self.assertEqual(s.tostring(), '<animateTransform fill="freeze" type="translate" />')


if __name__=='__main__':
    unittest.main()
