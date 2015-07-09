#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test ITransform interface
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import sys
import unittest

from svgwrite.params import Parameter
from svgwrite.base import BaseElement
from svgwrite.mixins import Transform

class Mock(BaseElement, Transform):
    elementname = 'g'
    _parameter = Parameter(True, 'full')

class TestITransfer(unittest.TestCase):
    def test_mock_class(self):
        m = Mock()
        self.assertEqual(m.tostring(), '<g />')

    def test_translate_tx(self):
        m = Mock()
        m.translate(tx=10)
        self.assertEqual(m.tostring(), '<g transform="translate(10)" />')

    def test_translate_tx_ty(self):
        m = Mock()
        # strings allowed
        m.translate(tx='10', ty=20)
        self.assertEqual(m.tostring(), '<g transform="translate(10,20)" />')

    def test_translate_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.translate, '10cm')

    def test_rotate(self):
        m = Mock()
        m.rotate(angle=30)
        self.assertEqual(m.tostring(), '<g transform="rotate(30)" />')

    def test_rotate_center(self):
        m = Mock()
        # strings allowed
        m.rotate(angle='30', center=(1,2))
        self.assertEqual(m.tostring(), '<g transform="rotate(30,1,2)" />')

    def test_rotate_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.rotate, '30deg')
        self.assertRaises(TypeError, m.rotate, '30', center=('1cm', '1cm'))

    def test_scale_sx(self):
        m = Mock()
        m.scale(sx=3)
        self.assertEqual(m.tostring(), '<g transform="scale(3)" />')

    def test_scale_sx_sy(self):
        m = Mock()
        m.scale(sx='3', sy=2)
        self.assertEqual(m.tostring(), '<g transform="scale(3,2)" />')

    def test_scale_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.scale, '3cm')
        self.assertRaises(TypeError, m.scale, '3', '2cm')

    def test_skewX(self):
        m = Mock()
        m.skewX(angle=30)
        self.assertEqual(m.tostring(), '<g transform="skewX(30)" />')

    def test_skewX_str(self):
        m = Mock()
        m.skewX(angle='30')
        self.assertEqual(m.tostring(), '<g transform="skewX(30)" />')

    def test_skewX_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.skewX, '3deg')

    def test_skewY(self):
        m = Mock()
        m.skewY(angle=30)
        self.assertEqual(m.tostring(), '<g transform="skewY(30)" />')

    def test_skewY_str(self):
        m = Mock()
        m.skewY(angle='30')
        self.assertEqual(m.tostring(), '<g transform="skewY(30)" />')

    def test_skewY_err(self):
        m = Mock()
        # no units allowed
        self.assertRaises(TypeError, m.skewY, '3deg')

    def test_matrix(self):
        m = Mock()
        m.matrix(1,2,3,4,5,6)
        self.assertEqual(m.tostring(), '<g transform="matrix(1,2,3,4,5,6)" />')

    def test_matrix_too_few_params(self):
        m = Mock()
        self.assertRaises(TypeError, m.matrix, 1, 2, 3, 4, 5)

    def test_combine_tranformation(self):
        m = Mock()
        m.translate(10,20)
        m.scale(2,2)
        self.assertEqual(m.tostring(), '<g transform="translate(10,20) scale(2,2)" />')

    def test_delete_transformation(self):
        m = Mock()
        m.translate(10,20)
        del m.attribs['transform']
        self.assertEqual(m.tostring(), '<g />')

if __name__=='__main__':
    unittest.main()
