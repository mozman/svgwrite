#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: package definition file
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from parameter import init
from drawing import Drawing
from shapes import Line, Rect, Circle, Ellipse, Polygon, Polyline
from path import Path

def cm(value):
    return "%scm" % value

def mm(value):
    return "%smm" % value

def em(value):
    return "%sem" % value

def ex(value):
    return "%sex" % value

def px(value):
    return "%spx" % value

def inch(value):
    return "%sin" % value

def pc(value):
    return "%spc" % value

def pt(value):
    return "%spt" % value
