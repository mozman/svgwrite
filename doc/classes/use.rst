Use
===

.. autoclass:: svgwrite.container.Use

.. seealso:: http://www.w3.org/TR/SVG11/struct.html#UseElement

.. automethod:: svgwrite.container.Use.__init__

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.interface.ITransform`
* :class:`svgwrite.interface.IXLink`
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

* **x** -- `<coordinate>`

  The x-axis coordinate of one corner of the rectangular region into which
  the referenced element is placed.

  Default is ``'0'``.

* **y** -- `<coordinate>`

  The y-axis coordinate of one corner of the rectangular region into which the
  referenced element is placed.

  Default is ``'0'``.

* **width** -- `<length>`

  The width of the rectangular region into which the referenced element is
  placed. A negative value is an error. A value of zero disables rendering
  of this element.

  Default is ``'100%'``.

* **height** -- `<length>`

  The height of the rectangular region into which the referenced element is
  placed. A negative value is an error. A value of zero disables rendering
  of this element.

  Default is ``'100%'``.

* **transform** -- :class:`svgwrite.interface.ITransform` interface

* **xlink:href** -- `string`

  set on __init__(href)

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
