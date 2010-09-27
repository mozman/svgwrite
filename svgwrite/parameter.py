#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svgwrite package parameter
# Created: 10.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
.. autoclass:: svgwrite.parameter._Parameter

.. attribute:: _Parameter.debug

   *True* : debug mode is **ON**, all SVG attributes are checked if valid
   in the element context. Also the included SVG subelements will be checked
   if they are valid for the parent SVG element.

   *False*: no validation checks will be done, but program execution is faster.

.. attribute:: _Parameter.profile

   A `string` containing the name of the SVG profile, valid profiles are:
   ``full``, ``basic`` and ``tiny``.

.. attribute:: _Parameter.validator

   *validator* provides methods to check validity of SVG attributes and values

.. automethod:: _Parameter.__init__([baseProfile="full", debug=False])

.. automethod:: _Parameter.set_debug(debug=True)

.. automethod:: _Parameter.set_profile(profile)

.. automethod:: _Parameter.get_auto_id()

"""
from svgwrite import validator

class _Parameter(object):
    debug = False
    profile = "full"
    validator = None
    autoid = 1
    def __init__(self):
        self.debug = False
        self._profile = "full"
        self._init_validator()

    def _init_validator(self):
        if self._profile == 'tiny':
            self.validator = validator.TinyProfileValidator(self.debug)
        else:
            self.validator = validator.FullProfileValidator(self.debug)

    def set_debug(self, debug=True):
        self.debug = debug
        self._init_validator()

    def get_version(self):
        if self._profile == 'tiny':
            return '1.2'
        else:
            return '1.1'

    def get_profile(self):
        return self._profile

    def set_profile(self, profile):
        """
        :param string profile: SVG Profile: ``full``, ``basic`` or ``tiny``

        """
        profile = profile.lower()
        if profile in ('tiny', 'basic', 'full'):
            self._profile = profile
            self._init_validator()
        else:
            raise ValueError("'%s' is not a valid profile." % profile)

    def get_auto_id(self):
        """ Get an automatic generated SVG id string: ``id#``. """
        retval = "id%d" %self.autoid
        self.autoid += 1
        return retval