.. _feOffset:

feOffset Filter Element
=======================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feOffsetElement

This filter primitive offsets the input image relative to its current position
in the image space by the specified vector.

This is important for effects like drop shadows.

When applying this filter, the destination location may be offset by a fraction
of a pixel in device space. In this case a high quality viewer should make use
of appropriate interpolation techniques, for example bilinear or bicubic. This
is especially recommended for dynamic viewers where this interpolation provides
visually smoother movement of images. For static viewers this is less of a concern.
Close attention should be made to the **image-rendering** property setting to
determine the authors intent.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **dx** -- `<number>`

    The amount to offset the input graphic along the x-axis. The offset amount
    is expressed in the coordinate system established by attribute **primitiveUnits**
    on the **filter** element.

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.

* **dy** -- `<number>`

    The amount to offset the input graphic along the y-axis. The offset amount
    is expressed in the coordinate system established by attribute **primitiveUnits**
    on the **filter** element.

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.