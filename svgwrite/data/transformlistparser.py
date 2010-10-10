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
        self.rv.append(Token('comma'))

    def t_wsp(self, s):
        r" \s+ "

    def t_number(self, s):
        r"[-+]?\d*\.?\d+([eE][-+]?\d+)?"
        self.rv.append(Token('number', float(s)))

    def t_lp(self, s):
        r" \( "
        self.rv.append(Token('lp'))

    def t_rp(self, s):
        r" \) "
        self.rv.append(Token('rp'))

    def t_translate(self, s):
        r" translate "
        self.rv.append(Token(s))

    def t_rotate(self, s):
        r" rotate "
        self.rv.append(Token(s))

    def t_matrix(self,s):
        r" matrix "
        self.rv.append(Token(s))

    def t_scale(self, s):
        r" scale "
        self.rv.append(Token(s))

    def t_skewX(self, s):
        r" skewX "
        self.rv.append(Token(s))

    def t_skewY(self, s):
        r" skewY "
        self.rv.append(Token(s))

class TransformParser(GenericParser):
    """ Just validate Syntax, don't need an AST (Abstract Syntax Tree).
    """
    def __init__(self, start='transforms'):
        GenericParser.__init__(self, start)

    def p_transforms(self, args):
        """
        transforms ::= transform
        transforms ::= transform cwsp transforms

        transform ::= matrixfunc
        transform ::= translatefunc
        transform ::= scalefunc
        transform ::= rotatefunc
        transform ::= skewXfunc
        transform ::= skewYfunc

        matrixfunc ::= matrix lp number cwsp number cwsp number cwsp number cwsp number cwsp number rp
        translatefunc ::= translate lp number cwsp number  rp
        translatefunc ::= translate lp number rp
        scalefunc ::= scale lp number cwsp number rp
        scalefunc ::= scale lp number rp
        rotatefunc ::= rotate lp number cwsp number cwsp number rp
        rotatefunc ::= rotate lp number rp
        skewXfunc ::= skewX lp number rp
        skewYfunc ::= skewY lp number rp

        cwsp ::= comma
        cwsp ::=
        """
