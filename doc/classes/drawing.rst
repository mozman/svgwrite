Drawing
=======

.. automodule:: svgwrite.drawing

.. autoclass:: svgwrite.drawing.Drawing

.. automethod:: svgwrite.drawing.Drawing.__init__

Attributes
----------

.. attribute:: Drawing.filename

   `string` should be valid for :func:`open`.

.. attribute:: Drawing.defs

   SVG defs section - as :class:`~svgwrite.container.Defs` object.

Methods
-------

.. automethod:: svgwrite.drawing.Drawing.add

.. automethod:: svgwrite.drawing.Drawing.write

.. automethod:: svgwrite.drawing.Drawing.save

.. automethod:: svgwrite.drawing.Drawing.saveas

.. automethod:: svgwrite.drawing.Drawing.add_stylesheet

.. automethod:: svgwrite.drawing.Drawing.get_xml

.. method:: Drawing.tostring()

   Get the XML representation as unicode `string`. If you embed the SVG object
   into a XHTML page, you have to link to the CSS files (if you use CSS classes)
   in the header section of the surrounding XHTML page.

   :return: unicode XML string of this object and all its subelements

Factory Methods
---------------

.. method:: Drawing.line(start=(0, 0), end=(0, 0), \*\*extra)

   Create a :class:`svgwrite.shapes.Line` object.

.. method:: Drawing.rect(insert=(0, 0), size=(1, 1), rx=None, ry=None, \*\*extra)

   Create a :class:`svgwrite.shapes.Rect` object.

.. method:: Drawing.circle(center=(0, 0), r=1, \*\*extra)

   Create a :class:`svgwrite.shapes.Circle` object.

.. method:: Drawing.ellipse(center=(0, 0), r=(1, 1), \*\*extra)

   Create a :class:`svgwrite.shapes.Ellipse` object.

.. method:: Drawing.polyline(points=[], \*\*extra)

   Create a :class:`svgwrite.shapes.Polyline` object.

.. method:: Drawing.polygon(points=[], \*\*extra)

   Create a :class:`svgwrite.shapes.Polygon` object.

.. method:: Drawing.text(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], \*\*extra)

   Create a :class:`svgwrite.text.Text` object.

.. method:: Drawing.tspan(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], \*\*extra)

   Create a :class:`svgwrite.text.TSpan` object.

.. method:: Drawing.tref(element, \*\*extra)

   Create a :class:`svgwrite.text.TRef` object.

.. method:: Drawing.textPath(path, text, startOffset=None, method='align', spacing='exact', \*\*extra)

   Create a :class:`svgwrite.text.TextPath` object.

.. method:: Drawing.textArea(text=None, insert=None, size=None, \*\*extra)

   Create a :class:`svgwrite.text.TextArea` object.

.. method:: Drawing.path(d=None, \*\*extra)

   Create a :class:`svgwrite.path.Path` object.

.. method:: Drawing.image(href, insert=None, size=None, \*\*extra)

   Create a :class:`svgwrite.image.Image` object.

.. method:: Drawing.g(\*\*extra)

   Create a :class:`svgwrite.container.Group` object.

.. method:: Drawing.symbol(\*\*extra)

   Create a :class:`svgwrite.container.Symbol` object.

.. method:: Drawing.svg(insert=None, size=None, \*\*extra)

   Create a :class:`svgwrite.container.SVG` object.

.. method:: Drawing.use(href, insert=None, size=None, \*\*extra)

   Create a :class:`svgwrite.container.Use` object.

.. method:: Drawing.a(href, target='_blank', \*\*extra)

   Create a :class:`svgwrite.container.Hyperlink` object.

.. method:: Drawing.marker(insert=None, size=None, orient=None, \*\*extra)

   Create a :class:`svgwrite.container.Marker` object.

.. method:: Drawing.script(href=None, content='', \*\*extra)

   Create a :class:`svgwrite.container.Script` object.

.. method:: Drawing.style(content='', \*\*extra)

   Create a :class:`svgwrite.container.Style` object.

.. method:: Drawing.linearGradient(start=None, end=None, inherit=None, \*\*extra)

   Create a :class:`svgwrite.gradients.LinearGradient` object.

.. method:: Drawing.radialGradient(center=None, r=None, focal=None, inherit=None, \*\*extra)

   Create a :class:`svgwrite.gradients.RadialGradient` object.

.. method:: Drawing.mask(start=None, size=None, \*\*extra)

   Create a :class:`svgwrite.masking.Mask` object.

.. method:: Drawing.clipPath(\*\*extra)

   Create a :class:`svgwrite.masking.ClipPath` object.

.. method:: Drawing.set(element=None, \*\*extra)

   Create a :class:`svgwrite.animate.Set` object.

.. method:: Drawing.animate(element=None, \*\*extra)

   Create a :class:`svgwrite.animate.Animate` object.

.. method:: Drawing.animateColor(element=None, \*\*extra)

   Create a :class:`svgwrite.animate.AnimateColor` object.

.. method:: Drawing.animateMotion(element=None, \*\*extra)

   Create a :class:`svgwrite.animate.AnimateMotion` object.

.. method:: Drawing.animateTransform(transform, element=None, \*\*extra)

   Create a :class:`svgwrite.animate.AnimateTransform` object.

.. method:: Drawing.filter(start=None, size=None, resolution=None, inherit=None, \*\*extra)

   Create a :class:`svgwrite.filters.Filter` object. (Filter Primitives are created
   by **factory-methods** of the class **Filter**)

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.container.Symbol`
* :class:`svgwrite.container.SVG`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.ViewBox`
* :class:`svgwrite.mixins.Presentation`
* :class:`svgwrite.mixins.Clipping`
* :class:`svgwrite.elementfactory.ElementFactory`
