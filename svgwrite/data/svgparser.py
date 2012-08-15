#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svgparser using pyparser
# Created: 16.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License
# depends on: pyparsing.py by Paul T. McGuire - http://pyparsing.wikispaces.com/

import sys
PYTHON3 = sys.version_info[0] > 2
if PYTHON3:
    from svgwrite.data.pyparsing_py3 import *
else:
    from svgwrite.data.pyparsing_py2 import *


event_names = [
    "focusin", "focusout", "activate", "click", "mousedown", "mouseup", "mouseover",
    "mousemove", "mouseout", "DOMSubtreeModified", "DOMNodeInserted", "DOMNoderemoved",
    "DOMNodeRemovedFromDocument", "DOMNodeInsertedetoDocument", "DOMAttrModified",
    "DOMCharacterDataModified", "SVGLoad", "SVGUnload", "SVGAbort", "SVGError",
    "SVGResize", "SVGScroll", "SVGZoom", "beginEvent", "endEvent", "repeatEvent",
    ]

sign = oneOf('+ -')
comma = Literal(',') * (0, 1) # zero or one ','
semicolon = Literal(';') * (0, 1) # zero or one ';'
integer_constant = Word(nums)
exponent = CaselessLiteral('E') + Optional(sign) + integer_constant
fractional_constant = Combine(Optional(integer_constant) + '.' + integer_constant) \
                    ^ Combine(integer_constant + '.')
scientific_constant = Combine(fractional_constant + Optional(exponent)) \
                    ^ Combine(integer_constant + exponent)
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
    nonnegative_number = integer_constant ^ scientific_constant
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

def _build_clock_val_parser():
    digit2 = Word(nums, exact=2)
    timecount = integer_constant
    fraction = integer_constant
    seconds = digit2
    minutes = digit2
    hours = integer_constant
    metric = oneOf("h min s ms")
    timecount_val = timecount + Optional("." + fraction) + Optional(metric)
    partial_clock_val = minutes + ":" + seconds + Optional("." + fraction)
    full_clock_val = hours + ":" + minutes + ":" + seconds + Optional("." + fraction)
    return full_clock_val | partial_clock_val | timecount_val

def _build_wall_clock_val_parser():
    # http://www.w3.org/TR/2005/REC-SMIL2-20050107/smil-timing.html#Timing-WallclockSyncValueSyntax
    digit2 = Word(nums, exact=2)
    fraction = integer_constant
    seconds = digit2
    minutes = digit2
    hours24 = digit2
    day = digit2
    month = digit2
    year = Word(nums, exact=4)
    tzd = Literal("Z") | (sign + hours24 + ":" + minutes)
    hhmmss = hours24 + ":" + minutes + Optional(":" + seconds + Optional("." + fraction))
    walltime = hhmmss + Optional(tzd)
    date = year + "-" + month + "-" + day
    datetime = date + "T" + walltime
    return (datetime | walltime | date)


def _build_animation_timing_parser():
    clock_val = _build_clock_val_parser()
    wallclock_value = _build_wall_clock_val_parser()
    event_ref = oneOf(event_names)
    id_value = "#" + Word(alphanums + "-_")
    opt_clock_val = Optional(sign + clock_val)

    wallclock_sync_value = Literal("wallclock(") + wallclock_value + ")"
    accesskey_value = Literal("accessKey(") + Word(alphas, exact=1) + ")" + opt_clock_val
    repeat_value = Optional(id_value + "." ) + Literal("repeat(") + integer_constant +")" + opt_clock_val
    event_value = Optional(id_value + "." ) + event_ref + opt_clock_val
    syncbase_value = id_value + "." + oneOf("begin end") + opt_clock_val
    offset_value = sign + clock_val
    begin_value = offset_value | syncbase_value | event_value | repeat_value \
                | accesskey_value | wallclock_sync_value | Literal("indefinite")
    return begin_value + ZeroOrMore(semicolon + begin_value)

class _AbstractParser(object):
    @classmethod
    def is_valid(cls, value):
        try:
            cls._parser.parseString(value, parseAll=True)
            return True
        except ParseException:
            return False

    @classmethod
    def parse(cls, value):
        raise NotImplementedError('parsing not implemented')

class TransformListParser(_AbstractParser):
    _parser = _build_transferlist_parser()

class PathDataParser(_AbstractParser):
    _parser = _build_pathdata_parser()

class AnimationTimingParser(_AbstractParser):
    _parser = _build_animation_timing_parser()
