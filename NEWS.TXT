
NEWS
====

Version 1.1.7 - 2016-05-22

  * BUGFIX: color accepts percentage values as floats like "rgb(10.2%, 3.78%, 20%)"

Version 1.1.6 - 2014-05-30

  * BUGFIX: sign for offset-value wasn't optional

Version 1.1.5 - 2014-03-26

  * BUGFIX: xml serialization for CPython 3.4.0

Version 1.1.4 - 2014-03-16

  * simplified path parser
  * pyparsing as external dependency (by jenselme)

Version 1.1.3 - 2013-10-01

  * updated pyparsing for Python 3 to version 2.0.1 (prior version caused memory leaks)
  * BUGFIX: utf8 to unicode encoding error for Python 2.7
  * Tests for Python 3 require CPython3.3 or newer, using the 'u' prefix.

Version 1.1.2 - 2013-01-08

  * prevent setup.py from compiling all modules - error with 'pyparsing_py2.py' and Python3
  * BUGFIX: all tests run with CPython3.3

Version 1.1.1 - 2012-08-15

  * License changed to MIT License
  * tested with CPython2.7, CPython3.2, CPython3.3 and pypy-1.9 on Win7 Pro 32-bit
  * BUGFIX: dwg.animateTranform() -> dwg.animateTransform()
  * BUGFIX: in examples, replaced width and height params by size parameter
  * added examples
  * edit docs

Version 1.0.1 - 2012-06-08

  * added inline stylesheets
  * added examples created by Lawrence Tattrie

Version 1.0.0 - 2012-05-27

  * stable
  * tested with CPython 2.7, CPython 3.2, pypy-1.8
  * added script tag - thx to jmahmood
  * docs also available at: http://readthedocs.org/docs/svgwrite

Version 0.2.4 - 2011-12-30

  * beta version
  * Python 2.7: all strings will be converted by the unicode() function, for
    strings containing none-ascii-characters use prefix ``u""`` or better
    use ``from __future__ import unicode_literals``, because this is
    Python 3 compatible.
  * tested with CPython 2.7, CPython 3.2, and PyPy 1.7
  * BUGFIX: color parsing accepts white spaces in ``rgb()`` like ``rgb(0, 0, 0)``

Version 0.2.3 - 2010-11-13

  * beta version
  * Python 3.1 support
  * splitted examples.py into several files and moved them to
    the subdir 'examples'

Version 0.2.2 - 2010-11-05

  * alpha version
  * removed 'attribs' parameter from all constructors
  * new elements: Set, Animate, AnimateMotion, AnimateColor,
    AnimateTransform, all filter elements
  * added set_desc(title, desc), set_metadata(xmldata) to BaseElement class
  * moved content of interfaces.py to mixins.py, (ITransform -> Transform and so on)

Version 0.2.1 - 2010-10-31

  * alpha version
  * new elements: Marker, ClipPath, Mask
  * paint service: LinearGradient, RadialGradient, Pattern

Version 0.2.0 - 2010-10-24

  * alpha version
  * validator rewritten as validator2.py
  * debug and profile options separated for each drawing object
  * important change: create objects with factory functions of the
    *Drawing* class: drawing.<svg-elementname>(...)
  * added mixins for setting stroke and fill properties
  * new elements: Hyperlink, Image, TextArea,

Version 0.1.0 - 2010-09-26

  * alpha version
  * new elements:

    * basic shapes: Line, Rect, Circle, Ellipse, Polyline, Polygon, Path
    * text elements: Text, TSpan, TRef, TextPath
    * container elements: Group, Symbol, SVG, Use, Defs

  * for examples see: examples.py
