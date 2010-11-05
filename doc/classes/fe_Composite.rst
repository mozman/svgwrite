.. _feComposite:

feComposite Filter Element
==========================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feCompositeElement

This filter performs the combination of the two input images pixel-wise in image
space using one of the Porter-Duff compositing operations: over, in, atop, out,
xor. Additionally, a component-wise arithmetic operation (with the result clamped
between [0..1]) can be applied.

The arithmetic operation is useful for combining the output from the
**feDiffuseLighting** and **feSpecularLighting** filters with texture data.
It is also useful for implementing dissolve. If the arithmetic operation is
chosen, each result pixel is computed using the following formula::

  result = k1*i1*i2 + k2*i1 + k3*i2 + k4

For this filter primitive, the extent of the resulting image might grow as
described in the section that describes the filter primitive subregion.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **operator** -- ``'over | in | out | atop | xor | arithmetic``

  The compositing operation that is to be performed. All of the **operator**
  types except arithmetic match the correspond operation as described in [PORTERDUFF].
  The arithmetic operator is described above. If attribute **operator** is not
  specified, then the effect is as if a value of ``'over'`` were specified.

* **k1**, **k2**, **k3**, **k4** -- `<number>`

    Only applicable if **operator** = ``'arithmetic'``.
    If the attribute is not specified, the effect is as if a value of 0 were specified.

* **in2** -- (see :ref:`in <in_attr>` attribute)

    The second input image to the compositing operation. This attribute can
    take on the same values as the **in** attribute.

