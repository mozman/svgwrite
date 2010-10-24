:class:`Presentation` mixin
===========================

.. autoclass:: svgwrite.mixins.Presentation

Methods
-------

.. automethod:: svgwrite.mixins.Presentation.fill(color=None, rule=None, opacity=None)

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#FillProperty
   * http://www.w3.org/TR/SVG11/painting.html#FillRuleProperty
   * http://www.w3.org/TR/SVG11/painting.html#FillOpacityProperty

.. automethod:: svgwrite.mixins.Presentation.stroke(color=None, width=None, opacity=None, linecap=None, linejoin=None, miterlimit=None)

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#StrokeProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeWidthProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeOpacityProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeLinecapProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeMiterlimitProperty

.. automethod:: svgwrite.mixins.Presentation.dasharray(dasharray=None, offset=None)

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#StrokeDasharrayProperty
   * http://www.w3.org/TR/SVG11/painting.html#StrokeDashoffsetProperty

:class:`MediaGroup` mixin
=========================

.. autoclass:: svgwrite.mixins.MediaGroup

   SVG Tiny 1.2

   valid for SVG Elements: animation, audio, desc, image, metadata, title, video

Methods
-------

.. automethod:: svgwrite.mixins.MediaGroup.viewport_fill(color=None, opacity=None)

.. seealso::

   * http://www.w3.org/TR/SVGMobile12/painting.html#viewport-fill-property
   * http://www.w3.org/TR/SVGMobile12/painting.html#viewport-fill-opacity-property

:class:`Markers` mixin
======================

.. autoclass:: svgwrite.mixins.Markers

Methods
-------

.. automethod:: svgwrite.mixins.Markers.set_markers(markers)

.. seealso::

   * http://www.w3.org/TR/SVG11/painting.html#MarkerProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerStartProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerMidProperty
   * http://www.w3.org/TR/SVG11/painting.html#MarkerEndProperty