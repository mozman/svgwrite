#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='svgwrite',
    version='0.0.0',
    description='A Python library to create SVG drawings.',
    author='mozman',
    url='http://bitbucket.org/mozman/svgwrite',
    download_url='http://bitbucket.org/mozman/svgwrite/downloads',
    author_email='mozman@gmx.at',
    packages=['svgwrite'],
    provides=['svgwrite'],
    long_description=read('README.TXT')+read('NEWS.TXT'),
    platforms="OS Independent",
    license="GPLv3",
    classifiers=[
    "Development Status :: 1 - Planning",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
	"Programming Language :: Python :: 2.7",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
     )
