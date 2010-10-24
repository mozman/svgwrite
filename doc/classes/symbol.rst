:class:`Symbol` objects --- <symbol>
====================================

.. autoclass:: svgwrite.container.Symbol

Inherited Attributes
--------------------

.. attribute:: Symbol.attribs

   `dict` of SVG attributes

.. attribute:: Symbol.elements

   `list` of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.Symbol.add(element)

.. automethod:: svgwrite.container.Symbol.tostring()

.. automethod:: svgwrite.container.Symbol.get_xml()

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

  .. seealso:: http://www.w3.org/TR/SVG11/struct.html#SymbolElement

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*
* **viewBox** -- use :class:`svgwrite.interface.IViewBox` interface
* **preserveAspectRatio** -- use :class:`svgwrite.interface.IViewBox`
  interface

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
