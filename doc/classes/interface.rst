ViewBox Mixin
=============

.. autoclass:: svgwrite.mixins.ViewBox

Methods
-------

.. automethod:: svgwrite.mixins.ViewBox.viewbox

.. automethod:: svgwrite.mixins.ViewBox.stretch

.. automethod:: svgwrite.mixins.ViewBox.fit

Transform Mixin
===============

.. autoclass:: svgwrite.mixins.Transform

Methods
-------

.. automethod:: svgwrite.mixins.Transform.translate

.. automethod:: svgwrite.mixins.Transform.rotate

.. automethod:: svgwrite.mixins.Transform.skewX

.. automethod:: svgwrite.mixins.Transform.skewY

.. automethod:: svgwrite.mixins.Transform.scale

XLink Mixin
===========

.. autoclass:: svgwrite.mixins.XLink

Methods
-------

.. automethod:: svgwrite.mixins.XLink.set_href

.. automethod:: svgwrite.mixins.XLink.set_xlink

Set **xlink:actuate** and **xlink:type** by the index operator::

    element['xlink:type'] = 'simple'
    element['xlink:actuate'] = 'onLoad'
