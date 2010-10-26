:class:`Use`
============

.. autoclass:: svgwrite.container.Use

.. automethod:: svgwrite.container.Use.__init__(href, [insert=None, size=None, attribs=None, \*\*extra])

Inherited Attributes
--------------------

.. attribute:: Use.attribs

   *dict* of SVG attributes

.. attribute:: Use.elements

   *list* of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.Use.add(element)

.. automethod:: svgwrite.container.Use.tostring()

.. automethod:: svgwrite.container.Use.get_xml()

Supported Interfaces
--------------------

:class:`svgwrite.interface.ITransform`
    :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
    :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

:class:`svgwrite.interface.IXLink`
    :meth:`set_href`

Used Mixins
-----------

:class:`svgwrite.mixins.Presentation`

    :meth:`fill`, :meth:`stroke`, :meth:`dasharray`

SVG Attributes
--------------

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **x** -- `coordinate` insert x-coordinate, set on __init__(insert)
* **y** -- `coordinate` insert y-coordinate, set on __init__(insert)
* **width** -- `length` width - default is ``'100%'``, set on __init__(size)
* **height** -- `length` height - default is ``'100%'``, set on __init__(size)
* **transform** -- :class:`svgwrite.interface.ITransform` interface
* **xlink:href** -- `string` set on __init__(href)
* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
