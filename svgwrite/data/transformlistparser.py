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

    def t_wsp(self, s):
        r" \s+ "

    def t_number(self, s):
        # FIXIT: this match .1, 1.0 but not 1. !!!
        r"[-+]?\d*\.?\d+([eE][-+]?\d+)?"
        self.rv.append(Token('number', float(s)))

    def t_bracket(self, s):
        r" \(|\) "
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
        transforms ::= transform cw transforms

        transform ::= matrixfunc
        transform ::= translatefunc
        transform ::= scalefunc
        transform ::= rotatefunc
        transform ::= skewXfunc
        transform ::= skewYfunc

        matrixfunc ::= matrix ( number cw number cw number cw number cw number cw number )
        translatefunc ::= translate ( number cw number  )
        translatefunc ::= translate ( number )
        scalefunc ::= scale ( number cw number )
        scalefunc ::= scale ( number )
        rotatefunc ::= rotate ( number cw number cw number )
        rotatefunc ::= rotate ( number )
        skewXfunc ::= skewX ( number )
        skewYfunc ::= skewY ( number )

        cw ::= ,
        cw ::=
        """
