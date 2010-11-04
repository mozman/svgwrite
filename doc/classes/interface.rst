IViewBox interface
==================

.. autoclass:: svgwrite.interface.IViewBox

Methods
-------

.. automethod:: svgwrite.interface.IViewBox.viewbox

.. automethod:: svgwrite.interface.IViewBox.stretch

.. automethod:: svgwrite.interface.IViewBox.fit

ITransform interface
====================

.. autoclass:: svgwrite.interface.ITransform

Methods
-------

.. automethod:: svgwrite.interface.ITransform.translate

.. automethod:: svgwrite.interface.ITransform.rotate

.. automethod:: svgwrite.interface.ITransform.skewX

.. automethod:: svgwrite.interface.ITransform.skewY

.. automethod:: svgwrite.interface.ITransform.scale

IXLink interface
================

.. autoclass:: svgwrite.interface.IXLink

Methods
-------

.. automethod:: svgwrite.interface.IXLink.set_href

.. automethod:: svgwrite.interface.IXLink.set_xlink

Set **xlink:actuate** and **xlink:type** by the index operator::

    element['xlink:type'] = 'simple'
    element['xlink:actuate'] = 'onLoad'
