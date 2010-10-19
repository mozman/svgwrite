:class:`Defs` objects --- <defs>
================================

.. autoclass:: svgwrite.container.Defs

Inherited Attributes
--------------------

.. attribute:: Defs.attribs

   `dict` of SVG attributes

.. attribute:: Defs.elements

   `list` of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.Defs.add(element)

.. automethod:: svgwrite.container.Defs.tostring()

.. automethod:: svgwrite.container.Defs.get_xml()

Supported Interfaces
--------------------

:class:`svgwrite.interface.ITransform`
    :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
    :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

SVG attributes
--------------

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*
* **transform** -- use :class:`svgwrite.interface.ITransform` interface

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`