#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test filters module
# Created: 04.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import unittest

from svgwrite import filters

class TestFilter(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter(profile='full', debug=True)
        self.assertEqual(f.tostring(), '<filter />')

    def test_constructor_params(self):
        f = filters.Filter(start=(10,20), size=(30,40), inherit='#test', profile='full', debug=True)
        self.assertEqual(f.tostring(), '<filter height="40" width="30" x="10" xlink:href="#test" y="20" />')

    def test_filterRes(self):
        f = filters.Filter(resolution=300, profile='full', debug=True)
        self.assertEqual(f.tostring(), '<filter filterRes="300" />')
        f = filters.Filter(resolution=(300, 400), profile='full', debug=True)
        self.assertEqual(f.tostring(), '<filter filterRes="300 400" />')
        f = filters.Filter(resolution="300 400", profile='full', debug=True)
        self.assertEqual(f.tostring(), '<filter filterRes="300 400" />')

class MockFRI(filters._FilterRequireInput):
    elementname = 'feBlend'

class TestFilterRequireInput(unittest.TestCase):
    def test_constructor(self):
        f = MockFRI('input')
        self.assertEqual(f.tostring(), '<feBlend in="input" />')

    def test_constructor_with_all_params(self):
        f = MockFRI('input', start=(10, 20), size=(30, 40), result='output')
        self.assertEqual(f.tostring(), '<feBlend height="40" in="input" result="output" width="30" x="10" y="20" />')

class Test_feBlend(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        f.feBlend('input1', in2='input2', mode='normal')
        self.assertEqual(f.tostring(), '<filter><feBlend in="input1" in2="input2" mode="normal" /></filter>')

class Test_feColorMatrix(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        f.feColorMatrix('input1', type_='matrix', values='0 0 0')
        self.assertEqual(f.tostring(), '<filter><feColorMatrix in="input1" type="matrix" values="0 0 0" /></filter>')

class Test_feComponentTransfer(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        f.feComponentTransfer('input1')
        self.assertEqual(f.tostring(), '<filter><feComponentTransfer in="input1" /></filter>')

    def test_add_FuncR(self):
        f = filters.Filter()
        fct = f.feComponentTransfer('input1')
        func = fct.feFuncR('identity')
        self.assertEqual(fct.tostring(), '<feComponentTransfer in="input1"><feFuncR type="identity" /></feComponentTransfer>')
        self.assertEqual(func.tostring(), '<feFuncR type="identity" />')

    def test_add_FuncG(self):
        f = filters.Filter()
        fct = f.feComponentTransfer('input1')
        func = fct.feFuncG('table')
        self.assertEqual(func.tostring(), '<feFuncG type="table" />')

    def test_add_FuncB(self):
        f = filters.Filter()
        fct = f.feComponentTransfer('input1')
        func = fct.feFuncB('discrete')
        self.assertEqual(func.tostring(), '<feFuncB type="discrete" />')

    def test_add_FuncA(self):
        f = filters.Filter()
        fct = f.feComponentTransfer('input1')
        func = fct.feFuncA('gamma')
        self.assertEqual(func.tostring(), '<feFuncA type="gamma" />')

    def test_FuncR_all_params(self):
        f = filters.Filter()
        fct = f.feComponentTransfer('input1')
        func = fct.feFuncR('identity', tableValues="1,2", slope=1, intercept=0,
                           amplitude=0, exponent=1, offset=0)
        self.assertEqual(func.tostring(), '<feFuncR amplitude="0" exponent="1" '\
                         'intercept="0" offset="0" slope="1" '\
                         'tableValues="1,2" type="identity" />')

if __name__=='__main__':
    unittest.main()