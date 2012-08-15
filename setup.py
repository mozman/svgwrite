#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 08.09.2010
# License: MIT License
# Copyright (C) 2010-2012  Manfred Moitzi


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
    license="MIT License",
    classifiers=[
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Intended Audience :: Developers",
	"Topic :: Multimedia :: Graphics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
     )
