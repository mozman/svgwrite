#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: animate elements
# Created: 31.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement

class Animate(BaseElement):
    """ The **animate** element allows scalar attributes and properties to be
    assigned different values over time .
    """
    elementname = 'animate'

class Set(BaseElement):
    """ The **set** element provides a simple means of just setting the value
    of an attribute for a specified duration. It supports all attribute types,
    including those that cannot reasonably be interpolated, such as string
    and boolean values. The **set** element is non-additive. The additive and
    accumulate attributes are not allowed, and will be ignored if specified.
    """
    elementname = 'set'

class AnimateColor(BaseElement):
    """ The **animateColor** element specifies a color transformation over
    time.
    """
    elementname = 'animateColor'

class AnimateMotion(BaseElement):
    """ The **animateMotion** element causes a referenced element to move
    along a motion path.
    """
    pass

class AnimateTransform(BaseElement):
    """ The **animateTransform** element animates a transformation attribute
    on a target element, thereby allowing animations to control translation,
    scaling, rotation and/or skewing.
    """
    elementname = 'animateTransform'

