.. _feDistantLight:

feDistantLight Filter Element
=============================

The light source **feDistantLight** is a child element of the filter primitives
:ref:`feDiffuseLighting <feDiffuseLighting>` or :ref:`feSpecularLighting <feDiffuseLighting>`,
create and add this object with the method :meth:`feDistantLight`
of the filter primitives **feDiffuseLighting** or **feSpecularLighting**.

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feDistantLightElement

SVG Attributes
--------------

* **azimuth** -- `<number>`

    Direction angle for the light source on the XY plane (clockwise), in degrees.

    Default is ``'0'``

* **elevation** -- `<number>`

    Direction angle for the light source on the YZ plane, in degrees.

    Default is ``'0'``

.. _fePointLight:

fePointLight Filter Element
===========================

The light source **fePointLight** is a child element of the filter primitives
:ref:`feDiffuseLighting <feDiffuseLighting>` or :ref:`feSpecularLighting <feDiffuseLighting>`,
create and add this object with the method :meth:`fePointLight`
of the filter primitives **feDiffuseLighting** or **feSpecularLighting**.

The light source **feDistantLight** is a child element of the filter primitives
**feDiffuseLighting** or **feSpecularLighting**.

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#fePointLightElement

SVG Attributes
--------------

* **x** -- `<number>` -- **source** parameter

    X location for the light source in the coordinate system established by
    attribute **primitiveUnits** on the **filter** element.

    Default is ``'0'``

* **y** -- `<number>` -- **source** parameter
    Y location for the light source in the coordinate system established by
    attribute **primitiveUnits** on the **filter** element.

    Default is ``'0'``

* **z** -- `<number>`-- **source** parameter

    Z location for the light source in the coordinate system established by
    attribute **primitiveUnits** on the ‘filter’ element, assuming that, in the
    initial coordinate system, the positive Z-axis comes out towards the person
    viewing the content and assuming that one unit along the Z-axis equals one
    unit in X and Y.

    Default is ``'0'``


.. _feSpotLight:

feSpotLight Filter Element
==========================

The light source **feSpotLight** is a child element of the filter primitives
:ref:`feDiffuseLighting <feDiffuseLighting>` or :ref:`feSpecularLighting <feDiffuseLighting>`,
create and add this object with the method :meth:`feSpotLight`
of the filter primitives **feDiffuseLighting** or **feSpecularLighting**.

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feSpotLightElement

SVG Attributes
--------------

* **x**, **y**, **z** -- see :ref:`fePointLight`

* **pointsAtX** -- `<number>` -- **target** parameter

    X location in the coordinate system established by attribute
    **primitiveUnits** on the **filter** element of the point at which the
    light source is pointing.

    Default is ``'0'``

* **pointsAtY** -- `<number>` -- **target** parameter

    Y location in the coordinate system established by attribute
    **primitiveUnits** on the **filter** element of the point at which the
    light source is pointing.

    Default is ``'0'``

* **pointsAtZ** -- `<number>` -- **target** parameter

    Z location in the coordinate system established by attribute
    **primitiveUnits** on the **filter** element of the point at which the light
    source is pointing, assuming that, in the initial coordinate system, the
    positive Z-axis comes out towards the person viewing the content and
    assuming that one unit along the Z-axis equals one unit in X and Y.

    Default is ``'0'``

* **specularExponent** -- `<number>`

    Exponent value controlling the focus for the light source.

    Default is ``'1'``

* **limitingConeAngle** -- `<number>`

    A limiting cone which restricts the region where the light is projected. No
    light is projected outside the cone. **limitingConeAngle** represents the
    angle in degrees between the spot light axis (i.e. the axis between the
    light source and the point to which it is pointing at) and the spot light
    cone. User agents should apply a smoothing technique such as anti-aliasing
    at the boundary of the cone.

    If no value is specified, then no limiting cone will be applied.
