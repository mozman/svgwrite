Pattern
=======

.. autoclass:: svgwrite.pattern.Pattern

.. seealso:: http://www.w3.org/TR/SVG11/pservers.html#PatternElement

Methods
-------

.. automethod:: svgwrite.pattern.Pattern.__init__

.. method:: Pattern.add

Add **element** to the pattern content.

The contents of the **pattern** are relative to a new coordinate system.
If there is a **viewBox** attribute, then the new coordinate system is fitted
into the region defined by the **x**, **y**, **width**, **height** and
**patternUnits** attributes on the **pattern** element using the standard
rules for **viewBox** and **preserveAspectRatio**. If there is no **viewBox**
attribute, then the new coordinate system has its origin at (x, y), where x
is established by the **x** attribute on the **pattern** element, and y is
established by the **y** attribute on the ‘pattern’ element. Thus, in the
following example::

  <pattern x="10" y="10" width="20" height="20">
    <rect x="5" y="5" width="10" height="10"/>
  </pattern>

or as :mod:`svgwrite` calls::

  # dwg is the main svg drawing
  pattern = dwg.pattern(insert=(10, 10), size=(20, 20))
  pattern.add(dwg.rect(insert=(5, 5), size=(10, 10))

the rectangle has its top/left located 5 units to the right and 5 units down
from the origin of the pattern tile.

SVG Attributes
--------------

* **patternUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for attributes **x**, **y**, **width** and
  **height**.

  If patternUnits= ``'userSpaceOnUse'`` , **x** , **y**, **width** and **height**
  represent values in the coordinate system that results from taking the
  current user coordinate system in place at the time when the **pattern**
  element is referenced (i.e., the user coordinate system for the element
  referencing the **pattern** element via a **fill** or **stroke** property)
  and then applying the transform specified by attribute **patternTransform**.

  If patternUnits= ``'objectBoundingBox'`` , the user coordinate system for
  attributes **x**, **y**, **width** and **height** is established using the
  bounding box of the element to which the pattern is applied (see Object
  bounding box units) and then applying the transform specified by attribute
  **patternTransform**.

  Default is ``'objectBoundingBox'``.

* **patternContentUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  Defines the coordinate system for the contents of the **pattern**. Note that
  this attribute has no effect if attribute **viewBox** is specified.

  If patternContentUnits= ``'userSpaceOnUse'`` , the user coordinate system for
  the contents of the **pattern** element is the coordinate system that
  results from taking the current user coordinate system in place at the time
  when the **pattern** element is referenced (i.e., the user coordinate system
  for the element referencing the **pattern** element via a **fill** or
  **stroke** property) and then applying the transform specified by attribute
  **patternTransform**.

  If patternContentUnits= ``'objectBoundingBox'`` , the user coordinate system
  for the contents of the **pattern** element is established using the bounding
  box of the element to which the pattern is applied (see Object bounding box
  units) and then applying the transform specified by attribute
  **patternTransform**.

  Default is ``'userSpaceOnUse'``.

* **patternTransform** -- `<transform-list>`

  Use the :class:`~svgwrite.mixins.Transform` interface to set transformations.

  Contains the definition of an optional additional transformation from the
  pattern coordinate system onto the target coordinate system (i.e.,
  ``'userSpaceOnUse'`` or ``'objectBoundingBox'``). This allows for things
  such as skewing the pattern tiles. This additional transformation matrix is
  post-multiplied to (i.e., inserted to the right of) any previously defined
  transformations, including the implicit transformation necessary to convert
  from object bounding box units to user space.

* **x** -- `<coordinate>` -- **insert** parameter

  **x**, **y**, **width** and **height** indicate how the pattern tiles are
  placed and spaced. These attributes represent coordinates and values in the
  coordinate space specified by the combination of attributes **patternUnits**
  and **patternTransform**.

  Default is ``'0'``.

* **y** -- `<coordinate>` -- **center** parameter

  See **x**.

  Default is ``'0'``.

* **width** -- `<length>` -- **size** parameter

  See **x**.

  A negative value is an error. A value of zero disables rendering of the
  element (i.e., no paint is applied).

  Default is ``'0'``.

* **height** -- `<length>` -- **size** parameter

  See **x**.

  A negative value is an error. A value of zero disables rendering of the
  element (i.e., no paint is applied).

  Default is ``'0'``.

* **xlink:href** -- `string` -- **inherit** parameter

  A URI reference to a different **pattern** element within the current SVG
  document fragment. Any attributes which are defined on the referenced
  element which are not defined on this element are inherited by this element.
  If this element has no children, and the referenced element does (possibly
  due to its own **xlink:href** attribute), then this element inherits the
  children from the referenced element. Inheritance can be indirect to an
  arbitrary level; thus, if the referenced element inherits attributes or
  children due to its own **xlink:href** attribute, then the current element
  can inherit those attributes or children.

* **preserveAspectRatio** -- ``'[defer] <align> [<meetOrSlice>]'``

  Use the :class:`~svgwrite.mixins.ViewBox` interface to set **viewbox**
  and **preserveAspectRatio**.
