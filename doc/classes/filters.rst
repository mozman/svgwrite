Introduction
============

This chapter describes SVG's declarative filter effects feature set, which
when combined with the 2D power of SVG can describe much of the common
artwork on the Web in such a way that client-side generation and alteration
can be performed easily. In addition, the ability to apply filter effects to
SVG graphics elements and container elements helps to maintain the semantic
structure of the document, instead of resorting to images which aside from
generally being a fixed resolution tend to obscure the original semantics
of the elements they replace. This is especially true for effects applied to
text.

Filter effects are defined by **filter** elements. To apply a filter effect
to a **graphics element** or a **container element**, you set the value of
the **filter** property on the given element such that it references the
filter effect.

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#Introduction

Filter Element
==============

.. autoclass:: svgwrite.filters.Filter

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#FilterElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.mixins.Presentation`

Methods
-------

.. automethod:: svgwrite.filters.Filter.__init__

.. method:: Filter.feBlend(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feBlend`

.. method:: Filter.feColorMatrix(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feColorMatrix`

.. method:: Filter.feComponentTransfer(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feComponentTransfer`

.. method:: Filter.feComposite(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feComposite`

.. method:: Filter.feConvolveMatrix(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feConvolveMatrix`

.. method:: Filter.feDiffuseLighting(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feDiffuseLighting`

.. method:: Filter.feDisplacementMap(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feDisplacementMap`

.. method:: Filter.feFlood(start=None, size=None, \*\*extra)

   create and add a :ref:`feFlood`

.. method:: Filter.feGaussianBlur(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feGaussianBlur`

.. method:: Filter.feImage(href, start=None, size=None, \*\*extra)

   create and add a :ref:`feImage`

.. method:: Filter.feMerge(start=None, size=None, \*\*extra)

   create and add a :ref:`feMerge`

.. method:: Filter.feMorphology(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feMorphology`

.. method:: Filter.feOffset(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feOffset`

.. method:: Filter.feSpecularLighting(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feSpecularLighting`

.. method:: Filter.feTile(in_, start=None, size=None, \*\*extra)

   create and add a :ref:`feTile`

.. method:: Filter.feTurbulence(start=None, size=None, \*\*extra)

   create and add a :ref:`feTurbulence`

SVG Attributes
--------------

* **filterUnits** -- ``'userSpaceOnUse | objectBoundingBox'``

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **primitiveUnits** -- ``'userSpaceOnUse | objectBoundingBox'``
  Specifies the coordinate system for the various length values within the
  filter primitives and for the attributes that define the filter primitive
  subregion.

  If **primitiveUnits** = ``'userSpaceOnUse'``, any length values within the
  filter definitions represent values in the current user coordinate system
  in place at the time when the **filter** element is referenced (i.e., the
  user coordinate system for the element referencing the **filter** element
  via a **filter** property).

  If **primitiveUnits** = ``'objectBoundingBox'``, then any length values
  within the filter definitions represent fractions or percentages of the
  bounding box on the referencing element (see Object bounding box units).
  Note that if only one number was specified in a `<number-optional-number>`
  value this number is expanded out before the **primitiveUnits** computation
  takes place.

  If attribute **primitiveUnits** is not specified, then the effect is as if
  a value of ``'userSpaceOnUse'`` were specified.

* **x** -- `<coordinate>` -- **start** parameter

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **y** -- `<coordinate>` -- **start** parameter

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **width** -- `<length>` -- **size** parameter

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **height** -- `<length>` -- **size** parameter

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **filterRes** -- `<number-optional-number>` -- **resolution** parameter

  See `Filter effects region. <http://www.w3.org/TR/SVG11/filters.html#FilterEffectsRegion>`_

* **xlink:href** -- `<iri>` -- **inherit** parameter

  A IRI reference to another **filter** element within the current SVG document
  fragment. Any attributes which are defined on the referenced **filter** element
  which are not defined on this element are inherited by this element.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Presentation Attributes </attributes/presentation>`
* :doc:`XLink Attributes </attributes/xlink>`

Example
-------

Source: https://secure.wikimedia.org/wikibooks/de/wiki/SVG/_Effekte#Urfilter_fePointLight.2C_Punktlichtquelle

.. literalinclude:: ../../examples/fePointLight.py
   :lines: 8-

and the XML result (with manual reformatting):

.. code-block:: xml

  <?xml version="1.0" encoding="utf-8" ?>
  <svg baseProfile="full" height="100%" version="1.1" width="100%"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:ev="http://www.w3.org/2001/xml-events"
    xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
          <filter id="DL" filterUnits="userSpaceOnUse"
            x="0" y="0" width="500" height="500" >
              <feDiffuseLighting diffuseConstant="1"
                x="0" y="0" width="500" height="500"
                in="SourceGraphic"
                kernelUnitLength="1"
                lighting-color="#f8f"
                surfaceScale="10">
                  <fePointLight x="500" y="250" z="250">
                      <animate attributeName="x"
                        dur="30s"
                        repeatDur="indefinite"
                        values="0;100;500;100;0" />
                      <animate attributeName="y"
                        dur="31s"
                        repeatDur="indefinite"
                        values="0;500;400;-100;0" />
                      <animate attributeName="z"
                        dur="37s"
                        repeatDur="indefinite"
                        values="0;1000;500;-100;0" />
                  </fePointLight>
              </feDiffuseLighting>
          </filter>
      </defs>
  </svg>