.. _filter_primitive:

Filter Primitives Overview
==========================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#FilterPrimitivesOverview

Unless otherwise stated, all image filters operate on premultiplied RGBA
samples. Filters which work more naturally on non-premultiplied data
(feColorMatrix and feComponentTransfer) will temporarily undo and redo
premultiplication as specified. All raster effect filtering operations take
1 to N input RGBA images, additional attributes as parameters, and produce a
single output RGBA image.

The RGBA result from each filter primitive will be clamped into the allowable
ranges for colors and opacity values. Thus, for example, the result from a
given filter primitive will have any negative color values or opacity values
adjusted up to color/opacity of zero.

The color space in which a particular filter primitive performs its operations
is determined by the value of property **color-interpolation-filters** on the
given filter primitive. A different property, **color-interpolation** determines
the color space for other color operations. Because these two properties have
different initial values (**color-interpolation-filters** has an initial value
of linearRGB whereas **color-interpolation** has an initial value of sRGB),
in some cases to achieve certain results (e.g., when coordinating gradient
interpolation with a filtering operation) it will be necessary to explicitly
set **color-interpolation** to linearRGB or **color-interpolation-filters**
to sRGB on particular elements. Note that the examples below do not explicitly
set either **color-interpolation** or **color-interpolation-filters**, so the
initial values for these properties apply to the examples.

Common SVG Attributes for Filter Primitives
===========================================

With the exception of the **in** attribute, all of the following attributes
are available on all filter primitive elements:

* **x** -- `<coordinate>`

  The minimum x coordinate for the subregion which restricts calculation and
  rendering of the given filter primitive. See filter primitive subregion.

* **y** -- `<coordinate>`

  The minimum y coordinate for the subregion which restricts calculation and
  rendering of the given filter primitive. See filter primitive subregion.

* **width** -- `<length>`

  The width of the subregion which restricts calculation and rendering of the
  given filter primitive. See filter primitive subregion.

* **height** -- `<length>`

  The height of the subregion which restricts calculation and rendering of
  the given filter primitive. See filter primitive subregion.

* **result** -- `<filter-primitive-reference>`

  Assigned name for this filter primitive. If supplied, then graphics that
  result from processing this filter primitive can be referenced by an **in**
  attribute on a subsequent filter primitive within the same **filter** element.
  If no value is provided, the output will only be available for re-use as
  the implicit input into the next filter primitive if that filter primitive
  provides no value for its **in** attribute.

.. _in_attr:

* **in** -- ``'SourceGraphic | SourceAlpha | BackgroundImage | BackgroundAlpha
  | FillPaint | StrokePaint'`` | `<filter-primitive-reference>`

  Identifies input for the given filter primitive. The value can be either
  one of six keywords or can be a string which matches a previous **result**
  attribute value within the same **filter** element. If no value is provided
  and this is the first filter primitive, then this filter primitive will use
  ``'SourceGraphic'`` as its input. If no value is provided and this is a subsequent
  filter primitive, then this filter primitive will use the result from the
  previous filter primitive as its input.

  * **SourceGraphic**

    This keyword represents the graphics elements that were the original input
    into the **filter** element. For raster effects filter primitives, the
    graphics elements will be rasterized into an initially clear RGBA raster
    in image space. Pixels left untouched by the original graphic will be left
    clear. The image is specified to be rendered in linear RGBA pixels. The
    alpha channel of this image captures any anti-aliasing specified by SVG.
    (Since the raster is linear, the alpha channel of this image will represent
    the exact percent coverage of each pixel.)

  * **SourceAlpha**

    This keyword represents the graphics elements that were the original
    input into the **filter** element. SourceAlpha has all of the same rules
    as SourceGraphic except that only the alpha channel is used. The input
    image is an RGBA image consisting of implicitly black color values for
    the RGB channels, but whose alpha channel is the same as SourceGraphic.
    If this option is used, then some implementations might need to rasterize
    the graphics elements in order to extract the alpha channel.

  * **BackgroundImage**

    This keyword represents an image snapshot of the canvas under the filter
    region at the time that the **filter** element was invoked. See Accessing
    the background image.

  * **BackgroundAlpha**

    Same as BackgroundImage except only the alpha channel is used. See
    SourceAlpha and Accessing the background image.

  * **FillPaint**

    This keyword represents the value of the **fill** property on the target
    element for the filter effect. The FillPaint image has conceptually
    infinite extent. Frequently this image is opaque everywhere, but it might
    not be if the `"paint"` itself has alpha, as in the case of a gradient or
    pattern which itself includes transparent or semi-transparent parts.

  * **StrokePaint**

    This keyword represents the value of the **stroke** property on the target
    element for the filter effect. The StrokePaint image has conceptually
    infinite extent. Frequently this image is opaque everywhere, but it might
    not be if the `"paint"` itself has alpha, as in the case of a gradient or
    pattern which itself includes transparent or semi-transparent parts.
