Marker
======

.. autoclass:: svgwrite.container.Marker

.. seealso:: http://www.w3.org/TR/SVG11/painting.html#MarkerElement

example::

    dwg = svgwrite.Drawing()
    # create a new marker object
    marker = dwg.marker(insert=(5,5), size=(10,10))

    # red point as marker
    marker.add(dwg.circle((5, 5), r=5, fill='red'))

    # add marker to defs section of the drawing
    dwg.defs.add(marker)

    # create a new line object
    line = dwg.add(dwg.polyline(
        [(10, 10), (50, 20), (70, 50), (100, 30)],
        stroke='black', fill='none'))

    # set marker (start, mid and end markers are the same)
    line.set_markers(marker)

    # or set markers direct as SVG Attributes 'marker-start', 'marker-mid',
    # 'marker-end' or 'marker' if all markers are the same.
    line['marker'] = marker.get_funciri()

    # NEW in v1.1.11
    # set individually markers, to just set the end marker set other markers to None or False:
    line.set_markers((None, False, marker))

.. automethod:: svgwrite.container.Marker.__init__

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.ViewBox`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given
  element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **viewBox** -- use :class:`svgwrite.mixins.ViewBox` interface

* **preserveAspectRatio** -- use :class:`svgwrite.mixins.ViewBox`
  interface

* **markerUnits** -- ``'strokeWidth|userSpaceOnUse'``

  Defines the coordinate system for attributes **markerWidth**, **markerHeight**
  and the contents of the **marker**.

  If markerUnits -- ``'strokeWidth'``, **markerWidth**,
  **markerHeight** and the contents of the **marker** represent values in a coordinate
  system which has a single unit equal the size in user units of the current
  stroke width in place for the graphic object referencing the marker.

  If markerUnits -- ``'userSpaceOnUse'``, **markerWidth**, **markerHeight** and the
  contents of the **marker** represent values in the current user coordinate
  system in place for the graphic object referencing the marker (i.e., the
  user coordinate system for the element referencing the **marker** element via
  a **marker**, **marker-start**, **marker-mid** or **marker-end** property).

* **refX** -- `<coordinate>` -- **insert** parameter

  The x-axis coordinate of the reference point which is to be aligned exactly
  at the marker position. The coordinate is defined in the coordinate system
  after application of the **viewBox** and **preserveAspectRatio** attributes.
  (default = "0")

* **refY** -- `<coordinate>` -- **insert** parameter

  The y-axis coordinate of the reference point which is to be aligned exactly
  at the marker position. The coordinate is defined in the coordinate system
  after application of the **viewBox** and **preserveAspectRatio** attributes.
  (default = "0")

* **markerWidth** -- `<length>` -- **size** parameter

  Represents the width of the viewport into which the marker is to be fitted
  when it is rendered. (default = "3")

* **markerHeight** -- `<length>` -- **size** parameter

  Represents the height of the viewport into which the marker is to be fitted
  when it is rendered. A value of zero disables rendering of the element.
  (default = "3")

* **orient** -- ``'auto'`` | `<angle>` -- **orient** parameter

  Indicates how the marker is rotated. (SVG default = "0", but for :meth:`__init__`
  ``'auto'`` is the default value)

  .. seealso:: http://www.w3.org/TR/SVG11/painting.html#OrientAttribute

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Presentation Attributes </attributes/presentation>`
