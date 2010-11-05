animate module
==============

Because the Web is a dynamic medium, SVG supports the ability to change
vector graphics over time.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html

Set
===

.. autoclass:: svgwrite.animate.Set

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#SetElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`

Methods
-------

.. automethod:: svgwrite.animate.Set.__init__

.. method:: Animate.set_href(element)

  :param element: set target svg element to `element`

.. automethod:: svgwrite.animate.Animate.set_target

.. automethod:: svgwrite.animate.Animate.set_event

.. automethod:: svgwrite.animate.Animate.set_timing

.. automethod:: svgwrite.animate.Animate.freeze

SVG Animation Attributes
------------------------

* onbegin, onend, onrepeat, onload (:doc:`Animation Event Attributes </attributes/animation_events>`)
* attributeType, attributeName (:doc:`Animation Target Attributes </attributes/animation_target>`)
* begin, dur, end, min, max, restart, repeatCount, repeatDur, fill (:doc:`Animation Timing Attributes </attributes/animation_timing>`)

SVG Attributes
--------------

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **to** -- `<value>`
  Specifies the value for the attribute during the duration of the **set**
  element. The argument value must match the attribute type.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`XLink Attributes </attributes/xlink>`

AnimateMotion
=============

.. autoclass:: svgwrite.animate.AnimateMotion

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AnimateMotionElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.animate.Set`

Methods
-------

.. automethod:: svgwrite.animate.AnimateMotion.__init__

.. automethod:: svgwrite.animate.AnimateMotion.set_value

SVG Animation Attributes
------------------------

* onbegin, onend, onrepeat, onload (:doc:`Animation Event Attributes </attributes/animation_events>`)
* begin, dur, end, min, max, restart, repeatCount, repeatDur, fill (:doc:`Animation Timing Attributes </attributes/animation_timing>`)
* calcMode, values, keyTimes, keySplines, from, to, by (:doc:`Animation Value Attributes </attributes/animation_value>`)
* additive, accumulate (:doc:`Animation Addition Attributes </attributes/animation_addition>`)

SVG Attributes
--------------

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **calcMode** -- ``'discrete | linear | paced | spline'``

  Specifies the interpolation mode for the animation.

* **path** -- `<path-data>` -- **path** parameter

  The motion path, expressed in the same format and interpreted the same way
  as the :ref:`d <pathCommands>` attribute on the **Path** element.
  The effect of a motion path animation is to add a supplemental
  transformation matrix onto the CTM for the referenced object which causes a
  translation along the x- and y-axes of the current user coordinate system
  by the computed X and Y values computed over time.

* **keyPoints** -- `<list-of-numbers>`

  **keyPoints** takes a semicolon-separated list of floating point values
  between 0 and 1 and indicates how far along the motion path the object
  shall move at the moment in time specified by corresponding **keyTimes**
  value. Distance calculations use the user agent's distance along the path
  algorithm. Each progress value in the list corresponds to a value in the
  **keyTimes** attribute list.

  If a list of **keyPoints** is specified, there must be exactly as many
  values in the **keyPoints** list as in the **keyTimes** list.

  If there are any errors in the **keyPoints** specification (bad values,
  too many or too few values), then the document is in error.

* **rotate** -- `<number>` | ``'auto'`` | ``'auto-reverse'``

  The **rotate** attribute post-multiplies a supplemental transformation
  matrix onto the CTM of the target element to apply a rotation
  transformation about the origin of the current user coordinate system.
  The rotation transformation is applied after the supplemental translation
  transformation that is computed due to the **path** attribute.

  * ``'auto'``

    Indicates that the object is rotated over time by the angle of the
    direction (i.e., directional tangent vector) of the motion path.

  * ``'auto-reverse'``

    Indicates that the object is rotated over time by the angle of the
    direction (i.e., directional tangent vector) of the motion path plus
    180 degrees.

  * `<number>`

    Indicates that the target element has a constant rotation transformation
    applied to it, where the rotation angle is the specified number of
    degrees.

    Default value is ``'0'``.

* **origin** -- ``'default'``

  The **origin** attribute is defined in the
  `SMIL Animation specification <http://www.w3.org/TR/2001/REC-smil-animation-20010904/#MotionOriginAttribute>`_

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`XLink Attributes </attributes/xlink>`

