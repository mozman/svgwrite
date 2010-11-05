.. _feDisplacementMap:

feDisplacementMap Filter Element
================================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feDisplacementMapElement

This filter primitive uses the pixels values from the image from **in2** to
spatially displace the image from **in**.

This filter can have arbitrary non-localized effect on the input which might
require substantial buffering in the processing pipeline. However with this
formulation, any intermediate buffering needs can be determined by scale which
represents the maximum range of displacement in either x or y.

When applying this filter, the source pixel location will often lie between
several source pixels. In this case it is recommended that high quality viewers
apply an interpolent on the surrounding pixels, for example bilinear or bicubic,
rather than simply selecting the nearest source pixel. Depending on the speed of
the available interpolents, this choice may be affected by the
**image-rendering** property setting.

The **color-interpolation-filters** property only applies to the **in2** source
image and does not apply to the **in** source image. The ‘in’ source image must
remain in its current color space.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **in2** -- (see :ref:`in <in_attr>` attribute)

    The second input image, which is used to displace the pixels in the image
    from attribute **in**. This attribute can take on the same values as the
    **in** attribute.

* **scale** -- `<number>`

    Displacement scale factor. The amount is expressed in the coordinate system
    established by attribute **primitiveUnits** on the **filter** element.

    When the value of this attribute is ``'0'``, this operation has no effect on the
    source image.

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.

* **xChannelSelector** -- ``'R | G | B | A'``

    Indicates which channel from **in2** to use to displace the pixels in **in**
    along the x-axis. If attribute **xChannelSelector** is not specified, then
    the effect is as if a value of ``'A'`` were specified.

* **yChannelSelector** -- ``'R | G | B | A'``

    Indicates which channel from **in2** to use to displace the pixels in **in**
    along the y-axis. If attribute **yChannelSelector** is not specified, then
    the effect is as if a value of ``'A'`` were specified.

