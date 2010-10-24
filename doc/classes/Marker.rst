:class:`Marker` objects --- <marker>
====================================

.. autoclass:: svgwrite.container.Symbol

Inherited Attributes
--------------------

.. attribute:: Marker.attribs

   `dict` of SVG attributes

.. attribute:: Marker.elements

   `list` of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.Marker.add(element)

.. automethod:: svgwrite.container.Marker.tostring()

.. automethod:: svgwrite.container.Marker.get_xml()

Supported Interfaces
--------------------

:class:`svgwrite.interface.IViewBox`
    :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

Used Mixins
-----------

:class:`svgwrite.mixins.Presentation`

    :meth:`fill`, :meth:`stroke`, :meth:`dasharray`

SVG attributes
--------------

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*
* **viewBox** -- use :class:`svgwrite.interface.IViewBox` interface
* **preserveAspectRatio** -- use :class:`svgwrite.interface.IViewBox`
  interface
* **markerUnits** -- ``'strokeWidth|userSpaceOnUse'``
  Defines the coordinate system for attributes **markerWidth**, **markerHeight**
  and the contents of the **marker**.

  If markerUnits=``'strokeWidth'``, **markerWidth**,
  **markerHeight** and the contents of the **marker** represent values in a coordinate
  system which has a single unit equal the size in user units of the current
  stroke width in place for the graphic object referencing the marker.

  If markerUnits=``'userSpaceOnUse'``, **markerWidth**, **markerHeight** and the
  contents of the **marker** represent values in the current user coordinate
  system in place for the graphic object referencing the marker (i.e., the
  user coordinate system for the element referencing the **marker** element via
  a **marker**, **marker-start**, <marker-mid** or **marker-end** property).

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
