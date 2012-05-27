#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 08.09.2010
#
#    Copyright (C) 2010  Manfred Moitzi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from distutils.core import setup

from svgwrite import VERSION, AUTHOR_NAME, AUTHOR_EMAIL

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname

setup(name='svgwrite',
    version=VERSION,
    description='A Python library to create SVG drawings.',
    author=AUTHOR_NAME,
    url='http://bitbucket.org/mozman/svgwrite',
    download_url='http://bitbucket.org/mozman/svgwrite/downloads',
    author_email=AUTHOR_EMAIL,
    packages=['svgwrite', 'svgwrite/data'],
    provides=['svgwrite'],
    long_description=read('README.TXT')+read('NEWS.TXT'),
    platforms="OS Independent",
    license="GPLv3",
    classifiers=[
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Intended Audience :: Developers",
	"Topic :: Multimedia :: Graphics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
     )
