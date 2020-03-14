#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svgparser using pyparser
# Created: 16.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License
# depends on: pyparsing.py by Paul T. McGuire - http://pyparsing.wikispaces.com/

__all__ = ["is_valid_transferlist", "is_valid_pathdata", "is_valid_animation_timing"]

import sys
import re

from pyparsing import *
from functools import partial

event_names = [
    "focusin", "focusout", "activate", "click", "mousedown", "mouseup", "mouseover",
    "mousemove", "mouseout", "DOMSubtreeModified", "DOMNodeInserted", "DOMNodeRemoved",
    "DOMNodeRemovedFromDocument", "DOMNodeInsertedtoDocument", "DOMAttrModified",
    "DOMCharacterDataModified", "SVGLoad", "SVGUnload", "SVGAbort", "SVGError",
    "SVGResize", "SVGScroll", "SVGZoom", "beginEvent", "endEvent", "repeatEvent",
    ]

sign = oneOf('+ -')
comma = Literal(',') * (0, 1)  # zero or one ','
semicolon = Literal(';') * (0, 1)  # zero or one ';'
integer_constant = Word(nums)
exponent = CaselessLiteral('E') + Optional(sign) + integer_constant
fractional_constant = Combine(Optional(integer_constant) + '.' + integer_constant) \
    ^ Combine(integer_constant + '.')
scientific_constant = Combine(fractional_constant + Optional(exponent)) \
    ^ Combine(integer_constant + exponent)
number = Combine(Optional(sign) + integer_constant) \
    ^ Combine(Optional(sign) + scientific_constant)

def has_valid_syntax(term, parser):
    try:
        parser.parseString(term, parseAll=True)
        return True
    except ParseException:
        return False


def build_transferlist_parser():
    matrix = Literal("matrix") + '(' + number + (Suppress(comma) + number) * 5 + ')'
    translate = Literal("translate") + '(' + number + Optional(comma + number) + ')'
    scale = Literal("scale") + '(' + number + Optional(comma + number) + ')'
    rotate = Literal("rotate") + '(' + number + Optional(comma + number + comma + number) + ')'
    skewX = Literal("skewX") + '(' + number + ')'
    skewY = Literal("skewY") + '(' + number + ')'
    transform = matrix | translate | scale | rotate | skewX | skewY
    return transform + ZeroOrMore(comma + transform)


transferlist_parser = build_transferlist_parser()
is_valid_transferlist = partial(has_valid_syntax, parser=transferlist_parser)

def build_pathdata_parser():
    c = "\s*[, ]\s*"
    integer_constant = r"\d+"
    nonnegative_number = r"(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?"
    number = r"[+-]?" + nonnegative_number
    flag = r"[01]"
    comma_delimited_coordinates = fr"\s*{number}({c}{number})*\s*"
    two_comma_delimited_numbers = fr"\s*{number}({c}{number}\s*)" "{1}"
    four_comma_delimited_numbers = fr"\s*{number}\s*({c}{number}\s*)" "{3}"
    six_comma_delimited_numbers = fr"\s*{number}\s*({c}{number}\s*)" "{5}"
    comma_delimited_coordinate_pairs = fr"{two_comma_delimited_numbers}({c}{two_comma_delimited_numbers})*"

    moveto = fr"[mM]\s*{comma_delimited_coordinate_pairs}"
    lineto = fr"[lL]\s*{comma_delimited_coordinate_pairs}"
    horizontal_lineto = fr"[hH]\s*{comma_delimited_coordinates}"
    vertical_lineto = fr"[vV]\s*{comma_delimited_coordinates}"
    curveto = f"[cC]\s*({six_comma_delimited_numbers})({c}{six_comma_delimited_numbers})*"
    smooth_curveto = fr"[sS]{four_comma_delimited_numbers}({c}{four_comma_delimited_numbers})*"
    quadratic_bezier_curveto = fr"[qQ]{four_comma_delimited_numbers}({c}{four_comma_delimited_numbers})*"
    smooth_quadratic_bezier_curveto = fr"[tT]\s*{comma_delimited_coordinate_pairs}"

    elliptical_arc_argument = f"{c}".join((
        fr"{nonnegative_number}",
        fr"{nonnegative_number}",
        fr"{number}",
        fr"{flag}",
        fr"{flag}",
        fr"{number}",
        fr"{number}",))
    elliptical_arc_argument = "\s*" + elliptical_arc_argument + "\s*"
    print(elliptical_arc_argument)
    elliptical_arc = fr"[aA]({elliptical_arc_argument})({c}{elliptical_arc_argument})*"

    drawto_command = "|".join((f"(\s*{cmd}\s*)" for cmd in (
        moveto, lineto, horizontal_lineto, vertical_lineto, "[zZ]",
        curveto, smooth_curveto, quadratic_bezier_curveto,
        smooth_quadratic_bezier_curveto, elliptical_arc)))

    pathre = f"^{moveto}({drawto_command})*$"

    return re.compile(pathre)

pathdata_parser = build_pathdata_parser()
def is_valid_pathdata(term):
    return bool(pathdata_parser.match(term))

def build_clock_val_parser():
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


def build_wall_clock_val_parser():
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
    return datetime | walltime | date


def build_animation_timing_parser():
    clock_val = build_clock_val_parser()
    wallclock_value = build_wall_clock_val_parser()
    event_ref = oneOf(event_names)
    # TODO: check id-value definition: is a leading '#' really valid?
    id_value = Optional("#") + Word(alphanums + "-_")
    opt_clock_val = Optional(sign + clock_val)

    wallclock_sync_value = Literal("wallclock(") + wallclock_value + ")"
    accesskey_value = Literal("accessKey(") + Word(alphas, exact=1) + ")" + opt_clock_val
    repeat_value = Optional(id_value + ".") + Literal("repeat(") + integer_constant + ")" + opt_clock_val
    event_value = Optional(id_value + ".") + event_ref + opt_clock_val
    syncbase_value = id_value + "." + oneOf("begin end") + opt_clock_val
    offset_value = Optional(sign) + clock_val
    begin_value = offset_value | syncbase_value | event_value | repeat_value \
                | accesskey_value | wallclock_sync_value | Literal("indefinite")
    return begin_value + ZeroOrMore(semicolon + begin_value)

animation_timing_parser = build_animation_timing_parser()
is_valid_animation_timing = partial(has_valid_syntax, parser=animation_timing_parser)
