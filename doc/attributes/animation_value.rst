Animation Value Attributes
==========================

.. _calcMode:

calcMode
--------

calcMode = ``'discrete | linear | paced | spline'``

Specifies the interpolation mode for the animation. This can take any of the
following values. The default mode is ``'linear'``, however if the attribute
does not support linear interpolation (e.g. for strings), the **calcMode**
attribute is ignored and discrete interpolation is used.

============== ==============================================================
value          description
============== ==============================================================
``'discrete'`` This specifies that the animation function will jump from one
               value to the next without any interpolation.
``'linear'``   Simple linear interpolation between values is used to
               calculate the animation function. Except for
               **animateMotion**, this is the default **calcMode**.
``'paced'``    Defines interpolation to produce an even pace of change across
               the animation. This is only supported for values that define
               a linear numeric range, and for which some notion of
               "distance" between points can be calculated (e.g. position,
               width, height, etc.). If ``'paced'`` is specified, any
               **keyTimes** or **keySplines** will be ignored. For
               **animateMotion**, this is the default **calcMode**.
``'spline'``   Interpolates from one value in the **values** list to the
               next according to a time function defined by a cubic Bézier
               spline. The points of the spline are defined in the
               **keyTimes** attribute, and the control points for each
               interval are defined in the **keySplines** attribute.
============== ==============================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#CalcModeAttribute

.. _values:

values
------

values = `<list>`

A semicolon-separated list of one or more values. Vector-valued attributes
are supported using the vector syntax of the **attributeType** domain.
Per the SMIL specification, leading and trailing white space, and white
space before and after semicolon separators, is allowed and will be ignored.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#ValuesAttribute

.. _keyTimes:

keyTimes
--------

keyTimes = `<list>`

A semicolon-separated list of time values used to control the pacing of the
animation. Each time in the list corresponds to a value in the **values**
attribute list, and defines when the value is used in the animation function.
Each time value in the **keyTimes** list is specified as a floating point
value between 0 and 1 (inclusive), representing a proportional offset into
the simple duration of the animation element.

If a list of **keyTimes** is specified, there must be exactly as many values
in the **keyTimes** list as in the **values** list.

Each successive time value must be greater than or equal to the preceding
time value.

The **keyTimes** list semantics depends upon the interpolation mode:

* For linear and spline animation, the first time value in the list must be
  0, and the last time value in the list must be 1. The key time associated
  with each value defines when the value is set; values are interpolated
  between the key times.
* For discrete animation, the first time value in the list must be 0. The
  time associated with each value defines when the value is set; the
  animation function uses that value until the next time defined in **keyTimes**.

If the interpolation mode is ``'paced'``, the **keyTimes** attribute is ignored.

If there are any errors in the **keyTimes** specification (bad values, too
many or too few values), the document fragment is in error.

If the simple duration is indefinite, any **keyTimes** specification will be
ignored.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#KeyTimesAttribute

.. _keySplines:

keySplines
----------

keySplines = `<list>`

A set of Bézier control points associated with the **keyTimes** list,
defining a cubic Bézier function that controls interval pacing. The attribute
value is a semicolon-separated list of control point descriptions. Each
control point description is a set of four values: x1 y1 x2 y2, describing
the Bézier control points for one time segment. Note: SMIL allows these
values to be separated either by commas with optional whitespace, or by
whitespace alone. The ‘keyTimes’ values that define the associated segment
are the Bézier "anchor points", and the ‘keySplines’ values are the control
points. Thus, there must be one fewer sets of control points than there are
**keyTimes**.

The values must all be in the range 0 to 1.

This attribute is ignored unless the **calcMode** is set to ``'spline'``.

If there are any errors in the **keySplines** specification (bad values, too
many or too few values), the document fragment is in error.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#KeySplinesAttribute

.. _from:

from
----

from = `<value>`

Specifies the starting value of the animation.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#FromAttribute

.. _to:

to
----

to = `<value>`

Specifies the ending value of the animation.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#ToAttribute

.. _by:

by
----

by = `<value>`

Specifies a relative offset value for the animation.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#ByAttribute