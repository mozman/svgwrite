.. _feDiffuseLighting:

feDiffuseLighting Filter Element
================================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feDiffuseLightingElement

This filter primitive lights an image using the alpha channel as a bump map. The
resulting image is an RGBA opaque image based on the light color with alpha = 1.0
everywhere. The lighting calculation follows the standard diffuse component of
the Phong lighting model. The resulting image depends on the light color, light
position and surface geometry of the input bump map.

The light map produced by this filter primitive can be combined with a texture
image using the multiply term of the arithmetic **feComposite** compositing method.
Multiple light sources can be simulated by adding several of these light maps
together before applying it to the texture image.

For common properties see: :ref:`filter_primitive`

Methods
-------

.. method:: feDiffuseLighting.feDistantLight(azimuth=0, elevation=0, **extra)

    create and add a light source: :ref:`feDistantLight`

.. method:: feDiffuseLighting.fePointLight(source=(0, 0, 0), **extra)

    :param source: source 3D point (**x**, **y**, **z**)

    create and add a light source: :ref:`fePointLight`

.. method:: feDiffuseLighting.feSpotLight(source=(0, 0, 0), target=(0, 0, 0), **extra)

    :param source: source 3D point (**x**, **y**, **z**)
    :param target: target 3D point (**pointsAtX**, **pointsAtY**, **pointsAtZ**)

    create and add a light source: :ref:`feSpotLight`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **surfaceScale** -- `<number>`

    height of surface when Ain = 1.

    If the attribute is not specified, then the effect is as if a value of 1
    were specified.

* **diffuseConstant** -- `<number>`

    kd in Phong lighting model. In SVG, this can be any non-negative number.

    If the attribute is not specified, then the effect is as if a value of 1
    were specified.

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

* **lighting-color** -- ``'currentColor'`` | `<color>` [`<icccolor>`] | ``'inherit'``

    The **lighting-color** property defines the color of the light source for
    filter primitives **feDiffuseLighting** and **feSpecularLighting**.
