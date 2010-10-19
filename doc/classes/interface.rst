:class:`IViewBox` interface
===========================

.. autoclass:: svgwrite.interface.IViewBox

Methods
-------

.. automethod:: svgwrite.interface.IViewBox.viewbox([minx=0, miny=0, width=0, height=0])

.. automethod:: svgwrite.interface.IViewBox.stretch()

.. automethod:: svgwrite.interface.IViewBox.fit([horiz="center", vert="middle", scale="meet"])

:class:`ITransform` interface
=============================

.. autoclass:: svgwrite.interface.ITransform

Methods
-------

.. automethod:: svgwrite.interface.ITransform.translate(tx, [ty=None])

.. automethod:: svgwrite.interface.ITransform.rotate(angle, [center=None])

.. automethod:: svgwrite.interface.ITransform.skewX(angle)

.. automethod:: svgwrite.interface.ITransform.skewY(angle)

.. automethod:: svgwrite.interface.ITransform.scale(sx, [sy=None])

:class:`IXLink` interface
=========================

.. autoclass:: svgwrite.interface.IXLink

Methods
-------

.. automethod:: svgwrite.interface.IXLink.set_href(element)
