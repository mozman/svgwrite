:class:`Image` objects --- <image>
==================================

.. autoclass:: svgwrite.image.Image

Methods
-------

.. automethod:: svgwrite.image.Image.__init__(href ,[insert=None, size=None, attribs=None, \*\*extra])

.. automethod:: svgwrite.image.Image.stretch()

.. automethod:: svgwrite.image.Image.fit([horiz="center", vert="middle", scale="meet"])

Inherited Attributes
--------------------

.. attribute:: Image.attribs

   *dict* of SVG attributes

.. attribute:: Image.elements

   *list* of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.image.Image.add(element)

.. automethod:: svgwrite.image.Image.tostring()

.. automethod:: svgwrite.image.Image.get_xml()

Supported Interfaces
--------------------

:class:`svgwrite.interface.ITransform`
    :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
    :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

SVG Attributes
--------------

* **class** -- *<string>* assigns one or more css-class-names to an element
* **style** -- *<string>* allows per-element css-style rules to be specified
  directly on a given element
* **x** -- *<coordinate>* insert x-coordinate, insert[0] parameter at
  :meth:`__init__`, default=0
* **y** -- *<coordinate>* insert y-coordinate, insert[1] parameter at
  :meth:`__init__`, default=0
* **width** -- *<length>* width - size[0] parameter at :meth:`__init__`
* **height** -- *<length>* height - size[1] parameter at :meth:`__init__`
* **transform** -- :class:`svgwrite.interface.ITransform` interface
* **xlink:href** -- *<string>* hyperlink to the image resource,
  href parameter at :meth:`__init__`
* **externalResourcesRequired** -- *<bool>* *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
