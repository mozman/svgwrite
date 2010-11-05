.. _feBlend:

feBlend Filter Element
======================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feBlendElement

This filter composites two objects together using commonly used imaging
software blending modes. It performs a pixel-wise combination of two input
images.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **mode** -- ``'normal | multiply | screen | darken | lighten'``

  One of the image blending modes. If attribute **mode** is not specified,
  then the effect is as if a value of ``'normal'`` were specified.

  see also: http://www.w3.org/TR/SVG11/filters.html#feBlendModeAttribute

* **in** -- (see :ref:`in <in_attr>` attribute)

* **in2** -- (see :ref:`in <in_attr>` attribute)

  The second input image to the blending operation. This attribute can take
  on the same values as the **in** attribute.
