.. _feColorMatrix:

feColorMatrix Filter Element
============================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feColorMatrixElement

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **type** -- ``'matrix | saturate | hueRotate | luminanceToAlpha'``

  Indicates the type of matrix operation. The keyword **matrix** indicates
  that a full 5x4 matrix of values will be provided. The other keywords
  represent convenience shortcuts to allow commonly used color operations to
  be performed without specifying a complete matrix. If attribute **type**
  is not specified, then the effect is as if a value of matrix were specified.

* **values** = `list of <number>s`

  The contents of **values** depends on the value of attribute **type** see:
  http://www.w3.org/TR/SVG11/filters.html#feColorMatrixValuesAttribute



