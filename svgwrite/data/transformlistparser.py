#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: transform list parser
# Created: 10.10.2010
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

class TransformScanner(GenericScanner):
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

    def t_bracket(self, s):
        r" [\(\)] "
        self.rv.append(Token(s))

    def t_command(self, s):
        r" translate|rotate|matrix|rotate|scale|skewX|skewY "
        self.rv.append(Token(s))

class TransformParser(GenericParser):
    """ Just validate Syntax, don't need an AST (Abstract Syntax Tree).
    """
    def __init__(self, start='transforms'):
        GenericParser.__init__(self, start)

    def p_transforms(self, args):
        """
        transforms ::= transform
        transforms ::= transform comma-wsp transforms

        transform ::= matrix-func
        transform ::= translate-func
        transform ::= scale-func
        transform ::= rotate-func
        transform ::= skewX-func
        transform ::= skewY-func

        matrix-func ::= matrix wsp* ( wsp* number comma-wsp number comma-wsp number comma-wsp number comma-wsp number comma-wsp number wsp* )
        translate-func ::= translate wsp* ( wsp* number comma-wsp number wsp* )
        translate-func ::= translate wsp* ( wsp* number wsp* )
        scale-func ::= scale wsp* ( wsp* number comma-wsp number wsp* )
        scale-func ::= scale wsp* ( wsp* number wsp* )
        rotate-func ::= rotate wsp* ( wsp* number comma-wsp number comma-wsp number wsp* )
        rotate-func ::= rotate wsp* ( wsp* number wsp* )
        skewX-func ::= skewX wsp* ( wsp* number wsp* )
        skewY-func ::= skewY wsp* ( wsp* number wsp* )

        number ::= integer-constant
        number ::= sign integer-constant
        number ::= floating-point-constant
        number ::= sign floating-point-constant

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
