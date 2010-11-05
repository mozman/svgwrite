.. _feTile:

feTile Filter Element
=======================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feTileElement

This filter primitive fills a target rectangle with a repeated, tiled pattern of
an input image. The target rectangle is as large as the filter primitive subregion
established by the **x**, **y**, **width** and **height** attributes on the
**feTile** element.

Typically, the input image has been defined with its own filter primitive
subregion in order to define a reference tile. **feTile** replicates the
reference tile in both X and Y to completely fill the target rectangle. The
top/left corner of each given tile is at location (x+i*width,y+j*height),
where (x,y) represents the top/left of the input image's filter primitive
subregion, width and height represent the width and height of the input
image's filter primitive subregion, and i and j can be any integer value.
In most cases, the input image will have a smaller filter primitive subregion
than the **feTile** in order to achieve a repeated pattern effect.

Implementers must take appropriate measures in constructing the tiled image to
avoid artifacts between tiles, particularly in situations where the user to
device transform includes shear and/or rotation. Unless care is taken,
interpolation can lead to edge pixels in the tile having opacity values lower or
higher than expected due to the interaction of painting adjacent tiles which
each have partial overlap with particular pixels.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **in** -- (see :ref:`in <in_attr>` attribute)
