#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svgwrite package parameter
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
.. data:: debug_mode

   *True* : debug mode is **ON**, all SVG attributes are checked if valid
   in the element context. Also the included SVG subelements will be checked
   if they are valid for the parent SVG element.

   *False*: no validation checks will be done, but program execution is faster.

.. data:: profile

   A `string` containing the name of the SVG profile, valid profiles are:
   ``full``, ``basic`` and ``tiny``.

.. autofunction:: init([baseProfile="full", debug=False])

"""
debug_mode = False
profile = "full"

def init(baseProfile="full", debug=False):
    """ Initialize or reassign values to the global variables.

    :param string baseProfile: SVG Profile: ``full``, ``basic`` or ``tiny``
    :param bool debug: set :data:`debug_mode`

    """
    global debug_mode
    debug_mode = debug
    baseProfile = baseProfile.lower()
    if baseProfile in ('tiny', 'basic', 'full'):
        global profile
        profile = baseProfile
    else:
        raise ValueError("'%s' is not a valid profile." % baseProfile)