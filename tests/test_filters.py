#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test filters module
# Created: 04.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

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


class Test_feComposite(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        pf = f.feComposite('input1', in2='input2')
        self.assertEqual(pf.tostring(), '<feComposite in="input1" in2="input2" />')

    def test_operator(self):
        f = filters.Filter()
        self.assertEqual(f.feComposite('input1', operator='over').tostring(),
                         '<feComposite in="input1" operator="over" />')
        self.assertEqual(f.feComposite('input1', operator='in').tostring(),
                         '<feComposite in="input1" operator="in" />')
        self.assertEqual(f.feComposite('input1', operator='out').tostring(),
                         '<feComposite in="input1" operator="out" />')
        self.assertEqual(f.feComposite('input1', operator='xor').tostring(),
                         '<feComposite in="input1" operator="xor" />')
        self.assertEqual(f.feComposite('input1', operator='arithmetic').tostring(),
                         '<feComposite in="input1" operator="arithmetic" />')

    def test_k1k2k3k4(self):
        f = filters.Filter()
        pf = f.feComposite('input1', k1=1, k2=2, k3=3, k4=4)
        self.assertEqual(pf.tostring(), '<feComposite in="input1" k1="1" k2="2" k3="3" k4="4" />')


class Test_feConvolveMatrix(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        pf = f.feConvolveMatrix('input1')
        self.assertEqual(pf.tostring(), '<feConvolveMatrix in="input1" />')

    def test_order(self):
        f = filters.Filter()
        pf = f.feConvolveMatrix('input1', order='1 2')
        self.assertEqual(pf.tostring(), '<feConvolveMatrix in="input1" order="1 2" />')

    def test_kernelMatrix(self):
        f = filters.Filter()
        pf = f.feConvolveMatrix('input1', kernelMatrix='1 2 3 4')
        self.assertEqual(pf.tostring(), '<feConvolveMatrix in="input1" kernelMatrix="1 2 3 4" />')

    def test_divisor_and_bias(self):
        f = filters.Filter()
        pf = f.feConvolveMatrix('input1', divisor=2.5, bias=0.5)
        self.assertEqual(pf.tostring(), '<feConvolveMatrix bias="0.5" divisor="2.5" in="input1" />')

    def test_targetX_and_targetY(self):
        f = filters.Filter()
        pf = f.feConvolveMatrix('input1', targetX=1, targetY=2)
        self.assertEqual(pf.tostring(), '<feConvolveMatrix in="input1" targetX="1" targetY="2" />')

    def test_edgeMode(self):
        f = filters.Filter()
        self.assertEqual(f.feConvolveMatrix('input1', edgeMode='duplicate').tostring(),
                         '<feConvolveMatrix edgeMode="duplicate" in="input1" />')
        self.assertEqual(f.feConvolveMatrix('input1', edgeMode='wrap').tostring(),
                         '<feConvolveMatrix edgeMode="wrap" in="input1" />')
        self.assertEqual(f.feConvolveMatrix('input1', edgeMode='none').tostring(),
                         '<feConvolveMatrix edgeMode="none" in="input1" />')

    def test_preserveAlpha(self):
        f = filters.Filter()
        self.assertEqual(f.feConvolveMatrix('input1', preserveAlpha='true').tostring(),
                         '<feConvolveMatrix in="input1" preserveAlpha="true" />')
        self.assertEqual(f.feConvolveMatrix('input1', preserveAlpha='false').tostring(),
                         '<feConvolveMatrix in="input1" preserveAlpha="false" />')

    def test_kernelUnitLength(self):
        f = filters.Filter()
        self.assertEqual(f.feConvolveMatrix('input1', kernelUnitLength=2).tostring(),
                         '<feConvolveMatrix in="input1" kernelUnitLength="2" />')


class Test_feDiffuseLighting(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feDiffuseLighting('input1').tostring(),
                         '<feDiffuseLighting in="input1" />')

    def test_surfaceScale(self):
        f = filters.Filter()
        self.assertEqual(f.feDiffuseLighting('input1', surfaceScale=1).tostring(),
                         '<feDiffuseLighting in="input1" surfaceScale="1" />')

    def test_diffuseConstant(self):
        f = filters.Filter()
        self.assertEqual(f.feDiffuseLighting('input1', diffuseConstant=1).tostring(),
                         '<feDiffuseLighting diffuseConstant="1" in="input1" />')

    def test_kernelUnitLength(self):
        f = filters.Filter()
        self.assertEqual(f.feDiffuseLighting('input1', kernelUnitLength=2).tostring(),
                         '<feDiffuseLighting in="input1" kernelUnitLength="2" />')

    def test_lighting_color(self):
        f = filters.Filter()
        self.assertEqual(f.feDiffuseLighting('input1', lighting_color='yellow').tostring(),
                         '<feDiffuseLighting in="input1" lighting-color="yellow" />')


class Test_feDisplacementMap(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feDisplacementMap('input1', in2="input2").tostring(),
                         '<feDisplacementMap in="input1" in2="input2" />')

    def test_scale(self):
        f = filters.Filter()
        self.assertEqual(f.feDisplacementMap('input1', scale=2).tostring(),
                         '<feDisplacementMap in="input1" scale="2" />')

    def test_xChannelSelector_yChannelSelector(self):
        f = filters.Filter()
        self.assertEqual(f.feDisplacementMap('input1', xChannelSelector="R", yChannelSelector="G").tostring(),
                         '<feDisplacementMap in="input1" xChannelSelector="R" yChannelSelector="G" />')


class Test_feFlood(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feFlood().tostring(),
                         '<feFlood />')

    def test_flood_color(self):
        f = filters.Filter()
        self.assertEqual(f.feFlood(flood_color="red").tostring(),
                         '<feFlood flood-color="red" />')

    def test_flood_opacity(self):
        f = filters.Filter()
        self.assertEqual(f.feFlood(flood_opacity=0.5).tostring(),
                         '<feFlood flood-opacity="0.5" />')


class Test_feGaussianBlur(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feGaussianBlur("input1").tostring(),
                         '<feGaussianBlur in="input1" />')

    def test_stdDeviation(self):
        f = filters.Filter()
        self.assertEqual(f.feGaussianBlur("input1", stdDeviation="1 2").tostring(),
                         '<feGaussianBlur in="input1" stdDeviation="1 2" />')


class Test_feImage(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feImage("./image.png").tostring(),
                         '<feImage xlink:href="./image.png" />')


class Test_feMerge(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feMerge(['Layer1', 'Layer2']).tostring(),
                         '<feMerge><feMergeNode in="Layer1" /><feMergeNode in="Layer2" /></feMerge>')

    def test_layers(self):
        f = filters.Filter()
        merge = f.feMerge(['Layer1', 'Layer2'])
        merge.feMergeNode(('Layer3', ))
        self.assertEqual(merge.tostring(),
                         '<feMerge><feMergeNode in="Layer1" /><feMergeNode in="Layer2" />'
                         '<feMergeNode in="Layer3" /></feMerge>')


class Test_feMorphology(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feMorphology("input1").tostring(),
                         '<feMorphology in="input1" />')

    def test_operator(self):
        f = filters.Filter()
        self.assertEqual(f.feMorphology("input1", operator="erode").tostring(),
                         '<feMorphology in="input1" operator="erode" />')
        self.assertEqual(f.feMorphology("input1", operator="dilate").tostring(),
                         '<feMorphology in="input1" operator="dilate" />')

    def test_radius(self):
        f = filters.Filter()
        self.assertEqual(f.feMorphology("input1", radius="1,2").tostring(),
                         '<feMorphology in="input1" radius="1,2" />')


class Test_feOffset(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feOffset("input1").tostring(),
                         '<feOffset in="input1" />')

    def test_dx_dy(self):
        f = filters.Filter()
        self.assertEqual(f.feOffset("input1", dx=10, dy=20).tostring(),
                         '<feOffset dx="10" dy="20" in="input1" />')


class Test_feSpecularLighting(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feSpecularLighting("input1").tostring(),
                         '<feSpecularLighting in="input1" />')

    def test_surfaceScale(self):
        f = filters.Filter()
        self.assertEqual(f.feSpecularLighting("input1", surfaceScale=7).tostring(),
                         '<feSpecularLighting in="input1" surfaceScale="7" />')

    def test_specularExponent(self):
        f = filters.Filter()
        self.assertEqual(f.feSpecularLighting("input1", specularExponent=7).tostring(),
                         '<feSpecularLighting in="input1" specularExponent="7" />')

    def test_kernelUnitLength(self):
        f = filters.Filter()
        self.assertEqual(f.feSpecularLighting("input1", kernelUnitLength="1,2").tostring(),
                         '<feSpecularLighting in="input1" kernelUnitLength="1,2" />')

    def test_lighting_color(self):
        f = filters.Filter()
        self.assertEqual(f.feSpecularLighting('input1', lighting_color='yellow').tostring(),
                         '<feSpecularLighting in="input1" lighting-color="yellow" />')


class Test_feTile(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feTile("input1").tostring(),
                         '<feTile in="input1" />')


class Test_feTurbulence(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence().tostring(),
                         '<feTurbulence />')

    def test_baseFrequency(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence(baseFrequency="1,2").tostring(),
                         '<feTurbulence baseFrequency="1,2" />')

    def test_numOctaves(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence(numOctaves="1").tostring(),
                         '<feTurbulence numOctaves="1" />')

    def test_seed(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence(seed="1").tostring(),
                         '<feTurbulence seed="1" />')

    def test_stitchTiles(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence(stitchTiles="stitch").tostring(),
                         '<feTurbulence stitchTiles="stitch" />')

    def test_type(self):
        f = filters.Filter()
        self.assertEqual(f.feTurbulence(type_="fractalNoise").tostring(),
                         '<feTurbulence type="fractalNoise" />')
        self.assertEqual(f.feTurbulence(type_="turbulence").tostring(),
                         '<feTurbulence type="turbulence" />')


class TestDistantLight(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        fp = f.feDiffuseLighting('input1')
        ls = fp.feDistantLight()
        self.assertEqual(ls.tostring(), '<feDistantLight />')
        self.assertEqual(fp.tostring(), '<feDiffuseLighting in="input1"><feDistantLight /></feDiffuseLighting>')
        self.assertEqual(f.tostring(), '<filter><feDiffuseLighting in="input1"><feDistantLight /></feDiffuseLighting></filter>')

    def test_all_parmeters(self):
        f = filters.Filter()
        ls = f.feDiffuseLighting('input1').feDistantLight(1, 2)
        self.assertEqual(ls.tostring(), '<feDistantLight azimuth="1" elevation="2" />')


class TestPointLight(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        fp = f.feDiffuseLighting('input1')
        ls = fp.fePointLight()
        self.assertEqual(ls.tostring(), '<fePointLight />')
        self.assertEqual(fp.tostring(), '<feDiffuseLighting in="input1"><fePointLight /></feDiffuseLighting>')
        self.assertEqual(f.tostring(), '<filter><feDiffuseLighting in="input1"><fePointLight /></feDiffuseLighting></filter>')

    def test_all_parmeters(self):
        f = filters.Filter()
        ls = f.feDiffuseLighting('input1').fePointLight(source=(1,2,3))
        self.assertEqual(ls.tostring(), '<fePointLight x="1" y="2" z="3" />')


class TestSpotLight(unittest.TestCase):
    def test_constructor(self):
        f = filters.Filter()
        fp = f.feDiffuseLighting('input1')
        ls = fp.feSpotLight()
        self.assertEqual(ls.tostring(), '<feSpotLight />')
        self.assertEqual(fp.tostring(), '<feDiffuseLighting in="input1"><feSpotLight /></feDiffuseLighting>')
        self.assertEqual(f.tostring(), '<filter><feDiffuseLighting in="input1"><feSpotLight /></feDiffuseLighting></filter>')

    def test_all_parmeters(self):
        f = filters.Filter()
        ls = f.feDiffuseLighting('input1').feSpotLight(source=(1, 2, 3), target=(4, 5, 6),
                                                       specularExponent=2,
                                                       limitingConeAngle=15)
        self.assertEqual(ls.tostring(), '<feSpotLight limitingConeAngle="15" '
                         'pointsAtX="4" pointsAtY="5" pointsAtZ="6" '
                         'specularExponent="2" x="1" y="2" z="3" />')


if __name__ == '__main__':
    unittest.main()
