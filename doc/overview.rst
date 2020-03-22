Overview
========

As the name `svgwrite` implies, `svgwrite` creates new SVG drawings, it does not read/import existing drawings, but you can always include other SVG drawings by the `<image>` entity.

`svgwrite` has a debugging feature, activated by :code:`svgwrite.Drawing(debug=True)`. This feature is meant to find
SVG errors produced by your code while developing. This validation algorithm is not optimized and therefore very slow for
big SVG files. That will not change in the future. And because it is slow DON'T use it in production code!

If `svgwrite` without debugging is still too slow, you have to use the `lxml` package without `svgwrite` as wrapper. That
is the ugly truth since `svgwrite` is just a wrapper around `xml.etree.ElementTree`. If you learn the ElementTree API and the
SVG elements and attributes, you do not need `svgwrite`.


SVG Elements
------------

.. IMPORTANT::

   Use the **factory-methods** of the class **Drawing** to create new objects.
   (This is necessary to support validation for different SVG versions.)
   All **factory-methods** have the original SVG Elementname (e.g. Drawing.a(...),
   Drawing.g(...), Drawing.symbol(...), Drawing.line(...))

a short example::

   dwg = svgwrite.Drawing()
   link = dwg.add(dwg.a("http://link.to/internet"))
   square = link.add(dwg.rect((0, 0), (1, 1), fill='blue'))


Structural Elements
~~~~~~~~~~~~~~~~~~~

:class:`~svgwrite.drawing.Drawing`, :class:`~svgwrite.container.SVG`,
:class:`~svgwrite.container.Group`, :class:`~svgwrite.container.Defs`,
:class:`~svgwrite.container.Symbol`, :class:`~svgwrite.container.Marker`,
:class:`~svgwrite.container.Use`, :class:`~svgwrite.container.Hyperlink`

Graphical Elements
~~~~~~~~~~~~~~~~~~

:class:`~svgwrite.shapes.Line`, :class:`~svgwrite.shapes.Rect`,
:class:`~svgwrite.shapes.Circle`, :class:`~svgwrite.shapes.Ellipse`,
:class:`~svgwrite.shapes.Polyline`, :class:`~svgwrite.shapes.Polygon`,
:class:`~svgwrite.path.Path`

Text Objects
~~~~~~~~~~~~

:class:`~svgwrite.text.Text`, :class:`~svgwrite.text.TSpan`,
:class:`~svgwrite.text.TRef`, :class:`~svgwrite.text.TextPath`,
:class:`~svgwrite.text.TextArea`,

Paint Server
~~~~~~~~~~~~

:class:`~svgwrite.gradients.LinearGradient`, :class:`~svgwrite.gradients.RadialGradient`,
:class:`~svgwrite.pattern.Pattern`,

Masking
~~~~~~~

:class:`~svgwrite.masking.Mask`, :class:`~svgwrite.masking.ClipPath`

Animation
~~~~~~~~~

:class:`~svgwrite.animate.Set`, :class:`~svgwrite.animate.Animate`,
:class:`~svgwrite.animate.AnimateColor`, :class:`~svgwrite.animate.AnimateMotion`,
:class:`~svgwrite.animate.AnimateTransform`

Filter Effects
~~~~~~~~~~~~~~

:class:`~svgwrite.filters.Filter`


Mixins
------

:class:`~svgwrite.mixins.ViewBox`,
:class:`~svgwrite.mixins.Transform`,
:class:`~svgwrite.mixins.XLink`,
:class:`~svgwrite.mixins.Presentation`,
:class:`~svgwrite.mixins.MediaGroup`,
:class:`~svgwrite.mixins.Markers`,
:class:`~svgwrite.mixins.Clipping`,

Common Attributes
-----------------

.. toctree::
   :maxdepth: 1

   attributes/core
   attributes/conditional_processing
   attributes/document_event
   attributes/graphical_event
   attributes/presentation
   attributes/xlink

Basic Data Types
----------------

W3C: http://www.w3.org/TR/SVG11/types.html

You can always use python-types (`int`, `float`) for length, coordinate or angle
values, for length and coordinates the default unit is ``px``, for angles the
default unit is ``deg``, or you can use a string including a unit (e.g. ``100in``,
``1.5cm``, ``3.141529rad``).

Examples::

    Drawing(height=100, width=100) # drawing area of 100px x 100px
    Drawing(height='10cm', width='20cm') # drawing area of 10cm x 20cm


Numbers
-------

Numbers can be intergers or floats, also in scientific notation:

.. note::
   *tiny profile*: numbers must **not** have more than 4 decimal digits in the
   fractional part of their decimal expansion and must be in the range -32,767.9999
   to +32,767.9999, inclusive

Examples:

* 10, -23, 0
* 73.1234, -0.002, .154, -.897, +13.2, 0000.123
* 1.24E+2, 1.24e+2,1E0, -.0E-1

Angles
------

The <angle> unit identifier is optional. If not provided, the angle value is assumed to be in degrees.

==== ================ ========================
unit identifier       description
==== ================ ========================
deg  angle in degrees (full circle is 360deg)
grad angle in grads   (full circle is 400grad)
rad  angle in radians (full circle is 2*PI)
==== ================ ========================

Length
------

A *<length>* is a distance measurement, given as a number along with a unit, the
unit identifiers must be in lower case. The meaning of a percentage length value
depends on the attribute for which the percentage length value has been specified.

Two common cases are:

1. when a percentage length value represents a percentage of the viewport *width* or *height*, and
2. when a percentage length value represents a percentage of the bounding box *width* or *height* on a given object.

Coordinates
-----------

A *<coordinate>* is a length in the user coordinate system that is the given distance
from the origin of the user coordinate system along the relevant axis (the x-axis
for X coordinates, the y-axis for Y coordinates). Its syntax is the same as that
for *<length>*.

Units
-----

W3C: http://www.w3.org/TR/SVG11/coords.html#Units

When a coordinate or length value is a number without a unit identifier (e.g., "25"),
then the given coordinate or length is assumed to be in user units (i.e., a value
in the current user coordinate system).

Absolute units identifiers are only recommended for the `width` and the `height`
on and situations where the content contains no transformations and it is desirable
to specify values relative to the device pixel grid or to a particular real world
unit size.

.. note::
   *tiny profile*: no usage of units except for the *width* and *height* attributes
   of the Drawing object.

==== ======================
unit identifier description
==== ======================
px   one px unit is defined to be equal to one user unit
em   font-size (actual font height)
ex   x-height (height of letter 'x' of actual font)
pt   point   "1pt" equals "1.25px" (and therefore 1.25 user units)
pc   pica "1pc" equals "15px" (and therefore 15 user units)
mm   millimeter "1mm" would be "3.543307px" (3.543307 user units)
cm   centimeter "1cm" equals "35.43307px" (and therefore 35.43307 user units)
in   inch "1in" equals "90px" (and therefore 90 user units)
==== ======================