Animate
=======

.. autoclass:: svgwrite.animate.Animate

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AnimateElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.animate.Set`

Methods
-------

.. automethod:: svgwrite.animate.Animate.__init__

.. automethod:: svgwrite.animate.Animate.set_value

SVG Animation Attributes
------------------------

* onbegin, onend, onrepeat, onload (:doc:`Animation Event Attributes </attributes/animation_events>`)
* attributeType, attributeName (:doc:`Animation Target Attributes </attributes/animation_target>`)
* begin, dur, end, min, max, restart, repeatCount, repeatDur, fill (:doc:`Animation Timing Attributes </attributes/animation_timing>`)
* calcMode, values, keyTimes, keySplines, from, to, by (:doc:`Animation Value Attributes </attributes/animation_value>`)
* additive, accumulate (:doc:`Animation Addition Attributes </attributes/animation_addition>`)

SVG Attributes
--------------

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`XLink Attributes </attributes/xlink>`

AnimateColor
============

.. autoclass:: svgwrite.animate.AnimateColor

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AnimateColorElement

The **from**, **by** and **to** attributes take color values, where each
color value is expressed using the following syntax (the same syntax as used
in SVG's properties that can take color values):

    <color> <icccolor>?

The **values** attribute for the **animateColor** element consists of a
semicolon-separated list of color values, with each color value expressed in
the above syntax.

Out of range color values can be provided, but user agent processing will be
implementation dependent. User agents should clamp color values to allow
color range values as late as possible, but note that system differences
might preclude consistent behavior across different systems.

The **color-interpolation** property applies to color interpolations that
result from **animateColor** animations.

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.animate.Animate`

SVG Animation Attributes
------------------------

* onbegin, onend, onrepeat, onload (:doc:`Animation Event Attributes </attributes/animation_events>`)
* attributeType, attributeName (:doc:`Animation Target Attributes </attributes/animation_target>`)
* begin, dur, end, min, max, restart, repeatCount, repeatDur, fill (:doc:`Animation Timing Attributes </attributes/animation_timing>`)
* calcMode, values, keyTimes, keySplines, from, to, by (:doc:`Animation Value Attributes </attributes/animation_value>`)
* additive, accumulate (:doc:`Animation Addition Attributes </attributes/animation_addition>`)

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`XLink Attributes </attributes/xlink>`

AnimateTransform
================

.. autoclass:: svgwrite.animate.AnimateTransform

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AnimateTransformElement

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.animate.Animate`

Methods
-------

.. automethod:: svgwrite.animate.AnimateTransform.__init__

SVG Animation Attributes
------------------------

* onbegin, onend, onrepeat, onload (:doc:`Animation Event Attributes </attributes/animation_events>`)
* attributeType, attributeName (:doc:`Animation Target Attributes </attributes/animation_target>`)
* begin, dur, end, min, max, restart, repeatCount, repeatDur, fill (:doc:`Animation Timing Attributes </attributes/animation_timing>`)
* calcMode, values, keyTimes, keySplines, from, to, by (:doc:`Animation Value Attributes </attributes/animation_value>`)
* additive, accumulate (:doc:`Animation Addition Attributes </attributes/animation_addition>`)

SVG Attributes
--------------

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **type** -- ``'translate | scale | rotate | skewX | skewY'``

  Indicates the type of transformation which is to have its values change
  over time. If the attribute is not specified, then the effect is as if a
  value of **translate** were specified.

The **from**, **by** and **to** attributes take a value expressed using the
same syntax that is available for the given transformation type:

* For a type = ``'translate'``, each individual value is expressed as
  `<tx> [,<ty>]`.

* For a type = ``'scale'``, each individual value is expressed as
  `<sx> [,<sy>].`

* For a type = ``'rotate'``, each individual value is expressed as
  `<rotate-angle> [<cx> <cy>].`

* For a type = ``'skewX'`` and type = ``'skewY'``, each individual value is
  expressed as `<skew-angle>.`

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`XLink Attributes </attributes/xlink>`

SVG Animation Attributes
========================

.. toctree::
   :maxdepth: 2

   /attributes/animation_events
   /attributes/animation_target
   /attributes/animation_timing
   /attributes/animation_value
   /attributes/animation_addition
