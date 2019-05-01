#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 08.09.2010
# License: MIT License
# Copyright (C) 2010-2018  Manfred Moitzi
import os
from setuptools import setup

AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'me@mozman.at'


def get_version():
    v = {}
    # do not import svgwrite, because required packages may not installed yet
    for line in open('./svgwrite/version.py').readlines():
        if line.strip().startswith('__version__'):
            exec(line, v)
            return v['__version__']
    raise IOError('__version__ string not found')


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname


setup(name='svgwrite',
      version=get_version(),
      description='A Python library to create SVG drawings.',
      author=AUTHOR_NAME,
      url='http://github.com/mozman/svgwrite.git',
      download_url='http://github.com/mozman/svgwrite/releases',
      author_email=AUTHOR_EMAIL,
      packages=['svgwrite', 'svgwrite/data', 'svgwrite/extensions'],
      provides=['svgwrite'],
      install_requires=['pyparsing>=2.0.1'],
      long_description=read('README.rst') + read('NEWS.rst'),
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Intended Audience :: Developers",
          "Topic :: Multimedia :: Graphics",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ]
)
