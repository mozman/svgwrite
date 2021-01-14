#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg hyperlink examples
# Created: 05.05.2017
# Copyright (C) 2017, Manfred Moitzi
# License: MIT License
try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import svgwrite


def hyperlink(name):
    dwg = svgwrite.Drawing(name, (200, 200), debug=True)
    # use the hyperlink element
    link = dwg.add(dwg.a('http://www.w3.org'))
    link.add(dwg.ellipse(center=(100, 50), r=(50, 25), fill='red'))
    dwg.save(pretty=True)

if __name__ == '__main__':
    hyperlink("hyperlink.svg")
