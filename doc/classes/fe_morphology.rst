.. _feMorphology:

feMorphology Filter Element
=============================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feMorphologyElement

This filter primitive performs "fattening" or "thinning" of artwork. It is
particularly useful for fattening or thinning an alpha channel.

The dilation (or erosion) kernel is a rectangle with a width of 2*x-radius and a
height of 2*y-radius. In dilation, the output pixel is the individual
component-wise maximum of the corresponding R,G,B,A values in the input image's
kernel rectangle. In erosion, the output pixel is the individual component-wise
minimum of the corresponding R,G,B,A values in the input image's kernel rectangle.

Frequently this operation will take place on alpha-only images, such as that
produced by the built-in input, ``'SourceAlpha'``. In that case, the implementation
might want to optimize the single channel case.

If the input has infinite extent and is constant, this operation has no effect.
If the input has infinite extent and is a tile, the filter is evaluated with
periodic boundary conditions.

Because **feMorphology** operates on premultipied color values, it will always
result in color values less than or equal to the alpha channel.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **operator** -- ``'erode | dilate'``

    A keyword indicating whether to erode (i.e., thin) or dilate (fatten) the
    source graphic. If attribute **operator** is not specified, then the effect
    is as if a value of ``'erode'`` were specified.

* **radius** -- `<number-optional-number>`

    The radius (or radii) for the operation. If two `<number>s` are provided,
    the first number represents a x-radius and the second value represents a
    y-radius. If one number is provided, then that value is used for both X and
    Y. The values are in the coordinate system established by attribute
    **primitiveUnits** on the **filter** element.

    A negative value is an error. A value of zero disables the effect of the
    given filter primitive (i.e., the result is a transparent black image).

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.
