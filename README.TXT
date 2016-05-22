
svgwrite
========

.. image:: https://readthedocs.org/projects/pip/badge/
   :target: https://svgwrite.readthedocs.org
   :alt: Read The Docs

.. image:: https://img.shields.io/pypi/l/svgwrite.svg
   :target: https://pypi.python.org/pypi/svgwrite/
   :alt: License

.. image:: https://img.shields.io/pypi/pyversions/svgwrite.svg
   :target: https://pypi.python.org/pypi/svgwrite/
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/wheel/svgwrite.svg
   :target: https://pypi.python.org/pypi/svgwrite/
   :alt: Wheel Status

.. image:: https://img.shields.io/pypi/status/svgwrite.svg
   :target: https://pypi.python.org/pypi/svgwrite/
   :alt: Status

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


Documentation
=============

  * http://packages.python.org/svgwrite
  * http://readthedocs.org/docs/svgwrite/

send feedback to mozman@gmx.at

svgwrite can be found on bitbucket.org at:

http://bitbucket.org/mozman/svgwrite
