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

class _Parameter(object):
    _debug = False
    _profile = "full"
    _autoid = 1
    validator = None

    def __init__(self):
        _Parameter._debug = False
        _Parameter._profile = "full"
        self._init_validator()

    def _init_validator(self):
        _Parameter.validator = get_validator(self.get_profile(),  self.get_debug())

    def get_debug(self):
        return _Parameter._debug

    def set_debug(self, debug):
        _Parameter._debug = debug
        self._init_validator()
    debug = property(get_debug, set_debug)

    def get_version(self):
        if _Parameter._profile == 'tiny':
            return '1.2'
        else:
            return '1.1'

    def get_profile(self):
        return _Parameter._profile

    def set_profile(self, profile):
        """
        :param string profile: name of the SVG profile, valid profiles are:
        ``'full|basic|tiny'``

        """
        profile = profile.lower()
        if profile in ('tiny', 'basic', 'full'):
            _Parameter._profile = profile
            self._init_validator()
        else:
            raise ValueError("'%s' is not a valid profile." % profile)
    profile = property(get_profile, set_profile)

    def get_auto_id(self):
        """ Get an automatic generated SVG id string: ``id###``. """
        retval = "id%d" % _Parameter._autoid
        _Parameter._autoid += 1
        return retval

    def _set_auto_id(self, value):
        """Just for testing. """
        _Parameter._autoid = value