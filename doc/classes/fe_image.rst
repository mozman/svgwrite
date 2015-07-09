.. _feImage:

feImage Filter Element
======================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feImageElement

This filter primitive refers to a graphic external to this filter element, which
is loaded or rendered into an RGBA raster and becomes the result of the filter
primitive.

This filter primitive can refer to an external image or can be a reference to
another piece of SVG. It produces an image similar to the built-in image source
``'SourceGraphic'`` except that the graphic comes from an external source.

If the **xlink:href** references a stand-alone image resource such as a
JPEG, PNG or SVG file, then the image resource is rendered according to the
behavior of the **image** element; otherwise, the referenced resource is rendered
according to the behavior of the **use** element. In either case, the current
user coordinate system depends on the value of attribute **primitiveUnits** on
the **filter** element. The processing of the **preserveAspectRatio** attribute
on the **feImage** element is identical to that of the **image** element.

When the referenced image must be resampled to match the device coordinate system,
it is recommended that high quality viewers make use of appropriate interpolation
techniques, for example bilinear or bicubic. Depending on the speed of the
available interpolents, this choice may be affected by the **image-rendering**
property setting.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **xlink:href** -- `<iri>`

    A IRI reference to the image source.

* **preserveAspectRatio** -- ``'[defer] <align> [<meetOrSlice>]'``

    If attribute **preserveAspectRatio** is not specified, then the effect is
    as if a value of ``'xMidYMid'`` meet were specified.