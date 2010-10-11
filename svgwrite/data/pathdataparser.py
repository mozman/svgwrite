#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: path data parser
# Created: 11.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
# depend on: spark.py module - http://pages.cpsc.ucalgary.ca/~aycock/spark/

import unittest

from spark import GenericScanner, GenericParser
from spark import LexicalError, ParseError

class Token(object):
    def __init__(self, type, attr=None):
        self.type = type
        self.attr = attr

    def __cmp__(self, o):
        return cmp(self.type, o)

    def __repr__(self):
        if self.attr:
            return "%s (%s)" % (self.type, self.attr)
        else:
            return str(self.type)

path_commands = {
    'l': 'lineto-cmd',
    'm': 'moveto-cmd',
    'v': 'vertical-lineto-cmd',
    'h': 'horizontal-lineto-cmd',
    'z': 'closepath-cmd',
    'c': 'curveto-cmd',
    's': 'smooth-curveto-cmd',
    'q': 'quadratic-bezier-curveto-cmd',
    't': 'smooth-quadratic-bezier-curveto-cmd',
    'a': 'elliptical-arc-cmd',
}

class PathDataScanner(GenericScanner):
    def __init__(self):
        GenericScanner.__init__(self)

    def tokenize(self, value):
        self.rv=[]
        GenericScanner.tokenize(self, value)
        return self.rv

    def t_comma(self, s):
        r" , "
        self.rv.append(Token(s))

    def t_point(self, s):
        r" \. "
        self.rv.append(Token(s))

    def t_wsp(self, s):
        r" \s+ "
        self.rv.append(Token('wsp+'))

    def t_digit(self, s):
        r" \d "
        self.rv.append(Token(s))

    def t_sign(self, s):
        r" [\-\+] "
        self.rv.append(Token(s))

    def t_exponent(self, s):
        r" [eE] "
        self.rv.append(Token('e'))

    def t_command(self, s):
        r" [mMlLvVhHzZcCsSqQtTaA] "
        self.rv.append(Token(path_commands[s.lower()]))

class PathDataParser(GenericParser):
    # http://www.w3.org/TR/SVG11/paths.html#PathData
    """ Just validate Syntax, don't need an AST (Abstract Syntax Tree).
    """
    def __init__(self, start='svgpath'):
        GenericParser.__init__(self, start)

    def p_svgpath(self, args):
        """
        svgpath ::= moveto-drawto-command-groups

        moveto-drawto-command-groups ::= moveto-drawto-command-group
        moveto-drawto-command-groups ::= moveto-drawto-command-group wsp* moveto-drawto-command-groups

        moveto-drawto-command-group ::= moveto
        moveto-drawto-command-group ::= moveto wsp* drawto-commands

        drawto-commands ::= drawto-command
        drawto-commands ::= drawto-command wsp* drawto-commands

        drawto-command ::= closepath-cmd
        drawto-command ::= lineto
        drawto-command ::= horizontal-lineto
        drawto-command ::= vertical-lineto
        drawto-command ::= curveto
        drawto-command ::= smooth-curveto
        drawto-command ::= quadratic-bezier-curveto
        drawto-command ::= smooth-quadratic-bezier-curveto
        drawto-command ::= elliptical-arc

        moveto ::= moveto-cmd wsp* moveto-argument-sequence
        moveto-argument-sequence ::= coordinate-pair
        moveto-argument-sequence ::= coordinate-pair comma-wsp moveto-argument-sequence

        lineto ::= lineto-cmd wsp* lineto-argument-sequence
        lineto-argument-sequence ::= coordinate-pair
        lineto-argument-sequence ::= coordinate-pair comma-wsp lineto-argument-sequence

        horizontal-lineto ::= horizontal-lineto-cmd wsp* horizontal-lineto-argument-sequence
        horizontal-lineto-argument-sequence ::= coordinate
        horizontal-lineto-argument-sequence ::= coordinate comma-wsp horizontal-lineto-argument-sequence

        vertical-lineto ::= vertical-lineto-cmd wsp* horizontal-lineto-argument-sequence

        curveto ::= curveto-cmd wsp* curveto-argument-sequence
        curveto-argument-sequence ::= curveto-argument
        curveto-argument-sequence ::= curveto-argument comma-wsp curveto-argument-sequence
        curveto-argument ::= coordinate-pair comma-wsp coordinate-pair comma-wsp coordinate-pair

        smooth-curveto ::= smooth-curveto-cmd wsp* smooth-curveto-argument-sequence
        smooth-curveto-argument-sequence ::= smooth-curveto-argument
        smooth-curveto-argument-sequence ::= smooth-curveto-argument comma-wsp smooth-curveto-argument-sequence
        smooth-curveto-argument ::= coordinate-pair comma-wsp coordinate-pair

        quadratic-bezier-curveto ::= quadratic-bezier-curveto-cmd wsp* quadratic-bezier-curveto-argument-sequence
        quadratic-bezier-curveto-argument-sequence ::= quadratic-bezier-curveto-argument
        quadratic-bezier-curveto-argument-sequence ::= quadratic-bezier-curveto-argument comma-wsp quadratic-bezier-curveto-argument-sequence
        quadratic-bezier-curveto-argument ::= coordinate-pair comma-wsp coordinate-pair

        smooth-quadratic-bezier-curveto ::= smooth-quadratic-bezier-curveto-cmd wsp* smooth-quadratic-bezier-curveto-argument-sequence
        smooth-quadratic-bezier-curveto-argument-sequence ::= coordinate-pair
        smooth-quadratic-bezier-curveto-argument-sequence ::= coordinate-pair comma-wsp smooth-quadratic-bezier-curveto-argument-sequence

        elliptical-arc ::=  elliptical-arc-cmd wsp* elliptical-arc-argument-sequence
        elliptical-arc-argument-sequence ::= elliptical-arc-argument
        elliptical-arc-argument-sequence ::= elliptical-arc-argument comma-wsp elliptical-arc-argument-sequence
        elliptical-arc-argument ::= nonnegative-number comma-wsp nonnegative-number comma-wsp number comma-wsp flag comma-wsp flag comma-wsp coordinate-pair

        coordinate-pair ::= coordinate comma-wsp coordinate
        coordinate ::= number

        nonnegative-number ::= integer-constant
        nonnegative-number ::= floating-point-constant

        number ::= integer-constant
        number ::= sign integer-constant
        number ::= floating-point-constant
        number ::= sign floating-point-constant

        flag ::= 0
        flag ::= 1

        integer-constant ::= digit-sequence

        floating-point-constant ::=  fractional-constant
        floating-point-constant ::=  fractional-constant exponent
        floating-point-constant ::=  digit-sequence
        floating-point-constant ::=  digit-sequence exponent

        fractional-constant ::=  digit-sequence . digit-sequence
        fractional-constant ::=  . digit-sequence
        fractional-constant ::=  digit-sequence .

        exponent ::=  e sign digit-sequence
        exponent ::=  e digit-sequence

        digit-sequence ::= digit
        digit-sequence ::= digit digit-sequence

        digit ::= 0
        digit ::= 1
        digit ::= 2
        digit ::= 3
        digit ::= 4
        digit ::= 5
        digit ::= 6
        digit ::= 7
        digit ::= 8
        digit ::= 9

        sign ::= -
        sign ::= +

        comma-wsp ::= wsp+ , wsp*
        comma-wsp ::= , wsp*
        comma-wsp ::= wsp+

        wsp* ::= wsp+
        wsp* ::=
        """
