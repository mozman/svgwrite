.. _feTurbulence:

feTurbulence Filter Element
===========================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feTurbulenceElement

This filter primitive creates an image using the Perlin turbulence function. It
allows the synthesis of artificial textures like clouds or marble. For a
detailed description the of the Perlin turbulence function, see "Texturing and
Modeling", Ebert et al, AP Professional, 1994. The resulting image will fill the
entire filter primitive subregion for this filter primitive.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)

* **baseFrequency** -- `<number-optional-number>`

    The base frequency (frequencies) parameter(s) for the noise function. If two
    `<number>s` are provided, the first number represents a base frequency in
    the X direction and the second value represents a base frequency in the Y
    direction. If one number is provided, then that value is used for both X
    and Y.

    A negative value for base frequency is an error.

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified.

* **numOctaves** -- `<integer>`

    The numOctaves parameter for the noise function.

    If the attribute is not specified, then the effect is as if a value of ``'1'``
    were specified.

* **seed** -- `<number>`

    The starting number for the pseudo random number generator.

    If the attribute is not specified, then the effect is as if a value of ``'0'``
    were specified. When the seed number is handed over to the algorithm above
    it must first be truncated, i.e. rounded to the closest integer value
    towards zero.

* **stitchTiles** -- ``'stitch | noStitch'``

    * ``'noStitch'`` -- no attempt it made to achieve smooth transitions at the
      border of tiles which contain a turbulence function. Sometimes the result
      will show clear discontinuities at the tile borders.

    * ``'stitch'`` -- then the user agent will automatically adjust
      baseFrequency-x and baseFrequency-y values such that the **feTurbulence**
      node's width and height (i.e., the width and height of the current
      subregion) contains an integral number of the Perlin tile width and
      height for the first octave. The baseFrequency will be adjusted up or
      down depending on which way has the smallest relative (not absolute)
      change as follows: Given the frequency, calculate
      lowFreq=floor(width*frequency)/width and hiFreq=ceil(width*frequency)/width.
      If frequency/lowFreq < hiFreq/frequency then use lowFreq, else use hiFreq.
      While generating turbulence values, generate lattice vectors as normal for
      Perlin Noise, except for those lattice points that lie on the right or
      bottom edges of the active area (the size of the resulting tile). In
      those cases, copy the lattice vector from the opposite edge of the active
      area.

    If attribute **stitchTiles** is not specified, then the effect is as if
    a value of ``'noStitch'`` were specified.

* **type** -- ``'fractalNoise | turbulence'``

    Indicates whether the filter primitive should perform a noise or turbulence
    function. If attribute **type** is not specified, then the effect is as if
    a value of ``'turbulence'`` were specified.
