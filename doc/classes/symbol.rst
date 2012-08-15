Symbol
======

.. autoclass:: svgwrite.container.Symbol

.. seealso:: http://www.w3.org/TR/SVG11/struct.html#SymbolElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.ViewBox`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Clipping`

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

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
