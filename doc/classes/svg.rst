SVG
===

.. autoclass:: svgwrite.container.SVG

.. seealso:: http://www.w3.org/TR/SVG11/struct.html#SVGElement

.. automethod:: svgwrite.container.SVG.__init__
.. automethod:: svgwrite.container.SVG.embed_stylesheet
.. automethod:: svgwrite.container.SVG.embed_font
.. automethod:: svgwrite.container.SVG.embed_google_web_font

Attributes
----------

.. attribute:: SVG.defs

   `Defs` container for referenced elements

   adding SVG elements to *defs*::

     svgobject.defs.add(element)


Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.container.Symbol`
* :class:`svgwrite.container.SVG`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.ViewBox`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given
  element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **transform** -- use :class:`svgwrite.mixins.Transform` interface

* **x** -- `<coordinate>` -- **insert** parameter

  (Has no meaning or effect on :class:`~svgwrite.drawing.Drawing` .)

  The x-axis coordinate of one corner of the rectangular region into which an
  embedded **svg** element is placed.

  Default is ``'0'``.

* **y** -- `<coordinate>` -- **insert** parameter

  (Has no meaning or effect on :class:`~svgwrite.drawing.Drawing` .)

  The y-axis coordinate of one corner of the rectangular region into which an
  embedded **svg** element is placed.

  Default is ``'0'``.

* **width** -- `<length>` -- **size** parameter

  For outermost **svg** elements (:class:`~svgwrite.drawing.Drawing`), the
  intrinsic width of the SVG document fragment. For embedded **svg** elements,
  the width of the rectangular region into which the **svg** element is placed.

  A negative value is an error. A value of zero disables rendering of the element.

  Default is ``'100%'``.

* **height** -- `<length>` -- **size** parameter

  For outermost **svg** elements (:class:`~svgwrite.drawing.Drawing`), the
  intrinsic height of the SVG document fragment. For embedded **svg** elements,
  the height of the rectangular region into which the **svg** element is placed.

  A negative value is an error. A value of zero disables rendering of the element.

  Default is ``'100%'``.

* **viewBox** -- :class:`svgwrite.mixins.ViewBox` interface

* **preserveAspectRatio**  -- :class:`svgwrite.mixins.ViewBox` interface

* **zoomAndPan** -- ``'disable | magnify'``

  Default is ``'magnify'``.

.. note::
   do not set or change following SVG attributes:
   version, baseProfile, contentScriptType, contentStyleType

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Document Event Attributes </attributes/document_event>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
