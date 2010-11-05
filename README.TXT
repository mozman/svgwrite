
svgwrite
========

Abstract
========

A Python library to create SVG drawings.

a simple example::

    import svgwrite

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
    dwg.save()

for more examples see: examples.py

Installation
============

with pip::

    pip install svgwrite

or from source::

    python setup.py install

Tests
=====

run tests with **nosetests** or **py.test**

with Python 2.7::

    python -m unittest discover -s tests

on Windows & Python 2.7::

    runtests.bat

Documentation
=============

http://packages.python.org/svgwrite

send feedback to mozman@gmx.at

svgwrite can be found on bitbucket.org at:

http://bitbucket.org/mozman/svgwrite
