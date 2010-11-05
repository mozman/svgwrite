ClipPath
========

.. autoclass:: svgwrite.masking.ClipPath

Adding clipping elements to :class:`ClipPath`::

  dwg = svgwrite.Drawing()
  clip_path = dwg.defs.add(dwg.clipPath())
  clip_path.add(dwg.circle((100, 100), 50))

.. seealso:: http://www.w3.org/TR/SVG11/masking.html#ClippingPaths

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

* **clipPathUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for the contents of the **clipPath**.

  If clipPathUnits = ``'userSpaceOnUse'`` , the contents of the **clipPath**
  represent values in the current user coordinate system in place at the
  time when the **clipPath** element is referenced (i.e., the user
  coordinate system for the element referencing the **clipPath** element
  via the **clip-path** property).

  If clipPathUnits = ``'objectBoundingBox'`` , then the user coordinate system
  for the contents of the **clipPath** element is established using the
  bounding box of the element to which the clipping path is applied.

  Default is ``'userSpaceOnUse'``

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Presentation Attributes </attributes/presentation>`

Mask
====

.. autoclass:: svgwrite.masking.Mask

.. seealso:: http://www.w3.org/TR/SVG11/masking.html#Masking

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  `False`: if document rendering can proceed even if external resources are
  unavailable else: `True`

* **maskUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for attributes **x**, **y**, **width** and
  **height**.

  If maskUnits = ``'userSpaceOnUse'`` , **x**, **y**, **width** and **height**
  represent values in the current user coordinate system in place at the time
  when the **mask** element is referenced (i.e., the user coordinate system
  for the element referencing the **mask** element via the **mask** property).

  If maskUnits = ``'objectBoundingBox'`` , **x**, **y**, **width** and **height**
  represent fractions or percentages of the bounding box of the element to
  which the mask is applied.

  Default is ``'objectBoundingBox'``.

* **maskContentUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for the contents of the **mask**.

  If maskContentUnits = ``'userSpaceOnUse'`` , the user coordinate system for
  the contents of the **mask** element is the current user coordinate system
  in place at the time when the **mask** element is referenced (i.e., the user
  coordinate system for the element referencing the **mask** element via the
  **mask** property).

  If maskContentUnits = ``'objectBoundingBox'`` , the user coordinate system for
  the contents of the **mask** is established using the bounding box of the
  element to which the mask is applied.

  Default is ``'userSpaceOnUse'``.

* **x** -- `<coordinate>` -- **start** parameter

  The x-axis coordinate of one corner of the rectangle for the largest
  possible offscreen buffer. Note that the clipping path used to render any
  graphics within the mask will consist of the intersection of the current
  clipping path associated with the given object and the rectangle defined by
  **x**, **y**, **width** and **height**.

  Default is ``'-10%'``.

* **y** -- `<coordinate>` -- **start** parameter

  The y-axis coordinate of one corner of the rectangle for the largest
  possible offscreen buffer.

  Default is ``'-10%'``.

* **width** -- `<length>` -- **size** parameter

  The width of the largest possible offscreen buffer. Note that the clipping
  path used to render any graphics within the mask will consist of the
  intersection of the current clipping path associated with the given object
  and the rectangle defined by **x**, **y**, **width** and **height**.

  Default is ``'120%'``.

* **height** -- `<length>` -- **size** parameter

  The height of the largest possible offscreen buffer.

  Default is ``'120%'``.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Presentation Attributes </attributes/presentation>`
