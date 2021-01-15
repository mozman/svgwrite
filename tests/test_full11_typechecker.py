#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test full11typechecker
# Created: 04.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.data.typechecker import Full11TypeChecker


class TestFull11TypeChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Full11TypeChecker()

    def test_version(self):
        self.assertEqual(('1.1', 'full'), self.checker.get_version())

    def test_is_anything(self):
        """ Everything is valid. """
        self.assertTrue(self.checker.is_anything('abcdef  :::\n \r \t all is valid äüß'))
        self.assertTrue(self.checker.is_anything(100))
        self.assertTrue(self.checker.is_anything((100, 11)))
        self.assertTrue(self.checker.is_anything(dict(a=100, b=200)))

    def test_is_string(self):
        """ Everything is valid. """
        self.assertTrue(self.checker.is_anything('abcdef  :::\n \r \t all is valid äüß'))
        self.assertTrue(self.checker.is_anything(100))
        self.assertTrue(self.checker.is_anything((100, 11)))
        self.assertTrue(self.checker.is_anything(dict(a=100, b=200)))
        self.assertTrue(self.checker.is_anything(u'äüß'.encode('utf-8')))

    def test_is_number(self):
        """ Integer and Float, also as String '100' or '3.1415'. """
        # big numbers only valid for full profile
        self.assertTrue(self.checker.is_number(100000))
        self.assertTrue(self.checker.is_number(-100000))
        self.assertTrue(self.checker.is_number(3.141592))
        self.assertTrue(self.checker.is_number('100000'))
        self.assertTrue(self.checker.is_number('-100000'))
        self.assertTrue(self.checker.is_number('3.141592'))

    def test_is_not_number(self):
        self.assertFalse(self.checker.is_number( (1,2) ))
        self.assertFalse(self.checker.is_number('manfred'))
        self.assertFalse(self.checker.is_number( dict(a=1, b=2) ))

    def test_is_name(self):
        self.assertTrue(self.checker.is_name('mozman-öäüß'))
        self.assertTrue(self.checker.is_name('mozman:mozman'))
        self.assertTrue(self.checker.is_name('mozman:mozman[2]'))
        # not only strings allowed
        self.assertTrue(self.checker.is_name(100))
        self.assertTrue(self.checker.is_name(100.123))

    def test_is_not_name(self):
        self.assertFalse(self.checker.is_name(''))
        self.assertFalse(self.checker.is_name('mozman,mozman[2]'))
        self.assertFalse(self.checker.is_name('mozman mozman[2]'))
        self.assertFalse(self.checker.is_name('mozman(mozman)[2]'))
        # tuple and dict contains ',', '(', ')' or ' '
        self.assertFalse(self.checker.is_name((100, 200)))
        self.assertFalse(self.checker.is_name(dict(a=100, b=200)))

    def test_is_length(self):
        for value in [' 100px ', ' -100ex ', ' 100em ', ' -100pt ',
                      ' 100pc ', ' 100mm', ' 100cm', ' 100in',
                      ' 5%', 100, 3.1415, 700000, -500000, '100000',
                      '-4000000.45']:
            self.assertTrue(self.checker.is_length(value))

    def test_is_not_length(self):
        for value in [' 100xpx ', ' -100km ', ' 100mi ', (1, 1),
                      dict(a=1, b=2), [1, 2], ' mozman ']:
            self.assertFalse(self.checker.is_length(value))

    def test_is_integer(self):
        """ Integer also as String '100'. """
        # big numbers only valid for full profile
        self.assertTrue(self.checker.is_integer(100000))
        self.assertTrue(self.checker.is_integer(-100000))
        self.assertTrue(self.checker.is_integer('100000'))
        self.assertTrue(self.checker.is_integer('-100000'))

    def test_is_not_integer(self):
        self.assertFalse(self.checker.is_integer( (1,2) ))
        self.assertFalse(self.checker.is_integer('manfred'))
        self.assertFalse(self.checker.is_integer( dict(a=1, b=2) ))
        self.assertFalse(self.checker.is_integer(3.141592))
        self.assertFalse(self.checker.is_integer('3.141592'))

    def test_is_percentage(self):
        self.assertTrue(self.checker.is_percentage(100))
        self.assertTrue(self.checker.is_percentage(50.123))
        self.assertTrue(self.checker.is_percentage(1000))
        self.assertTrue(self.checker.is_percentage('100'))
        self.assertTrue(self.checker.is_percentage('50.123'))
        self.assertTrue(self.checker.is_percentage('1000'))
        self.assertTrue(self.checker.is_percentage(' 100% '))
        self.assertTrue(self.checker.is_percentage(' 50.123% '))
        self.assertTrue(self.checker.is_percentage(' 1000% '))

    def test_is_not_percentage(self):
        self.assertFalse(self.checker.is_percentage('100px'))
        self.assertFalse(self.checker.is_percentage('100cm'))
        self.assertFalse(self.checker.is_percentage(' mozman '))
        self.assertFalse(self.checker.is_percentage( (1, 2) ))
        self.assertFalse(self.checker.is_percentage( dict(a=1, b=2) ))

    def test_is_time(self):
        self.assertTrue(self.checker.is_time(100))
        self.assertTrue(self.checker.is_time(50.123))
        self.assertTrue(self.checker.is_time(1000))
        self.assertTrue(self.checker.is_time(' 100 '))
        self.assertTrue(self.checker.is_time(' 50.123 '))
        self.assertTrue(self.checker.is_time(' 1000 '))
        self.assertTrue(self.checker.is_time(' 100ms'))
        self.assertTrue(self.checker.is_time(' 50.123s'))
        self.assertTrue(self.checker.is_time(' 1000ms'))

    def test_is_not_time(self):
        self.assertFalse(self.checker.is_time('100px'))
        self.assertFalse(self.checker.is_time('100cm'))
        self.assertFalse(self.checker.is_time(' mozman '))
        self.assertFalse(self.checker.is_time( (1, 2) ))
        self.assertFalse(self.checker.is_time( dict(a=1, b=2) ))

    def test_is_angle(self):
        self.assertTrue(self.checker.is_angle(100))
        self.assertTrue(self.checker.is_angle(50.123))
        self.assertTrue(self.checker.is_angle(1000))
        self.assertTrue(self.checker.is_angle(' 100 '))
        self.assertTrue(self.checker.is_angle(' 50.123 '))
        self.assertTrue(self.checker.is_angle(' 1000 '))
        self.assertTrue(self.checker.is_angle(' 100rad'))
        self.assertTrue(self.checker.is_angle(' 50.123grad'))
        self.assertTrue(self.checker.is_angle(' 1000deg'))

    def test_is_not_angle(self):
        self.assertFalse(self.checker.is_angle('100px'))
        self.assertFalse(self.checker.is_angle('100cm'))
        self.assertFalse(self.checker.is_angle(' mozman '))
        self.assertFalse(self.checker.is_angle( (1, 2) ))
        self.assertFalse(self.checker.is_angle( dict(a=1, b=2) ))

    def test_is_frequency(self):
        self.assertTrue(self.checker.is_frequency(100))
        self.assertTrue(self.checker.is_frequency(50.123))
        self.assertTrue(self.checker.is_frequency(1000))
        self.assertTrue(self.checker.is_frequency(' 100 '))
        self.assertTrue(self.checker.is_frequency(' 50.123 '))
        self.assertTrue(self.checker.is_frequency(' 1000 '))
        self.assertTrue(self.checker.is_frequency(' 100Hz'))
        self.assertTrue(self.checker.is_frequency(' 50.123kHz'))
        self.assertTrue(self.checker.is_frequency(' 1000Hz'))

    def test_is_not_frequency(self):
        self.assertFalse(self.checker.is_frequency('100px'))
        self.assertFalse(self.checker.is_frequency('100cm'))
        self.assertFalse(self.checker.is_frequency(' mozman '))
        self.assertFalse(self.checker.is_frequency( (1, 2) ))
        self.assertFalse(self.checker.is_frequency( dict(a=1, b=2) ))

    def test_is_shape(self):
        self.assertTrue(self.checker.is_shape(' rect(1, 2, 3, 4)'))
        self.assertTrue(self.checker.is_shape(' rect(1cm, 2mm, -3px, 4%)'))

    def test_is_not_shape(self):
        self.assertFalse(self.checker.is_shape('rect(1, 2, 3)'))
        self.assertFalse(self.checker.is_shape('rect(1, 2, 3, 4, 5)'))
        self.assertFalse(self.checker.is_shape('rect(1, 2, 3, m)'))

    def test_is_number_optional_number(self):
        self.assertTrue(self.checker.is_number_optional_number(' 1, 2'))
        self.assertTrue(self.checker.is_number_optional_number('1 2. '))
        self.assertTrue(self.checker.is_number_optional_number('1  '))
        self.assertTrue(self.checker.is_number_optional_number(' 1.5  '))
        self.assertTrue(self.checker.is_number_optional_number( 1 ))
        self.assertTrue(self.checker.is_number_optional_number( [1, 2] ))

    def test_is_not_number_optional_number(self):
        self.assertFalse(self.checker.is_number_optional_number(' 1px, 2'))
        self.assertFalse(self.checker.is_number_optional_number(''))
        self.assertFalse(self.checker.is_number_optional_number(' , 2'))
        self.assertFalse(self.checker.is_number_optional_number(' 1 , 2 , 3'))
        self.assertFalse(self.checker.is_number_optional_number(' 1. 2. 3.'))
        self.assertFalse(self.checker.is_number_optional_number(' 1 2 3'))
        self.assertFalse(self.checker.is_number_optional_number([]))
        self.assertFalse(self.checker.is_number_optional_number([1,2,3]))
        self.assertFalse(self.checker.is_number_optional_number([1, '1px']))

    def test_is_IRI(self):
        # every none empty string is valid - no real url validation is done
        self.assertTrue(self.checker.is_IRI("http://localhost:8080?a=12"))
        self.assertTrue(self.checker.is_IRI("%&/(/&%$"))

    def test_is_not_IRI(self):
        self.assertFalse(self.checker.is_IRI(""))
        self.assertFalse(self.checker.is_IRI(1))
        self.assertFalse(self.checker.is_IRI(3.1415))
        self.assertFalse(self.checker.is_IRI( (1, 0)))
        self.assertFalse(self.checker.is_IRI(dict(a=1)))

    def test_is_FuncIRI(self):
        self.assertTrue(self.checker.is_FuncIRI("url(http://localhost:8080?a=12)"))
        self.assertTrue(self.checker.is_FuncIRI("url(ftp://something/234)"))

    def test_is_not_FuncIRI(self):
        self.assertFalse(self.checker.is_FuncIRI("url()"))
        self.assertFalse(self.checker.is_FuncIRI("url"))
        self.assertFalse(self.checker.is_FuncIRI("url("))
        self.assertFalse(self.checker.is_FuncIRI("url(http://localhost:8080"))
        self.assertFalse(self.checker.is_FuncIRI("http://localhost:8080"))

    def test_is_semicolon_list(self):
        # update 2017-12-27:
        # semicolon-list is a list of (any) VALUES separated by semicolons
        self.assertTrue(self.checker.is_semicolon_list("1;2;3;4;5"))
        self.assertTrue(self.checker.is_semicolon_list("1;2,3;4,5"))
        self.assertTrue(self.checker.is_semicolon_list("1.;2.,3.;4.,5."))
        self.assertTrue(self.checker.is_semicolon_list("1"))
        self.assertTrue(self.checker.is_semicolon_list("1 2;3;4;5"))
        self.assertTrue(self.checker.is_semicolon_list("1 A;3 4;5,Z"))
        self.assertTrue(self.checker.is_semicolon_list("#000000;#0000ff;#00ff00;#ff0000"))

    def test_is_not_semicolon_list(self):
        self.assertFalse(self.checker.is_semicolon_list(""))

    def test_is_icc_color(self):
        self.assertTrue(self.checker.is_icccolor("icc-color(red)"))
        self.assertTrue(self.checker.is_icccolor("icc-color(red mozman)"))
        self.assertTrue(self.checker.is_icccolor("icc-color(red,mozman)"))
        self.assertTrue(self.checker.is_icccolor("icc-color(red,mozman 123)"))

    def test_is_not_icc_color(self):
        self.assertFalse(self.checker.is_icccolor("icc-color()"))
        self.assertFalse(self.checker.is_icccolor("icc-color((a))"))

    def test_is_hex_color(self):
        self.assertTrue(self.checker.is_color("#101010"))
        self.assertTrue(self.checker.is_color("#111"))
        self.assertTrue(self.checker.is_color("#FFFFFF"))
        self.assertTrue(self.checker.is_color("#FFF"))
        self.assertTrue(self.checker.is_color("#aaaaaa"))
        self.assertTrue(self.checker.is_color("#aaa"))

    def test_is_not_hex_color(self):
        self.assertFalse(self.checker.is_color("#1"))
        self.assertFalse(self.checker.is_color("#22"))
        self.assertFalse(self.checker.is_color("#4444"))
        self.assertFalse(self.checker.is_color("#55555"))
        self.assertFalse(self.checker.is_color("#7777777"))
        self.assertFalse(self.checker.is_color("#gghhii"))

    def test_is_rgb_int_color(self):
        self.assertTrue(self.checker.is_color("rgb(1,2,3)"))
        self.assertTrue(self.checker.is_color("rgb( 1, 2, 3 )"))
        self.assertTrue(self.checker.is_color("rgb( 11, 21, 31 )"))
        self.assertTrue(self.checker.is_color("rgb( 0, 0, 0 )"))
        self.assertTrue(self.checker.is_color("rgb( 255 , 255 , 255 )"))
    def test_is_not_rgb_int_color(self):
        self.assertFalse(self.checker.is_color("rgb(,2,3)"))
        self.assertFalse(self.checker.is_color("rgb(1,,3)"))
        self.assertFalse(self.checker.is_color("rgb(1,2)"))
        self.assertFalse(self.checker.is_color("rgb(1)"))
        self.assertFalse(self.checker.is_color("rgb(a,2,3)"))
        self.assertFalse(self.checker.is_color("rgb()"))

    def test_is_rgb_percentage_color(self):
        self.assertTrue(self.checker.is_color("rgb(1%,2%,3%)"))
        self.assertTrue(self.checker.is_color("rgb( 1%, 2%, 3% )"))
        self.assertTrue(self.checker.is_color("rgb( 11%, 21%, 31% )"))
        self.assertTrue(self.checker.is_color("rgb( 0%, 0%, 0% )"))
        # this is not really valid
        self.assertTrue(self.checker.is_color("rgb( 255% , 255% , 255% )"))

    def test_is_not_rgb_percentage_color(self):
        self.assertFalse(self.checker.is_color("rgb()"))
        self.assertFalse(self.checker.is_color("rgb(1,2%,3%)"))
        self.assertFalse(self.checker.is_color("rgb(,2%,3%)"))
        self.assertFalse(self.checker.is_color("rgb(,,)"))
        self.assertFalse(self.checker.is_color("rgb(a%,b%,c%)"))
        # decimals allowed
        self.assertTrue(self.checker.is_color("rgb(1.0%, 2.0%, 3.0%)"))

    def test_is_color_name(self):
        self.assertTrue(self.checker.is_color("blue"))

    def test_is_not_color_name(self):
        self.assertFalse(self.checker.is_color("blau"))

    def test_is_paint_with_funcIRI(self):
        self.assertTrue(self.checker.is_paint("rgb(10, 20, 30)"))

    def test_is_paint_with_funcIRI_2(self):
        self.assertTrue(self.checker.is_paint("rgb(10, 20, 30) none"))

    def test_is_paint_with_funcIRI_3(self):
        self.assertTrue(self.checker.is_paint("url(localhost) rgb(10, 20, 30)"))

    def test_is_paint(self):
        self.assertTrue(self.checker.is_paint("inherit"))
        self.assertTrue(self.checker.is_paint("none"))
        self.assertTrue(self.checker.is_paint("currentColor"))
        self.assertTrue(self.checker.is_paint("rgb(10,20,30)"))
        self.assertTrue(self.checker.is_paint("rgb(10%,20%,30%)"))
        self.assertTrue(self.checker.is_paint("url(localhost)"))
        self.assertTrue(self.checker.is_paint("red"))

    def test_is_not_paint(self):
        self.assertFalse(self.checker.is_paint("(123)"))
        self.assertFalse(self.checker.is_paint("123"))
        self.assertFalse(self.checker.is_paint("schwarz"))

    def test_is_XML_name(self):
        self.assertTrue(self.checker.is_XML_Name("Name:xml123"))
        self.assertTrue(self.checker.is_XML_Name("Name-xml123"))
        self.assertTrue(self.checker.is_XML_Name("Name.xml123"))

    def test_is_not_XML_name(self):
        self.assertFalse(self.checker.is_XML_Name("Name xml123"))
        self.assertFalse(self.checker.is_XML_Name("0Name:xml123"))
        self.assertFalse(self.checker.is_XML_Name(".Name:xml123"))

    def test_is_transform_list(self):
        self.assertTrue(self.checker.is_transform_list("translate(10,10)"))
        self.assertTrue(self.checker.is_transform_list("scale(2 2)"))
        self.assertTrue(self.checker.is_transform_list("rotate( 30 )"))
        self.assertTrue(self.checker.is_transform_list("skewX(15)"))
        self.assertTrue(self.checker.is_transform_list("skewY(-15)"))
        self.assertTrue(self.checker.is_transform_list("matrix(.1 .2 .3 .4 .5 .6)"))

        self.assertTrue(self.checker.is_transform_list("translate(10,10),  rotate( 30 )"))
        self.assertTrue(self.checker.is_transform_list("translate(10,10) , rotate( 30 )"))
        self.assertTrue(self.checker.is_transform_list("translate(10,10) , rotate( 30 )"))
        self.assertTrue(self.checker.is_transform_list("translate(10,10)   rotate( 30 )"))

    def test_is_not_transform_list(self):
        self.assertFalse(self.checker.is_transform_list("mozman(10,10)"))
        self.assertFalse(self.checker.is_transform_list("translate(10,10"))
        self.assertFalse(self.checker.is_transform_list("translate 10, 10"))
        self.assertFalse(self.checker.is_transform_list("translate(10, 10))"))
        self.assertFalse(self.checker.is_transform_list("translate((10, 10))"))

    def test_is_not_transform_list_invalid_separator(self):
        self.assertFalse(self.checker.is_transform_list("translate(10,10) ,, rotate( 30 )"))
        self.assertFalse(self.checker.is_transform_list("translate(10,10) x rotate( 30 )"))

    def test_is_four_numbers(self):
        self.assertTrue(self.checker.is_four_numbers(' 1, 2, 3, 4 '))
        self.assertTrue(self.checker.is_four_numbers(' 1  2 3  4 '))
        self.assertTrue(self.checker.is_four_numbers((1,2,3,4)))
    def test_is_not_four_numbers(self):
        self.assertFalse(self.checker.is_four_numbers(' 1, 2, 3, '))
        self.assertFalse(self.checker.is_four_numbers(' 1, 2 '))
        self.assertFalse(self.checker.is_four_numbers(' 1 '))
        self.assertFalse(self.checker.is_four_numbers((1,2,3)))

    def test_is_shape(self):
        self.assertTrue(self.checker.is_shape("rect(1,2,3,4)"))
        self.assertTrue(self.checker.is_shape("rect(1px,2px,-3px,-4px)"))
        self.assertTrue(self.checker.is_shape("rect( 1px , 2px , -3px , -4px )"))
        self.assertTrue(self.checker.is_shape("rect(auto,auto,auto,auto)"))
        self.assertTrue(self.checker.is_shape("rect( auto , auto , auto , auto )"))

if __name__=='__main__' :
    unittest.main()
