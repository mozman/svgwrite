.. _feConvolveMatrix:

feConvolveMatrix Filter Element
===============================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feConvolveMatrixElement

**feConvolveMatrix** applies a matrix convolution filter effect. A convolution
combines pixels in the input image with neighboring pixels to produce a resulting
image. A wide variety of imaging operations can be achieved through convolutions,
including blurring, edge detection, sharpening, embossing and beveling.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **order** -- `<number-optional-number>`

    Indicates the number of cells in each dimension for **kernelMatrix**. The
    values provided must be `<integer>`s greater than zero. The first number,
    `<orderX>`, indicates the number of columns in the matrix. The second number,
    `<orderY>`, indicates the number of rows in the matrix. If `<orderY>` is not
    provided, it defaults to <orderX>.

    If the attribute is not specified, the effect is as if a value of 3 were
    specified.

* **kernelMatrix** -- `<list of numbers>`

    The list of `<number>`s that make up the kernel matrix for the convolution.
    Values are separated by space characters and/or a comma. The number of
    entries in the list must equal `<orderX>` times `<orderY>`.

* **divisor** -- `<number>`

    After applying the **kernelMatrix** to the input image to yield a number,
    that number is divided by **divisor** to yield the final destination color
    value. The default value is the sum of all values in **kernelMatrix**, with
    the exception that if the sum is zero, then the divisor is set to 1.

* **bias** = `<number>`

    After applying the **kernelMatrix** to the input image to yield a number and
    applying the **divisor**, the **bias** attribute is added to each component.

* **targetX** -- `<integer>`

    Determines the positioning in X of the convolution matrix relative to a
    given target pixel in the input image. The leftmost column of the matrix is
    column number zero. The value must be such that: 0 <= targetX < orderX. By
    default, the convolution matrix is centered in X over each pixel of the
    input image (i.e., targetX = floor ( orderX / 2 )).

* **targetY** -- `<integer>`
    Determines the positioning in Y of the convolution matrix relative to a
    given target pixel in the input image. The topmost row of the matrix is
    row number zero. The value must be such that: 0 <= targetY < orderY. By
    default, the convolution matrix is centered in Y over each pixel of the
    input image (i.e., targetY = floor ( orderY / 2 )).

* **edgeMode** -- ``'duplicate | wrap | none'``

    Determines how to extend the input image as necessary with color values so
    that the matrix operations can be applied when the kernel is positioned at
    or near the edge of the input image.

    * ``'duplicate'`` indicates that the input image is extended along each of its
      borders as necessary by duplicating the color values at the given edge of
      the input image.

    * ``'wrap'`` indicates that the input image is extended by taking the color
      values from the opposite edge of the image.

    * ``'none'`` indicates that the input image is extended with pixel values of
      zero for R, G, B and A.

    If attribute **edgeMode** is not specified, then the effect is as if a value
    of ``'duplicate'`` were specified.

* **kernelUnitLength** -- `<number-optional-number>`

    The first number is the `<dx>` value. The second number is the `<dy>` value.
    If the `<dy>` value is not specified, it defaults to the same value as `<dx>`.
    Indicates the intended distance in current filter units (i.e., units as
    determined by the value of attribute **primitiveUnits**) between successive
    columns and rows, respectively, in the **kernelMatrix**. By specifying
    value(s) for **kernelUnitLength**, the kernel becomes defined in a scalable,
    abstract coordinate system. If **kernelUnitLength** is not specified, the
    default value is one pixel in the offscreen bitmap, which is a pixel-based
    coordinate system, and thus potentially not scalable. For some level of
    consistency across display media and user agents, it is necessary that a
    value be provided for at least one of **filterRes** and **kernelUnitLength**.
    In some implementations, the most consistent results and the fastest performance
    will be achieved if the pixel grid of the temporary offscreen images aligns
    with the pixel grid of the kernel. A negative or zero value is an error.

* **preserveAlpha** -- ``'false | true'``

    A value of false indicates that the convolution will apply to all channels,
    including the alpha channel.

    A value of true indicates that the convolution will only apply to the color
    channels. In this case, the filter will temporarily unpremultiply the color
    component values, apply the kernel, and then re-premultiply at the end.

    If **preserveAlpha** is not specified, then the effect is as if a value of
    ``'false'`` were specified.
