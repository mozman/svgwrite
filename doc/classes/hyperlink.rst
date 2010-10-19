:class:`Hyperlink` objects --- <a>
==================================

.. autoclass:: svgwrite.container.Hyperlink

.. automethod:: svgwrite.container.Hyperlink.__init__(href, [target='_blank', attribs=None, \*\*extra])

Inherited Attributes
--------------------

.. attribute:: Hyperlink.attribs

   *dict* of SVG attributes

.. attribute:: Hyperlink.elements

   *list* of SVG subelements

Inherited Methods
-----------------

.. automethod:: svgwrite.container.Hyperlink.add(element)

.. automethod:: svgwrite.container.Hyperlink.tostring()

.. automethod:: svgwrite.container.Hyperlink.get_xml()

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
* **transform** -- :class:`svgwrite.interface.ITransform` interface
* **xlink:href** -- `string` set on :meth:`__init__`
* **xlink:show** -- ``'new|replace'`` use the **target** attribute
* **xlink:acuate** -- `string` ``'onRequest'`` This attribute provides
  documentation to XLink-aware processors that an application should
  traverse from the starting resource to the ending resource only on a
  post-loading event triggered for the purpose of traversal.
* **target** -- `string` This attribute specifies the name or portion of
  the target window, frame, pane, tab, or other relevant presentation
  context (e.g., an HTML or XHTML frame, iframe, or object element)
  into which a document is to be opened when the link is activated.

  - ``_replace``: The current SVG image is replaced by the linked
    content in the same rectangular area in the same frame as the
    current SVG image.
  - ``_self``: The current SVG image is replaced by the linked content
     in the same frame as the current SVG image. This is the lacuna
     value, if the target attribute is not specified.
  - ``_parent``: The immediate frameset parent of the SVG image is
    replaced by the linked content.
  - ``_top``: The content of the full window or tab, including any
    frames, is replaced by the linked content
  - ``_blank``: A new un-named window or tab is requested for the
    display of the linked content. If this fails, the result is the
    same as ``_top``
  - ``<XML-Name>``: Specifies the name of the frame, pane, or other
    relevant presentation context for display of the linked content.
    If this already exists, it is re-used, replacing the existing
    content. If it does not exist, it is created (the same as ``_blank``,
    except that it now has a name).

* **externalResourcesRequired** -- `bool` *False*: if document rendering
  can proceed even if external resources are unavailable else: *True*

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`
