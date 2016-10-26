SolidColor
==========

The `solidColor` element is a paint server that provides a single color with opacity. It can be referenced like the
other paint servers (i.e. gradients).

.. autoclass:: svgwrite.solidcolor.SolidColor

.. seealso:: https://www.w3.org/TR/SVGTiny12/painting.html#SolidColorElement


Methods
-------

.. automethod:: svgwrite.solidcolor.SolidColor.__init__

SVG Attributes
--------------

* **solid-color** -- ``'currentColor | <color> | inherit'`` (__init__() parameter `color`)

    The `solid-color` attribute specifies the color that shall be used for this `solidColor` element. The keyword
    ``"currentColor"`` can be specified in the same manner as within a `<paint>` specification for the `fill` and
    `stroke` properties.

* **solid-opacity** -- ``'<opacity-value> | inherit'`` (__init__() parameter `opacity`)

    The `solid-opacity` parameter defines the opacity of the `solidColor`. Any values outside the range `0.0`
    (fully transparent) to `1.0` (fully opaque) must be clamped to this range.