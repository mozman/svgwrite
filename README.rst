svgwrite
========

This package is inactive! No new features will be added, there will
be no change of behavior, just bugfixes will be merged.

Abstract
--------

A Python library to create SVG drawings.

a simple example::

    import svgwrite

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
    dwg.save()

for more examples see: examples.py

As the name `svgwrite` implies, `svgwrite` creates new SVG drawings, it does not read existing drawings and also does
not import existing drawings, but you can always include other SVG drawings by the <image> entity.

`svgwrite` is a pure Python package and has no external dependencies.

Installation
------------

with pip::

    pip install svgwrite

or from source::

    python setup.py install


Documentation
-------------

http://readthedocs.org/docs/svgwrite/

svgwrite can be found on GitHub.com at:

http://github.com/mozman/svgwrite.git

Contact
-------

svgwrite@mozman.at
