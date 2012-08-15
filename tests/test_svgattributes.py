#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test SVGAttribute
# Created: 12.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.data.types import SVGAttribute, SVGMultiAttribute

class TestSVGMultiAttribute(unittest.TestCase):
    def setUp(self):
        self.ma = SVGMultiAttribute({
            '*': SVGAttribute('x',
                              anim=True,
                              types=frozenset(['coordinate']),
                              const=frozenset(['star'])),
            'text tref tspan': SVGAttribute('x',
                                            anim=False,
                                            types=frozenset(['list-of-coordinate']),
                                            const=frozenset(['text']))
            }
        )

    def test_no_default(self):
        ma = SVGMultiAttribute({
            'a': SVGAttribute('x',
                              anim=True,
                              types=frozenset(['coordinate']),
                              const=frozenset(['star'])),
            'b': SVGAttribute('x',
                              anim=False,
                              types=frozenset(['list-of-coordinate']),
                              const=frozenset(['text']))
            }
        )
        self.assertTrue('coordinate' in ma.get_types('c'))

    def test_get_types(self):
        coordinate = frozenset(['coordinate'])
        list_of_coordinates = frozenset(['list-of-coordinate'])

        self.assertEqual(coordinate, self.ma.get_types('line')) # default attribute
        self.assertEqual(coordinate, self.ma.get_types()) # default attribute
        self.assertEqual(list_of_coordinates, self.ma.get_types('text'))
        self.assertEqual(list_of_coordinates, self.ma.get_types('tref'))
        self.assertEqual(list_of_coordinates, self.ma.get_types('tspan'))

    def test_get_anim(self):
        self.assertTrue(self.ma.get_anim('line')) # default attribute
        self.assertTrue(self.ma.get_anim()) # default attribute
        self.assertFalse(self.ma.get_anim('text'))
        self.assertFalse(self.ma.get_anim('tref'))
        self.assertFalse(self.ma.get_anim('tspan'))

    def test_get_const(self):
        star = frozenset(['star'])
        text = frozenset(['text'])

        self.assertEqual(star, self.ma.get_const('line')) # default attribute
        self.assertEqual(star, self.ma.get_const()) # default attribute
        self.assertEqual(text, self.ma.get_const('text'))
        self.assertEqual(text, self.ma.get_const('tref'))
        self.assertEqual(text, self.ma.get_const('tspan'))

    def test_init_error(self):
        # different attribute names
        ma = { '*' : SVGAttribute('x', True, [], []),
               'text' : SVGAttribute('y', False, [], [])
               }
        self.assertRaises(ValueError, SVGMultiAttribute, ma)

if __name__=='__main__':
    unittest.main()
