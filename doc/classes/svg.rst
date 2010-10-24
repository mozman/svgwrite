:class:`SVG` objects --- <svg>
==============================

.. autoclass:: svgwrite.container.SVG

.. automethod:: svgwrite.container.SVG.__init__([insert=None, size=None, attribs=None, \*\*extra])

Attributes
----------

.. attribute:: SVG.defs

   `Defs` container for referenced elements

   adding SVG elements to *defs*::

     svgobject.defs.add(element)

Inherited Attributes
--------------------

.. attribute:: SVG.attribs

   `dict` of SVG attributes

.. attribute:: SVG.elements

   `list` of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.SVG.add(element)

.. automethod:: svgwrite.container.SVG.tostring()

.. automethod:: svgwrite.container.SVG.get_xml()

Supported Interfaces
--------------------

:class:`svgwrite.interface.IViewBox`
    :meth:`viewbox`, :meth:`stretch`, :meth:`fit`

Used Mixins
-----------

:class:`svgwrite.mixins.Presentation`

    :meth:`fill`, :meth:`stroke`, :meth:`dasharray`


SVG Attributes
--------------

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **x** -- `coordinate` x-coordinate, if <svg> is enbedded into another
  <svg>-element
* **y** -- `coordinate` y-coordinate, if <svg> is enbedded into another
  <svg>-element
* **width** -- `length` canvas-width - default is '100%'
* **height** -- `length` canvas-height - default is '100%'
* **viewBox** -- :class:`svgwrite.interface.IViewBox` interface
* **preserveAspectRatio**  -- :class:`svgwrite.interface.IViewBox` interface
* **zoomAndPan** -- ``"disable"|"magnify"`` : default is ``"magnify"``
* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*

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
