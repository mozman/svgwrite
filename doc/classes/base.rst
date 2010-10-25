:class:`BaseElement` objects
============================

.. autoclass:: svgwrite.base.BaseElement

.. automethod:: svgwrite.base.BaseElement.__init__([attribs=None, **extra])

Attributes
----------

.. attribute:: BaseElement.attribs

   *dict* of SVG attributes

.. attribute:: BaseElement.elements

   *list* of SVG subelements

Methods
-------

.. automethod:: svgwrite.base.BaseElement.add(element)

.. automethod:: svgwrite.base.BaseElement.tostring()

.. automethod:: svgwrite.base.BaseElement.get_xml()

.. automethod:: svgwrite.base.BaseElement.get_funciri()

.. automethod:: svgwrite.base.BaseElement.__getitem__(key)

.. automethod:: svgwrite.base.BaseElement.__setitem__(key, value)

set/get SVG attributes::

    element['attribute'] = value
    value = element['attribute']

Common SVG Attributes
---------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Document Event Attributes </attributes/document_event>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
