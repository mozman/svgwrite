#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite

def simple_text(name):
    dwg = svgwrite.Drawing(name, (200, 200), debug=True)
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text("This is a Test!", (10,20)))
    # 'x', 'y', 'dx', 'dy' and 'rotate' has to be a <list> or a <tuple>!!!
    # 'param'[0] .. first letter, 'param'[1] .. second letter, and so on
    # if there are more letters than values, the last list-value is used
    #
    # different 'y' coordinates does not work with Firefox 3.6
    paragraph.add(dwg.text("This is a Test", x=[10], y=[40, 45, 50, 55, 60]))

    # different formats can be used by the TSpan element
    # The atext.tspan(...) method is a shortcut for: atext.add(dwg.tspan(...))
    atext = dwg.text("A", insert=(10, 80))

    # text color is set by the 'fill' property and 'stroke sets the outline color.
    atext.add(dwg.tspan(' Word', font_size='1.5em', fill='red'))
    atext.add(dwg.tspan(' is a Word!', dy=['1em'], font_size='0.7em', fill='green'))
    paragraph.add(dwg.text("Das ist ein Test mit ÖÄÜäüö!", (10,120)))
    paragraph.add(atext)
    dwg.save()

if __name__ == '__main__':
    simple_text("simple_text.svg")
