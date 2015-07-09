Animation Addition Attributes
=============================

additive
--------

additive = ``'replace | sum'``

Controls whether or not the animation is additive.

============= =================================================================
value         description
============= =================================================================
``'sum'``     Specifies that the animation will add to the underlying value of
              the attribute and other lower priority animations.
``'replace'`` Specifies that the animation will override the underlying value
              of the attribute and other lower priority animations. This is the
              default, however the behavior is also affected by the animation
              value attributes **by** and **to**, as described in SMIL
              Animation: How from, to and by attributes affect additive
              behavior.
============= =================================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AdditiveAttribute

accumulate
----------

accumulate = ``'none | sum'``

Controls whether or not the animation is cumulative.

=========== =================================================================
value       description
=========== =================================================================
``'sum'``   Specifies that each repeat iteration after the first builds upon
            the last value of the previous iteration.
``'none'``  Specifies that repeat iterations are not cumulative. This is the
            default.
=========== =================================================================

This attribute is ignored if the target attribute value does not support
addition, or if the animation element does not repeat.

Cumulative animation is not defined for "to animation".

This attribute will be ignored if the animation function is specified with
only the **to** attribute.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AccumulateAttribute