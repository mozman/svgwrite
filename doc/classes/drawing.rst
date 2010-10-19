:class:`Drawing` objects
========================

.. automodule:: svgwrite.drawing

.. autoclass:: svgwrite.drawing.Drawing

.. automethod:: svgwrite.drawing.Drawing.__init__([filename="noname.svg", size=('100%', '100%'), **extra])

Attributes
----------

.. attribute:: Drawing.filename

   `string` should be valid for :func:`open`.

Inherited Attributes
--------------------

.. attribute:: Drawing.attribs

   *dict* of SVG attributes

.. attribute:: Drawing.elements

   *list* of SVG subelements

.. attribute:: Drawing.defs

   *Defs* container for referenced SVG elements

Methods
-------

.. automethod:: svgwrite.drawing.Drawing.write(fileobj)

.. automethod:: svgwrite.drawing.Drawing.save()

.. automethod:: svgwrite.drawing.Drawing.saveas(filename)

.. automethod:: svgwrite.drawing.Drawing.add_stylesheet(href, title, alternate, media)

.. automethod:: svgwrite.drawing.Drawing.get_xml()

Inherited Methods
-----------------

.. automethod:: svgwrite.drawing.Drawing.add(element)

.. automethod:: svgwrite.drawing.Drawing.tostring()

Supported Interfaces
--------------------

:class:`~svgwrite.interface.IViewBox`
