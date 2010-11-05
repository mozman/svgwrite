.. _feGaussianBlur:

feGaussianBlur Filter Element
=============================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feGaussianBlurElement

This filter primitive performs a Gaussian blur on the input image.

Frequently this operation will take place on alpha-only images, such as that
produced by the built-in input, ``'SourceAlpha'``. The implementation may notice
this and optimize the single channel case. If the input has infinite extent and
is constant, this operation has no effect. If the input has infinite extent and
is a tile, the filter is evaluated with periodic boundary conditions.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **stdDeviation** -- `<number-optional-number>`

    The standard deviation for the blur operation. If two `<number>s` are
    provided, the first number represents a standard deviation value along the
    x-axis of the coordinate system established by attribute **primitiveUnits**
    on the **filter** element. The second value represents a standard deviation
    in Y. If one number is provided, then that value is used for both X and Y.

    A negative value is an error. A value of zero disables the effect of the
    given filter primitive (i.e., the result is the filter input image).

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.