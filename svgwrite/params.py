#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svgwrite package parameter
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
.. attribute:: svgwrite.parameter

   The global parameter object.

.. attribute:: svgwrite.parameter.debug

   *read/write* property

   * *True* : debug mode is on, all SVG attributes are checked if valid
     in the element context. Also the included SVG subelements will be
     checked if they are valid for the parent SVG element.

   * *False*: no validation checks will be done, but program execution is
     faster.

.. attribute:: svgwrite.parameter.profile

   *read/write* property

   name of the SVG profile, valid profiles are: ``'full|basic|tiny'``

"""

from validator2 import get_validator

class Parameter(object):
    __slots__ = ['_debug', 'validator', '_profile']

    def __init__(self, debug=True, profile='full'):
        self._debug = debug
        self.set_profile(profile)

    def _init_validator(self):
        self.validator = get_validator(self.profile,  self.debug)

    def get_debug(self):
        return self._debug

    def set_debug(self, debug):
        self._debug = debug
        self._init_validator()
    debug = property(get_debug, set_debug)

    def get_version(self):
        if self._profile == 'tiny':
            return '1.2'
        else:
            return '1.1'

    def get_profile(self):
        return self._profile

    def set_profile(self, profile):
        """
        :param string profile: name of the SVG profile, valid profiles are:
        ``'full|basic|tiny'``

        """
        profile = profile.lower()
        if profile in ('tiny', 'basic', 'full'):
            self._profile = profile
            self._init_validator()
        else:
            raise ValueError("'%s' is not a valid profile." % profile)
    profile = property(get_profile, set_profile)
