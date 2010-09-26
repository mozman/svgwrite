#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import os
from distutils.core import setup

from svgwrite.metadata import VERSION, AUTHOR_NAME, AUTHOR_EMAIL

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='svgwrite',
    version=VERSION,
    description='A Python library to create SVG drawings.',
    author=AUTHOR_NAME,
    url='http://bitbucket.org/mozman/svgwrite',
    download_url='http://bitbucket.org/mozman/svgwrite/downloads',
    author_email=AUTHOR_EMAIL,
    packages=['svgwrite'],
    provides=['svgwrite'],
    long_description=read('README.TXT')+read('NEWS.TXT'),
    platforms="OS Independent",
    license="GPLv3",
    classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
	"Programming Language :: Python :: 2.7",
    "Intended Audience :: Developers",
	"Topic :: Multimedia :: Graphics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
     )
