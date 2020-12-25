Line
====

.. autoclass:: svgwrite.shapes.Line

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#LineElement

.. automethod:: svgwrite.shapes.Line.__init__

SVG Attributes
--------------

* **x1** -- `<coordinate>` -- **start** parameter
* **y1** -- `<coordinate>` -- **start** parameter
* **x2** -- `<coordinate>` -- **end** parameter
* **y2** -- `<coordinate>` -- **end** parameter

Common SVG Attributes
---------------------

These are the common SVG Attributes for Line, Rect, Circle, Ellipse,
Poliyline and Polygon.

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given
  element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **transform** -- use :class:`svgwrite.mixins.Transform` interface

Common Standard SVG Attributes
------------------------------

These are the common Standard SVG Attributes for Line, Rect, Circle, Ellipse,
Poliyline and Polygon.

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Markers`

Rect
====

.. autoclass:: svgwrite.shapes.Rect

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#RectElement

.. automethod:: svgwrite.shapes.Rect.__init__

SVG Attributes
--------------

* **x** -- `<coordinate>` -- **insert** parameter

  The x-axis coordinate of the side of the
  rectangle which has the smaller x-axis coordinate value

* **y** -- `<coordinate>` -- **insert** parameter

  The y-axis coordinate of the side of the
  rectangle which has the smaller y-axis coordinate value

* **width** -- `<length>` -- **size** parameter

* **height** -- `<length>` -- **size** parameter

* **rx** -- `<length>` -- **rx** parameter

  For rounded rectangles, the y-axis radius of the
  ellipse used to round off the corners of the rectangle.

* **ry** -- `<length>` -- **ry** parameter

  For rounded rectangles, the y-axis radius of the
  ellipse used to round off the corners of the rectangle.


Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`

Circle
======

.. autoclass:: svgwrite.shapes.Circle

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#CircleElement

.. automethod:: svgwrite.shapes.Circle.__init__

SVG Attributes
--------------

* **cx** -- `<coordinate>` -- **center** parameter

  The x-axis coordinate of the center of the circle.

* **cy** -- `<coordinate>` -- **center** parameter

  The y-axis coordinate of the center of the circle.

* **r** -- `<length>` -- **r** parameter

  The radius of the circle.

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`

Ellipse
=======

.. autoclass:: svgwrite.shapes.Ellipse

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#EllipseElement

.. automethod:: svgwrite.shapes.Ellipse.__init__

SVG Attributes
--------------

* **cx** -- `<coordinate>` -- **center** parameter

  The x-axis coordinate of the center of the ellipse.

* **cy** -- `<coordinate>` -- **center** parameter

  The y-axis coordinate of the center of the ellipse.

* **rx** -- `<length>` -- **r** parameter

  The x-axis radius of the ellipse.

* **ry** -- `<length>` -- **r** parameter

  The y-axis radius of the ellipse.

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`

Polyline
========

.. autoclass:: svgwrite.shapes.Polyline

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#PolylineElement

.. automethod:: svgwrite.shapes.Polyline.__init__

Attributes
----------

.. attribute:: Polyline.points

   `list` of points, a point is a `2-tuple` (x, y): x, y = `<number>`

SVG Attributes
--------------

* **points** -- `list` of points  -- **points** parameter

  The points that make up the polyline. All coordinate values are in the
  **user coordinate system** (no units allowed).

How to append points::

    Polyline.points.append( point )
    Polyline.points.extend( [point1, point2, point3, ...] )

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Markers`

Polygon
=======

.. autoclass:: svgwrite.shapes.Polygon

.. seealso:: http://www.w3.org/TR/SVG11/shapes.html#PolygonElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Markers`

Basic Shapes Examples
=====================

.. literalinclude:: ../../examples/basic_shapes.py
   :lines: 16-

basic_shapes.svg
----------------

.. image:: ../../examples/basic_shapes.svg
   :width: 800
   :height: 800
   :alt: Your browser can't render SVG images.