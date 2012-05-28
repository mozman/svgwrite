Script
======

The *script* element indicate links to a client-side language.

.. autoclass:: svgwrite.container.Script

.. seealso:: http://www.w3.org/TR/SVG/script.html

.. automethod:: svgwrite.container.Script.__init__

.. automethod:: svgwrite.container.Script.append

Best place for the *script* element is the *defs* attribute of the
:class:`~svgwrite.drawing.Drawing` class::

    drawing.defs.add(drawing.script('script-content'))

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`

SVG Attributes
--------------

* **type** -- `string`

  Identifies the scripting language for the given *script* element. The value
  content-type specifies a media type, per MIME. If a *type* is not provided,
  the value of **contentScriptType** on the **svg** element shall be used,
  which in turn defaults to ``'application/ecmascript'``. If a *script* element
  falls outside of the outermost svg element and the *type* is not provided,
  the *type* must default to ``'application/ecmascript'``

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **xlink:href** -- `string` -- **href** parameter

* **xlink:show** -- ``'new|replace'``

* **xlink:acuate** -- ``'onRequest'``

  This attribute provides documentation to XLink-aware processors that an
  application should traverse from the starting resource to the ending
  resource only on a post-loading event triggered for the purpose of traversal.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
