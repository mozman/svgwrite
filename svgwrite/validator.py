#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg validator classes
# Created: 11.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
.. autoclass:: svgwrite.validator.FullProfileValidator

.. autoclass:: svgwrite.validator.TinyProfileValidator

"""

from svgwrite import pattern
from svgwrite import full11data

class FullProfileValidator(object):
    content_model = full11data.get_content_model()
    valid_attributes = full11data.get_valid_attributes()
    attribute_checker = full11data.attribute_checker

    def __init__(self, debug=True):
        self.debug = debug

    def check_attribute_names(self, elementname, attribs):
        """Checks if all attribute-names (keys of attribs) for element 'elementname'
        are valid.

        Raises ValueError if not valid.
        """
        valid_attribs = self.valid_attributes[elementname]
        for key in attribs.iterkeys():
            if key not in valid_attribs:
                raise ValueError("Invalid attribute '%s' for element '%s'." % (key, elementname))
        return attribs # pass-through function

    def check_attribute_value(self, attributename, value):
        """Checks if value is valid for attribute 'attribute-name'.

        Raises ValueError if not valid.
        """
        if not isinstance(value, basestring):
            value = unicode(value)
        if not self.attribute_checker[attributename](value):
            raise ValueError("Value '%s' is not valid for attribute '%s'." % (value, attributename))
        return value # pass-through function

    def check_valid_content(self, element, subelement):
        """ Check if element can contain subelement.

        Raises ValueError for invalid subelement.
        """
        valid_subelements = self.content_model[element]
        if '*' not in valid_subelements:
            if subelement not in valid_subelements:
                raise ValueError("Invalid content '%s' for element '%s'." % (subelement, element))
        return subelement

    def get_coordinate(self, value):
        """ Split value in (number, unit) if value has an unit or (number, None).

        Raises ValueError if not valid.
        """
        if value is None:
            raise TypeError("Invalid type 'None'.")
        if isinstance(value, (int, float)):
            return (value, None)
        else:
            result = pattern.coordinate.match(value.strip())
            if result:
                number, tmp, unit = result.groups()
                number = float(number)
            else:
                raise ValueError("'%s' has not a valid svg coordinate." % value)
            return (number, unit)

    def get_angle(self, value):
        """ Split value in (number, unit) if value has an unit or (number, None).

        Raises ValueError if not valid.
        """
        if value is None:
            raise TypeError("invalid type 'None'.")
        if isinstance(value, (int, float)):
            return (value, None)
        else:
            result = pattern.angle.match(value.strip())
            if result:
                number, tmp, unit = result.groups()
                number = float(number)
            else:
                raise ValueError("'%s' has not a valid svg angle." % value)
            return (number, unit)

    def check_coordinate(self, value):
        """ Check if value is a valid coordinate, raises ValueError if not valid.
        """
        number, unit = self.get_coordinate(value)
        return value
    check_length = check_coordinate

    def check_angle(self, value):
        """ Check if value is a valid angle, raises ValueError if not valid.
        """
        number, unit = self.get_angle(value)
        return value

    def check_number(self, value):
        number = float(value) # ok if we get a float number
        return value

class TinyProfileValidator(FullProfileValidator):
    def check_tiny(self, number):
        """ Check if number is a valid 'tiny' number, raises ValueError
        if number is not valid.

        Raises ValueError if not valid.
        """
        if not (-32767.9999 <= number <= 32767.9999):
            raise ValueError("'%.4f' out of range for baseProfile 'tiny'" % number)
        return number # pass-through function

    def check_number(self, value):
        number = float(value)
        self.check_tiny(number)
        return value

    def get_angle(self, value):
        number, unit = (super(TinyProfileValidator, self).get_angle(value))
        number = self.check_tiny(round(number, 4)) # round to four places for tiny profile
        return (number, unit)

    def get_coordinate(self, value):
        number, unit = (super(TinyProfileValidator, self).get_coordinate(value))
        number = self.check_tiny(round(number, 4)) # round to four places for tiny profile
        return (number, unit)
