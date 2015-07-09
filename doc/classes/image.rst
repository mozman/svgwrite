Image
=====

.. autoclass:: svgwrite.image.Image

Methods
-------

.. automethod:: svgwrite.image.Image.__init__

.. automethod:: svgwrite.image.Image.stretch

.. automethod:: svgwrite.image.Image.fit

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
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

* **transform** -- use :class:`svgwrite.mixins.Transform` interface

* **x** -- `<coordinate>` -- **insert** parameter

  The x-axis coordinate of one corner of the rectangular region into which
  the referenced document is placed.

  Default is ``'0'``.

* **y** -- `<coordinate>` -- **insert** parameter

  The y-axis coordinate of one corner of the rectangular region into which
  the referenced document is placed.

  Default is ``'0'``.

* **width** -- `<length>` -- **size** parameter

  The width of the rectangular region into which the referenced document is
  placed. A negative value is an error. A value of zero disables rendering
  of the element.

* **height** -- `<length>` -- **size** parameter

  The height of the rectangular region into which the referenced document is
  placed. A negative value is an error. A value of zero disables rendering of
  the element.

* **xlink:href** -- `string` -- **href** parameter

  A IRI reference to the image resource.

* **preserveAspectRatio** -- ``'[defer] <align> [<meetOrSlice>]'``

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
