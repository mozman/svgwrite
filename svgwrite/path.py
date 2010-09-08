#coding:utf-8
# Author:  mozman
# Purpose: svg path element
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

from base import BaseElement

class Path(BaseElement):
    def __init__(self, attribs=None, **kwargs):
        super(Path, self).__init__(attribs, kwargs)
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
        self.commands.extend(point)

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

    def get_etree(self):
        self.attribs['d'] = self.commands_to_unicode()
        return super(Path, self).get_etree()

    def commands_to_unicode(self):
        strings = []
        for command in self.commands:
            s = unicode(command)
            if isinstance(command, tuple):
                s = s[1:-1] # remove brackets
            strings.append(s)
        return u' '.join(strings)