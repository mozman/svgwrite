:class:`Line` objects --- <line>
================================

.. autoclass:: svgwrite.shapes.Line

:class:`Rect` objects --- <rect>
================================

.. autoclass:: svgwrite.shapes.Rect

:class:`Circle` objects --- <circle>
====================================

.. autoclass:: svgwrite.shapes.Circle

:class:`Ellipse` objects --- <ellipse>
======================================

.. autoclass:: svgwrite.shapes.Ellipse

:class:`Polyline` objects --- <polyline>
========================================

.. autoclass:: svgwrite.shapes.Polyline

:class:`Polygon` objects --- <polygon>
======================================

.. autoclass:: svgwrite.shapes.Polygon

Common for: Line, Rect, Circle, Ellipse, Polyline, Polygon
----------------------------------------------------------

Inherited Attributes
~~~~~~~~~~~~~~~~~~~~

.. attribute:: Polygon.attribs

   *dict* of SVG attributes

.. attribute:: Polygon.elements

   *list* of SVG subelements

Inherited Methods
~~~~~~~~~~~~~~~~~

.. automethod:: svgwrite.base.BaseElement.add(element)
   :noindex:

.. automethod:: svgwrite.base.BaseElement.tostring()
   :noindex:

.. automethod:: svgwrite.base.BaseElement.get_xml()
   :noindex:

Supported Interfaces
~~~~~~~~~~~~~~~~~~~~

:class:`svgwrite.interface.ITransform`
    :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
    :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

Supported SVG attributes
~~~~~~~~~~~~~~~~~~~~~~~~

* **class** -- `string` assigns one or more css-class-names to an element
* **style** -- `string` allows per-element css-style rules to be specified
  directly on a given element
* **externalResourcesRequired** -- `bool` *False*: if document rendering can
  proceed even if external resources are unavailable else: *True*
* **transform** -- use :class:`~svgwrite.interface.ITransform` interface

Standard SVG Attributes
~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`


for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`
