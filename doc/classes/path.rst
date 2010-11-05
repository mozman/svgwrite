Path
====

.. autoclass:: svgwrite.path.Path

.. seealso:: http://www.w3.org/TR/SVG11/paths.html#PathElement

.. automethod:: svgwrite.path.Path.__init__

Attributes
----------

.. attribute:: commands

   `list` -- the command and coordinate stack

Methods
-------

.. automethod:: svgwrite.path.Path.push

.. automethod:: svgwrite.path.Path.push_arc

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Markers`

.. _pathCommands:

Path Commands
-------------

.. seealso:: http://www.w3.org/TR/SVG11/paths.html#PathData

Uppercase commands indicates absolute coordinates, lowercase commands
indicates relative coordinates

* **horizontal-line 'h', 'H' x+**

  Draws a horizontal line from the current point (cpx, cpy) to (x, cpy).

* **vertical-line 'v', 'V' y+**

  Draws a vertical line from the current point (cpx, cpy) to (cpx, y).

* **line 'l', 'L' (x y)+**

  Draw a line from the current point to the given (x,y) coordinate.

* **moveto 'm', 'M' (x y)+**

  Start a new sub-path at the given (x,y) coordinate.
  If a moveto is followed by multiple pairs of coordinates, the subsequent
  pairs are treated as implicit lineto commands. Hence, implicit lineto
  commands will be relative if the moveto is relative, and absolute if the
  moveto is absolute. If a relative moveto (m) appears as the first element
  of the path, then it is treated as a pair of absolute coordinates.
  In this case, subsequent pairs of coordinates are treated as relative even
  though the initial moveto is interpreted as an absolute moveto.

* **cubic-bezier-curve 'c', 'C' (x1 y1 x2 y2 x y)+**

  Draws a cubic Bézier curve from the current point
  to (x,y) using (x1,y1) as the control point at the beginning of the curve
  and (x2,y2) as the control point at the end of the curve.

* **smooth-cubic-bezier-curve 's', 'S' (x2 y2 x y)+**

  Draws a cubic Bézier curve from the current point to
  (x,y). The first control point is assumed to be the reflection of the second
  control point on the previous command relative to the current point. (If
  there is no previous command or if the previous command was not an C, c,
  S or s, assume the first control point is coincident with the current point.)
  (x2,y2) is the second control point (i.e., the control point at the end of
  the curve).

* **quadratic-bezier-curve 'q', 'Q' (x1 y1 x y)+**

  Draws a quadratic Bézier curve from the current point
  to (x,y) using (x1,y1) as the control point.

* **smooth-quadratic-bezier-curve 't', 'T' (x y)+**

  Draws a quadratic Bézier curve from the current point to (x,y).
  The control point is assumed to be the reflection of the control point on
  the previous command relative to the current point. (If there is no previous
  command or if the previous command was not a Q, q, T or t, assume the control
  point is coincident with the current point.)

* **elliptical-arc 'a', 'A' (rx ry x-axis-rotation large-arc-flag sweep-flag x y)+**

  Draws an elliptical arc from the current point to (x, y). The size and orientation
  of the ellipse are defined by two radii (rx, ry) and an x-axis-rotation,
  which indicates how the ellipse as a whole is rotated relative to the
  current coordinate system. The center (cx, cy) of the ellipse is
  calculated automatically to satisfy the constraints imposed by the other
  parameters. large-arc-flag and sweep-flag contribute to the automatic
  calculations and help determine how the arc is drawn.

* **'z', 'Z'**

  close current subpath

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed
  even if external resources are unavailable else: *True*

* **transform** -- use :class:`svgwrite.mixins.Transform` methods

* **pathLength** -- `<number>`

  the *pathLength* attribute can be used to provide the author's
  computation of the total length of the path so that the user agent can
  scale distance-along-a-path computations by the ratio of 'pathLength' to
  the user agent's own computed value for total path length.
  A "moveto" operation within a 'path' element is defined to have zero length.

* **d** -- `string`

  The definition of the outline of a shape, use push-method to add commands
  and coordinates

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
