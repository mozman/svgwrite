Style
=====

Internal Stylesheets

.. autoclass:: svgwrite.container.Style

.. seealso:: http://www.w3.org/TR/SVG/styling.html#StyleElement

.. automethod:: svgwrite.container.Style.__init__

.. automethod:: svgwrite.container.Style.append

Best place for the *style* element is the *defs* attribute of the
:class:`~svgwrite.drawing.Drawing` class::

    drawing.defs.add(drawing.style('stylesheet-content'))

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`

SVG Attributes
--------------

* **type** -- `string`

  default is ``'text/css'``

* **title** -- `string`

  (For compatibility with HTML 4.) This attribute specifies an advisory
  title for the ‘style’ element.

* **media** -- `string`

  This attribute specifies the intended destination medium for style information.
  It may be a single media descriptor or a comma-separated list.
  The default value for this attribute is ``'all'``.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
