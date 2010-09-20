Overview
========

Global Parameters
-----------------

:mod:`svgwrite.parameter`

Structural Elements
-------------------

.. toctree::
   :titlesonly:

   classes/drawing
   classes/svg
   classes/group
   classes/defs
   classes/use

Graphical Elements
------------------
.. toctree::
   :maxdepth: 1

   classes/path
   classes/shapes

Interfaces
----------

.. toctree::
   :maxdepth: 1

   classes/interface

Common Attributes
-----------------

.. toctree::
   :titlesonly:

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