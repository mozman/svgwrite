#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svgparser using pyparser
# Created: 16.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
# depends on: pyparsing.py by Paul T. McGuire - http://pyparsing.wikispaces.com/

from pyparsing import *

sign = oneOf('+ -')
comma = Literal(',')*(0,1) # zeroOrOne ','
digits = Word(nums)
integer_constant = digits

exponent = CaselessLiteral('E') + Optional(sign) + digits
fractional_constant = Combine(Optional(digits) + '.' + digits) \
                    ^ Combine(digits + '.')
scientific_constant = Combine(fractional_constant + Optional(exponent)) \
                        ^ Combine(digits + exponent)
number = Combine(Optional(sign) + integer_constant) \
       ^ Combine(Optional(sign) + scientific_constant)

def _build_transferlist_parser():
    matrix = Literal("matrix") + '(' + number + (Suppress(comma) + number) * 5 + ')'
    translate = Literal("translate") + '(' + number + Optional(comma + number) + ')'
    scale = Literal("scale") + '(' + number + Optional(comma + number) + ')'
    rotate = Literal("rotate") + '(' + number + Optional(comma + number + comma + number) + ')'
    skewX = Literal("skewX") + '(' + number + ')'
    skewY = Literal("skewY") + '(' + number + ')'
    transform = matrix | translate | scale | rotate | skewX | skewY
    return transform + ZeroOrMore(comma + transform)

def _build_pathdata_parser():
    coordinate = number
    coordinate_pair = coordinate + comma + coordinate
    nonnegative_number = digits ^ scientific_constant
    flag = oneOf('0 1')

    closepath = oneOf('Z z')
    moveto = oneOf('M m') + coordinate_pair + ZeroOrMore(comma + coordinate_pair)
    lineto = oneOf('L l') + coordinate_pair + ZeroOrMore(comma + coordinate_pair)
    horizontal_lineto = oneOf('H h') + coordinate + ZeroOrMore(comma + coordinate)
    vertical_lineto = oneOf('V v') + coordinate + ZeroOrMore(comma + coordinate)

    curveto_argument_sequence = coordinate_pair \
                              + comma + coordinate_pair \
                              + comma + coordinate_pair
    curveto = oneOf('C c') + curveto_argument_sequence \
            + ZeroOrMore(comma + curveto_argument_sequence)

    smooth_curveto_argument_sequence = coordinate_pair + comma + coordinate_pair
    smooth_curveto = oneOf('S s') \
                   + smooth_curveto_argument_sequence \
                   + ZeroOrMore(comma + smooth_curveto_argument_sequence)

    quadratic_bezier_curveto_argument_sequence = coordinate_pair \
                                               + comma + coordinate_pair
    quadratic_bezier_curveto = oneOf('Q q') \
                             + quadratic_bezier_curveto_argument_sequence \
                             + ZeroOrMore(comma + quadratic_bezier_curveto_argument_sequence)

    smooth_quadratic_bezier_curveto = oneOf('T t') + coordinate_pair \
                                    + ZeroOrMore(comma + coordinate_pair)

    elliptical_arc_argument = nonnegative_number + comma + nonnegative_number \
                            + comma + number + comma + flag + comma + flag \
                            + comma + coordinate_pair
    elliptical_arc = oneOf('A a') + elliptical_arc_argument \
                   + ZeroOrMore(comma + elliptical_arc_argument)

    drawto_command = closepath \
                   | lineto \
                   | horizontal_lineto \
                   | vertical_lineto \
                   | curveto \
                   | smooth_curveto \
                   | quadratic_bezier_curveto \
                   | smooth_quadratic_bezier_curveto \
                   | elliptical_arc
    drawto_commands = drawto_command + ZeroOrMore(drawto_command)
    moveto_drawto_command_group = moveto + ZeroOrMore(drawto_commands)
    return moveto_drawto_command_group + ZeroOrMore(moveto_drawto_command_group)

class TransformListParser(object):
    _parser = _build_transferlist_parser()

    @staticmethod
    def is_valid(value):
        try:
            TransformListParser._parser.parseString(value, parseAll=True)
            return True
        except ParseException:
            return False

class PathDataParser(object):
    _parser = _build_pathdata_parser()

    @staticmethod
    def is_valid(value):
        try:
            PathDataParser._parser.parseString(value, parseAll=True)
            return True
        except ParseException:
            return False
