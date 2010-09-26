
svgwrite
========

Abstract
========

A Python library to create SVG drawings.

a simple example::

    import svgwrite as svg
    drawing = svg.Drawing('test.svg')
    drawing.add(svg.Line((0, 0), (10, 0), color=svg.rgb(10, 10, 16, '%')))
    drawing.add(svg.Text('Test', insert=(0, 0.2)))
    drawing.save()

for more examples see: examples.py

Installation
============

with pip::

    pip install svgwrite

or from source::

    python setup.py install

Documentation
=============

http://packages.python.org/svgwrite

send feedback to mozman@gmx.at

svgwrite can be found on bitbucket.org at:

http://bitbucket.org/mozman/svgwrite
