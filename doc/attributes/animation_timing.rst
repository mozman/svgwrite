Animation Timing Attributes
===========================

.. _begin:

begin
-----

begin = `<begin-value-list>`

Defines when the element should begin (i.e. become active).

The attribute value is a semicolon separated list of values.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#BeginAttribute

.. _dur:

dur
---

dur = `<Clock-value>` | ``'media | indefinite'``

Specifies the simple duration.

The attribute value can be one of the following:

=============== ==============================================================
value           description
=============== ==============================================================
`<Clock-value>` Specifies the length of the simple duration in presentation
                time. Value must be greater than 0.
``media``       Specifies the simple duration as the intrinsic media duration.
                This is only valid for elements that define media.(For SVG's
                animation elements, if ``'media'`` is specified, the attribute
                will be ignored.)
``indefinite``  Specifies the simple duration as indefinite.
=============== ==============================================================

If the animation does not have a **dur** attribute, the simple duration is
indefinite. Note that interpolation will not work if the simple duration is
indefinite (although this may still be useful for **set** elements).

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#DurAttribute

.. _end:

end
---

end = `<end-value-list>`

Defines an end value for the animation that can constrain the active duration.

The attribute value is a semicolon separated list of values.

A value of ``'indefinite'`` specifies that the end of the animation will be
determined by an endElement method call (the animation DOM methods are
described in DOM interfaces).

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#EndAttribute

.. _min:

min
---

min = `<Clock-value>` | ``'media'``

Specifies the minimum value of the active duration.

=============== =============================================================
value           description
=============== =============================================================
`<Clock-value>` Specifies the length of the minimum value of the active
                duration, measured in local time.
                Value must be greater than 0.
``'media'``     Specifies the minimum value of the active duration as the
                intrinsic media duration. This is only valid for elements
                that define media. (For SVG's animation elements, if
                ``'media'`` is specified, the attribute will be ignored.)
=============== =============================================================

The default value for **min** is ``'0'``. This does not constrain the active
duration at all.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#MinAttribute

.. _max:

max
---

max = `<Clock-value>` | ``'media'``

Specifies the maximum value of the active duration.

=============== =============================================================
value           description
=============== =============================================================
`<Clock-value>` Specifies the length of the maximum value of the active
                duration, measured in local time.
                Value must be greater than 0.
``'media'``     Specifies the maximum value of the active duration as the
                intrinsic media duration. This is only valid for elements
                that define media. (For SVG's animation elements, if
                ``'media'`` is specified, the attribute will be ignored.)
=============== =============================================================

There is no default value for **max**. This does not constrain the active
duration at all.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#MaxAttribute

.. _restart:

restart
-------

restart = ``'always | whenNotActive | never'``

=================== ==========================================================
value               description
=================== ==========================================================
``'always'``        The animation can be restarted at any time. This is the
                    default value.
``'whenNotActive'`` The animation can only be restarted when it is not active
                    (i.e. after the active end). Attempts to restart the
                    animation during its active duration are ignored.
``'never'``         The element cannot be restarted for the remainder of the
                    current simple duration of the parent time container.
                    (In the case of SVG, since the parent time container is
                    the SVG document fragment, then the animation cannot be
                    restarted for the remainder of the document duration.)
=================== ==========================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#RestartAttribute

.. _repeatCount:

repeatCount
-----------

repeatCount = `<number>` | ``'indefinite'``

Specifies the number of iterations of the animation function. It can have the
following attribute values:

================ ============================================================
value            description
================ ============================================================
`<number>`       This is a (base 10) "floating point" numeric value that
                 specifies the number of iterations. It can include partial
                 iterations expressed as fraction values. A fractional value
                 describes a portion of the simple duration. Values must be
                 greater than 0.
``'indefinite'`` The animation is defined to repeat indefinitely (i.e. until
                 the document ends).
================ ============================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#RepeatCountAttribute

.. _repeatDur:

repeatDur
---------

repeatDur = `<Clock-value>` | ``'indefinite'``

Specifies the total duration for repeat. It can have the following attribute
values:

================ ============================================================
value            description
================ ============================================================
`<Clock-value>`  Specifies the duration in presentation time to repeat the
                 animation function f(t).
``'indefinite'`` The animation is defined to repeat indefinitely (i.e. until
                 the document ends).
================ ============================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#RepeatDurAttribute

.. _animateFill:

fill
----

fill = ``'freeze | remove'``

This attribute can have the following values:

============ ================================================================
value        description
============ ================================================================
``'freeze'`` The animation effect F(t) is defined to freeze the effect value
             at the last value of the active duration. The animation effect
             is "frozen" for the remainder of the document duration (or until
             the animation is restarted - see SMIL Animation: Restarting
             animation).
``'remove'`` The animation effect is removed (no longer applied) when the
             active duration of the animation is over. After the active end
             of the animation, the animation no longer affects the target
             (unless the animation is restarted - see SMIL Animation:
             Restarting animation).

             This is the default value.
============ ================================================================

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#FillAttribute