#!/usr/bin/env python3
# License: MIT License
# Copyright (C) 2010-2020  Manfred Moitzi
from pathlib import Path
from setuptools import setup

AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'me@mozman.at'

ROOT = Path(__file__).resolve().parent

def get_version():
    v = {}
    # do not import svgwrite, because required packages may not installed yet
    for line in (ROOT / "svgwrite" / "version.py").read_text().splitlines():
        if line.strip().startswith('__version__'):
            exec(line, v)
            return v['__version__']
    raise IOError('__version__ string not found')


setup(name='svgwrite',
      version=get_version(),
      description='A Python library to create SVG drawings.',
      author=AUTHOR_NAME,
      url='http://github.com/mozman/svgwrite.git',
      download_url='http://github.com/mozman/svgwrite/releases',
      author_email=AUTHOR_EMAIL,
      python_requires='>=3.6',
      packages=['svgwrite', 'svgwrite/data', 'svgwrite/extensions'],
      provides=['svgwrite'],
      long_description=((ROOT / 'README.rst').read_text() +
                        (ROOT / 'NEWS.rst').read_text()),
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Intended Audience :: Developers",
          "Topic :: Multimedia :: Graphics",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ]
)
