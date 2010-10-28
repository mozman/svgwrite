:class:`Drawing`
================

.. automodule:: svgwrite.drawing

.. autoclass:: svgwrite.drawing.Drawing

.. automethod:: svgwrite.drawing.Drawing.__init__([filename="noname.svg", size=('100%', '100%'), **extra])

Attributes
----------

.. attribute:: Drawing.filename

   `string` should be valid for :func:`open`.

Methods
-------

.. automethod:: svgwrite.drawing.Drawing.write(fileobj)

.. automethod:: svgwrite.drawing.Drawing.save()

.. automethod:: svgwrite.drawing.Drawing.saveas(filename)

.. automethod:: svgwrite.drawing.Drawing.add_stylesheet(href, title, alternate, media)

.. automethod:: svgwrite.drawing.Drawing.get_xml()

Factory Methods
---------------

.. method:: Drawing.line(start=(0, 0), end=(0, 0), attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Line` object.

.. method:: Drawing.rect(insert=(0, 0), size=(1, 1), rx=None, ry=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Rect` object.

.. method:: Drawing.circle(center=(0, 0), r=1, attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Circle` object.

.. method:: Drawing.ellipse(center=(0, 0), r=(1, 1), attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Ellipse` object.

.. method:: Drawing.polyline(points=[], attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Polyline` object.

.. method:: Drawing.polygon(points=[], attribs=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Polygon` object.

.. method:: Drawing.text(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, \*\*extra)

   Create a :class:`svgwrite.text.Text` object.

.. method:: Drawing.tspan(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, \*\*extra)

   Create a :class:`svgwrite.text.TSpan` object.

.. method:: Drawing.tref(element, attribs=None, \*\*extra)

   Create a :class:`svgwrite.text.TRef` object.

.. method:: Drawing.textPath(path, text, startOffset=None, method='align', spacing='exact', attribs=None, \*\*extra)

   Create a :class:`svgwrite.text.TextPath` object.

.. method:: Drawing.textArea(text=None, insert=None, size=None, attribs={}, \*\*extra)

   Create a :class:`svgwrite.text.TextArea` object.

.. method:: Drawing.path(d=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.path.Path` object.

.. method:: Drawing.image(href, insert=None, size=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.image.Image` object.

.. method:: Drawing.g(attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Group` object.

.. method:: Drawing.defs(attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Defs` object.

.. method:: Drawing.symbol(attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Symbol` object.

.. method:: Drawing.svg(insert=None, size=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.SVG` object.

.. method:: Drawing.use(href, insert=None, size=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Use` object.

.. method:: Drawing.a(href, target='_blank', attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Hyperlink` object.

.. method:: Drawing.marker(insert=None, size=None, orient=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.container.Marker` object.

.. method:: Drawing.linearGradient(start=None, end=None, inherit=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.gradients.LinearGradient` object.

.. method:: Drawing.radialGradient(center=None, r=None, focal=None, inherit=None, attribs=None, \*\*extra)

   Create a :class:`svgwrite.gradients.RadialGradient` object.

Inherited Attributes
--------------------

.. attribute:: Drawing.attribs

   *dict* of SVG attributes

.. attribute:: Drawing.elements

   *list* of SVG subelements

.. attribute:: Drawing.defs

   *Defs* container for referenced SVG elements

Inherited Methods
-----------------

.. automethod:: svgwrite.drawing.Drawing.add(element)

.. automethod:: svgwrite.drawing.Drawing.tostring()

Supported Interfaces
--------------------

:class:`~svgwrite.interface.IViewBox`
