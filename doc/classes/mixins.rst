ViewBox Mixin
=============

.. autoclass:: svgwrite.mixins.ViewBox

.. automethod:: svgwrite.mixins.ViewBox.viewbox

.. automethod:: svgwrite.mixins.ViewBox.stretch

.. automethod:: svgwrite.mixins.ViewBox.fit

Transform Mixin
===============

.. autoclass:: svgwrite.mixins.Transform

.. automethod:: svgwrite.mixins.Transform.translate

.. automethod:: svgwrite.mixins.Transform.rotate

.. automethod:: svgwrite.mixins.Transform.skewX

.. automethod:: svgwrite.mixins.Transform.skewY

.. automethod:: svgwrite.mixins.Transform.scale

XLink Mixin
===========

.. autoclass:: svgwrite.mixins.XLink

.. automethod:: svgwrite.mixins.XLink.set_href

.. automethod:: svgwrite.mixins.XLink.set_xlink

Set **xlink:actuate** and **xlink:type** by the index operator::

    element['xlink:type'] = 'simple'
    element['xlink:actuate'] = 'onLoad'

Presentation Mixin
==================

.. autoclass:: svgwrite.mixins.Presentation

.. automethod:: svgwrite.mixins.Presentation.fill

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#FillProperty
   * http://www.w3.org/TR/SVG11/painting.html#FillRuleProperty
   * http://www.w3.org/TR/SVG11/painting.html#FillOpacityProperty

.. automethod:: svgwrite.mixins.Presentation.stroke

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#StrokeProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeWidthProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeOpacityProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeLinecapProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeMiterlimitProperty

.. automethod:: svgwrite.mixins.Presentation.dasharray

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#StrokeDasharrayProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeDashoffsetProperty

MediaGroup Mixin
================

   SVG Tiny 1.2

   valid for SVG Elements: animation, audio, desc, image, metadata, title, video

.. autoclass:: svgwrite.mixins.MediaGroup

.. automethod:: svgwrite.mixins.MediaGroup.viewport_fill

.. seealso::

   * http://www.w3.org/TR/SVGMobile12/painting.html#viewport-fill-property
   * http://www.w3.org/TR/SVGMobile12/painting.html#viewport-fill-opacity-property

Markers Mixin
=============

.. autoclass:: svgwrite.mixins.Markers

.. automethod:: svgwrite.mixins.Markers.set_markers

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#MarkerProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerStartProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerMidProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerEndProperty

Clipping Mixin
==============

.. autoclass:: svgwrite.mixins.Clipping

.. automethod:: svgwrite.mixins.Clipping.clip_rect

.. seealso:: http://www.w3.org/TR/SVG11/masking.html#OverflowAndClipProperties
