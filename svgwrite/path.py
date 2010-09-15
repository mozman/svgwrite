#coding:utf-8
# Author:  mozman
# Purpose: svg path element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement
from utils import check_coordinate

class Path(BaseElement):
    """ The svg <path /> object.

    Methods:
    --------
    hline(*values) -- add horizontal line
    vline(*values) -- add vertical line
    moveto(point) -- move cursor to point and begin a new subpath
    lineto(points) -- draw line to points[0], points[1], ...
    qbezier(b1, dest) -- draw quadratic bezier curve to dest with breakpoint b1
    continue_qbezier(dest) -- continue q. bezier curve to point dest
    cbezier(b1, b2, dest) -- draw cubic bezier curve to dest with breakpoints b1, b2
    continue_cbezier(b2, dest) -- continue c. bezier curve to point dest with breakpoint b2
    close() -- close path
    """
    def __init__(self, attribs=None, **kwargs):
        super(Path, self).__init__(attribs, **kwargs)
        self.commands = []

    def hline(self, *values):
        self.commands.append(u'h')
        self.commands.extend(values)

    def vline(self, *values):
        self.commands.append(u'v')
        self.commands.extend(values)

    def moveto(self, point=(0, 0)):
        self.commands.append(u'm')
        self.commands.append(point)

    def lineto(self, points=[]):
        self.commands.append(u'l')
        self.commands.extend(points)

    def qbezier(self, b1=(0,0), dest=(0,0)):
        self.commands.append('q')
        self.commands.append(b1)
        self.commands.append(dest)

    def continue_qbezier(self, dest=(0,0)):
        self.commands.append(u't')
        self.commands.append(dest)

    def cbezier(self, b1=(0,0), b2=(0,0), dest=(0,0)):
        self.commands.append(u'c')
        self.commands.append(b1)
        self.commands.append(b2)
        self.commands.append(dest)

    def continue_cbezier(self, b2=(0,0), dest=(0,0)):
        self.commands.append(u's')
        self.commands.append(b2)
        self.commands.append(dest)

    def close(self):
        self.commands.append(u'z')

    def get_xml(self):
        self.attribs['d'] = self.commands_to_unicode()
        return super(Path, self).get_xml()

    def commands_to_unicode(self):
        strings = []
        for command in self.commands:
            s = unicode(command)
            if isinstance(command, tuple):
                for coord in command: # check for valid coords
                    check_coordinate(coord)
                s = s[1:-1] # remove brackets
            strings.append(s)
        return u' '.join(strings)