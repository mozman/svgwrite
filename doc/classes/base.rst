:mod:`base` modul
=================

.. automodule:: svgwrite.base

:class:`BaseElement` objects
----------------------------

.. autoclass:: svgwrite.base.BaseElement

Attributes
~~~~~~~~~~

.. attribute:: BaseElement.attribs

   `dict` of SVG attributes

.. attribute:: BaseElement.elements

   `list` of SVG subelements

Methods
~~~~~~~

.. automethod:: BaseElement.add(element)

.. automethod:: BaseElement.tostring()

.. automethod:: BaseElement.get_xml()

.. automethod:: BaseElement.__getitem__(key)

.. automethod:: BaseElement.__setitem__(key, value)

.. _Common-SVG-Attributs:

Common SVG Attributes
---------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Document Event Attributes </attributes/document_event>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
