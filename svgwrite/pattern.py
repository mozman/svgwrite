#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: pattern module
# Created: 27.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import re

# coordinates with optional unit
coordinate = re.compile("(^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)(cm|em|ex|in|mm|pc|pt|px|%)?$")

# coordinates with optional unit
angle = re.compile("(^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)(deg|rad|grad)?$")

# numbers without units
number = re.compile("(^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)$")
