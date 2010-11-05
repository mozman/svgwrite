LinearGradient
==============

.. automodule:: svgwrite.gradients

.. seealso::

  * http://www.w3.org/TR/SVG11/pservers.html#Gradients
  * http://www.w3.org/TR/SVG11/pservers.html#LinearGradients

.. autoclass:: svgwrite.gradients.LinearGradient

Methods
-------

.. automethod:: svgwrite.gradients.LinearGradient.__init__

.. automethod:: svgwrite.gradients.LinearGradient.add_stop_color

.. automethod:: svgwrite.gradients.LinearGradient.get_paint_server

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed
  even if external resources are unavailable else: *True*

* **gradientUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for attributes **x1**, **y1**, **x2** and **y2**.

  .. seealso:: http://www.w3.org/TR/SVG11/pservers.html#LinearGradientElementGradientUnitsAttribute

* **gradientTransform** -- `<transform-list>`

  Use the :class:`-svgwrite.mixins.Transform` interface to set transformations.

  Contains the definition of an optional additional transformation from the
  gradient coordinate system onto the target coordinate system (i.e.,
  userSpaceOnUse or objectBoundingBox). This allows for things such as skewing
  the gradient. This additional transformation matrix is post-multiplied to
  (i.e., inserted to the right of) any previously defined transformations,
  including the implicit transformation necessary to convert from object
  bounding box units to user space.

* **x1** -- `<coordinate>`  -- **start** parameter

  **x1**, **y1**, **x2** and **y2** define a gradient vector for the linear
  gradient. This gradient vector provides starting and ending points onto
  which the gradient stops are mapped. The values of **x1**, **y1**, **x2**
  and **y2** can be either numbers or percentages.

  default is ``'0%'``

* **y1** -- `<coordinate>`  -- **start** parameter

  See **x1**. Default is ``'0%'``

* **x2** -- `<coordinate>` -- **end** parameter

  See **x1**. Default is ``'100%'``

* **y2** -- `<coordinate>` -- **end** parameter

  See **x1**. Default is ``'0%'``

* **spreadMethod** -- ``'pad | reflect | repeat'``

  Indicates what happens if the gradient starts or ends inside the bounds of
  the target rectangle. Possible values are: ``'pad'``, which says to use the
  terminal colors of the gradient to fill the remainder of the target region,
  ``'reflect'``, which says to reflect the gradient pattern start-to-end,
  end-to-start, start-to-end, etc. continuously until the target rectangle is
  filled, and ``'repeat'``, which says to repeat the gradient pattern start-to-end,
  start-to-end, start-to-end, etc. continuously until the target region is
  filled.

  default is ``'pad'``

* **xlink:href** -- `<iri>` -- **inherit** parameter

  A URI reference to a different :class:`LinearGradient` or :class:`RadialGradient`
  element within the current SVG document fragment. Any :class:`LinearGradient`
  attributes which are defined on the referenced element which are not defined
  on this element are inherited by this element. If this element has no defined
  gradient stops, and the referenced element does (possibly due to its own
  **xlink:href** attribute), then this element inherits the gradient stop from
  the referenced element. Inheritance can be indirect to an arbitrary level;
  thus, if the referenced element inherits attribute or gradient stops due to
  its own **xlink:href** attribute, then the current element can inherit those
  attributes or gradient stops.

RadialGradient
==============

.. seealso:: http://www.w3.org/TR/SVG11/pservers.html#RadialGradients

.. autoclass:: svgwrite.gradients.RadialGradient

Methods
-------

.. automethod:: svgwrite.gradients.RadialGradient.__init__

.. automethod:: svgwrite.gradients.RadialGradient.add_stop_color

.. automethod:: svgwrite.gradients.RadialGradient.get_paint_server

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed
  even if external resources are unavailable else: *True*

* **gradientUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for attributes **cx**, **cy**, **r**, **fx**
  and **fy**.

  .. seealso:: http://www.w3.org/TR/SVG11/pservers.html#RadialGradientElementGradientUnitsAttribute

* **cx** -- `<coordinate>` -- **center** parameter

  **cx**, **cy** and **r** define the largest (i.e., outermost) circle for
  the radial gradient. The gradient will be drawn such that the 100% gradient
  stop is mapped to the perimeter of this largest (i.e., outermost) circle.

  default is ``'50%'``

* **cy** -- `<coordinate>` -- **center** parameter

  See **cx**. Default is ``'50%'``.

* **r** -- `<length>` -- **r** parameter

  See **cx**.

  A value of zero will cause the area to be painted as a single color using
  the color and opacity of the last gradient stop.

  Default is ``'50%'``.

* **fx** -- `<coordinate>` -- **focal** parameter

  **fx** and **fy** define the focal point for the radial gradient. The
  gradient will be drawn such that the 0% gradient stop is mapped to (fx, fy).
  If attribute **fx** is not specified, **fx** will coincide with the
  presentational value of **cx** for the element whether the value for **cx**
  was inherited or not. If the element references an element that specifies a
  value for **fx**, then the value of 'fx' is inherited from the referenced
  element.

* **fy** -- `<coordinate>` -- **focal** parameter

  See **fx**.
  If attribute **fy** is not specified, **fy** will coincide with the
  presentational vlaue of **cy** for the element whether the value for **cy**
  was inherited or not. If the element references an element that specifies a
  value for **fy**, then the value of **fy** is inherited from the referenced
  element.

* **gradientTransform** -- `<transform-list>`

  Use the :class:`-svgwrite.mixins.Transform` interface to set transformations.

  See :class:`LinearGradient`

* **spreadMethod** -- ``'pad | reflect | repeat'``

  See :class:`LinearGradient`

* **xlink:href** -- `<iri>` -- **inherit** parameter

  See :class:`LinearGradient`