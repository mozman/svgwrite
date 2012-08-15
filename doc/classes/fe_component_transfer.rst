.. _feComponentTransfer:

feComponentTransfer Filter Element
==================================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feComponentTransferElement

This filter primitive performs component-wise remapping of data::

  R' = feFuncR( R )
  G' = feFuncG( G )
  B' = feFuncB( B )
  A' = feFuncA( A )

for every pixel. It allows operations like brightness adjustment, contrast
adjustment, color balance or thresholding.

The calculations are performed on non-premultiplied color values. If the
input graphics consists of premultiplied color values, those values are
automatically converted into non-premultiplied color values for this operation.
(Note that the undoing and redoing of the premultiplication can be avoided if
feFuncA is the identity transform and all alpha values on the source graphic
are set to 1.)

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

Methods
-------

.. method:: feFuncR(type_, \*\*extra)

   create and add a transfer function for the **red** component of the input graphic

.. method:: feFuncG(type_, \*\*extra)

   create and add a transfer function for the **green** component of the input graphic

.. method:: feFuncB(type_, \*\*extra)

   create and add a transfer function for the **blue** component of the input graphic

.. method:: feFuncA(type_, \*\*extra)

   create and add a transfer function for the **alpha** component of the input graphic

Parameters for feFuncX() Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **type** -- ``'identity | table | discrete | linear | gamma'``

  see: http://www.w3.org/TR/SVG11/filters.html#feComponentTransferTypeAttribute

* **tableValues** -- `(list of <number>s)`

  When **type** = ``'table'``, the list of `<number>s` v0,v1,...vn, separated
  by white space and/or a comma, which define the lookup table. An empty list
  results in an identity transfer function.

* **slope** -- `<number>`

  When **type** = ``'linear'``, the slope of the linear function.

* **intercept** -- `<number>`

  When **type** = ``'linear'``, the intercept of the linear function.

* **amplitude** -- `<number>`

  When **type** = ``'gamma'``, the amplitude of the gamma function.

* **exponent** -- `<number>`

  When **type** = ``'gamma'``, the exponent of the gamma function.

* **offset** -- `<number>`

  When **type** = ``'gamma'``, the offset of the gamma function.
