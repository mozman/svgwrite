Text
====

.. automodule:: svgwrite.text

.. autoclass:: svgwrite.text.Text

.. seealso:: http://www.w3.org/TR/SVG11/text.html#TextElement

Refer to **TSpan** SVG Attributes

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.text.TSpan`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`

TSpan
=====

.. autoclass:: svgwrite.text.TSpan

.. seealso:: http://www.w3.org/TR/SVG11/text.html#TSpanElement

.. automethod::  svgwrite.text.TSpan.__init__

Attributes
----------

.. attribute:: TSpan.text

   stores the text value.

Methods
-------

.. automethod:: svgwrite.text.TSpan.__init__

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **x** -- `<coordinate+>`

   If a single `<coordinate>` is provided, then the value represents the new
   absolute X coordinate for the current text position for rendering the
   glyphs that correspond to the first character within this element or
   any of its descendants.

   If `list` of n `<coordinates>` is provided, then the values represent
   new absolute X coordinates for the current text position for rendering
   the glyphs corresponding to each of the first n characters within this
   element or any of its descendants.

   If more `<coordinates>` are provided than characters, then the extra
   `<coordinates>` will have no effect on glyph positioning.

   If more characters exist than `<coordinates>` , then for each of these
   extra characters:

     (a) if an ancestor **Text** or **TSpan**
         element specifies an absolute X coordinate for the given
         character via an **x** attribute, then that absolute X
         coordinate is used as the starting X coordinate for that
         character (nearest ancestor has precedence), else

     (b) the starting X coordinate for rendering the glyphs corresponding
         to the given character is the X coordinate of the resulting
         current text position from the most recently rendered glyph for
         the current **Text** element.

   If the attribute is not specified:

     (a) if an ancestor **Text** or **TSpan**
         element specifies an absolute X coordinate for a given character
         via an **x** attribute, then that absolute X coordinate is
         used (nearest ancestor has precedence), else

     (b) the starting X coordinate for rendering the glyphs corresponding
         to a given character is the X coordinate of the resulting current
         text position from the most recently rendered glyph for the current
         **Text** element.


* **y** -- `<coordinate+>`

   The corresponding list of absolute Y coordinates for the glyphs
   corresponding to the characters within this element. The processing
   rules for the **y** attribute parallel the processing rules for
   the **x** attribute.

* **dx** -- `<length+>`

   If a single <length> is provided, this value represents the new
   relative X coordinate for the current text position for rendering
   the glyphs corresponding to the first character within this element
   or any of its descendants. The current text position is shifted
   along the x-axis of the current user coordinate system by `<length>`
   before the first character's glyphs are rendered.

   If a `list` of n `<length>` is provided, then
   the values represent incremental shifts along the x-axis for the
   current text position before rendering the glyphs corresponding to
   the first n characters within this element or any of its descendants.
   Thus, before the glyphs are rendered corresponding to each character,
   the current text position resulting from drawing the glyphs for the
   previous character within the current **Text** element
   is shifted along the X axis of the current user coordinate system by
   `<length>` .

   If more `<lengths>` are provided than characters, then any extra
   `<lengths>` will have no effect on glyph positioning.

   If more characters exist than <length>s, then for each of these extra
   characters:

     (a) if an ancestor **Text** or **TSpan**
         element specifies a relative X coordinate for the given character
         via a **dx** attribute, then the current text position is shifted
         along the x-axis of the current user coordinate system by that
         amount (nearest ancestor has precedence), else

     (b) no extra shift along the x-axis occurs.

   If the attribute is not specified:

     (a) if an ancestor **Text** or **TSpan**
         element specifies a relative X coordinate for a given character
         via a **dx** attribute, then the current text position is shifted
         along the x-axis of the current user coordinate system by that
         amount (nearest ancestor has precedence), else

     (b) no extra shift along the x-axis occurs.

* **dy** -- `<length+>`

   The corresponding list of relative Y coordinates for the characters
   within the **tspan** element. The processing rules for the **dy** attribute
   parallel the processing rules for the **dx** attribute.

* **rotate** -- `<angle+>`

   The supplemental rotation about the current text position that will be
   applied to all of the glyphs corresponding to each character within
   this element.

   If a `list` of `<numbers>` is provided, then the first `<number>` represents
   the supplemental rotation for the glyphs corresponding to the first
   character within this element or any of its descendants, the second
   <number> represents the supplemental rotation for the glyphs that
   correspond to the second character, and so on.

   If more `<numbers>` are provided than there are characters, then the
   extra `<numbers>` will be ignored.

   If more characters are provided than `<numbers>`, then for each of these
   extra characters the rotation value specified by the last number must
   be used.

   If the attribute is not specified and if an ancestor **Text**
   or **TSpan** element specifies a supplemental rotation
   for a given character via a **rotate** attribute, then the given
   supplemental rotation is applied to the given character (nearest
   ancestor has precedence). If there are more characters than `<numbers>`
   specified in the ancestor's **rotate** attribute, then for each of
   these extra characters the rotation value specified by the last number
   must be used.

   This supplemental rotation has no impact on the rules by which current
   text position is modified as glyphs get rendered and is supplemental
   to any rotation due to text on a path and to **glyph-orientation-horizontal**
   or **glyph-orientation-vertical**.

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **textLength** -- `<length>`

  The purpose of this attribute is to allow
  the author to achieve exact alignment, in visual rendering order after
  any bidirectional reordering, for the first and last rendered glyphs
  that correspond to this element; thus, for the last rendered character
  (in visual rendering order after any bidirectional reordering), any
  supplemental inter-character spacing beyond normal glyph advances are
  ignored (in most cases) when the user agent determines the appropriate
  amount to expand/compress the text string to fit within a length of
  **textLength**.

* **lengthAdjust** -- ``'spacing | spacingAndGlyphs'``

  Indicates the type of adjustments which the user agent shall make to make
  the rendered length of the text match the value specified on the **textLength**
  attribute.

  * ``'spacing'`` indicates that only the advance values are adjusted. The
    glyphs themselves are not stretched or compressed.

  * ``'spacingAndGlyphs'`` indicates that the advance values are adjusted and
    the glyphs themselves stretched or compressed in one axis (i.e., a
    direction parallel to the inline-progression-direction).

  If the attribute is not specified, the effect is as a value of *spacing*
  were specified.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`

TRef
====

.. autoclass:: svgwrite.text.TRef

.. seealso:: http://www.w3.org/TR/SVG11/text.html#TRefElement

.. automethod:: svgwrite.text.TRef.__init__

.. automethod:: svgwrite.text.TRef.set_href

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **xlink:href** -- `<string>`
  A IRI reference to an element whose character data content shall be used
  as character data for this **tref** element.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`

TextPath
========

.. autoclass:: svgwrite.text.TextPath

.. seealso:: http://www.w3.org/TR/SVG11/text.html#TextPathElement

Methods
-------

.. automethod:: svgwrite.text.TextPath.__init__

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.XLink`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **class** -- `string`

  assigns one or more css-class-names to an element

* **style** -- `string`

  allows per-element css-style rules to be specified directly on a given element

* **externalResourcesRequired** -- `bool`

  *False*: if document rendering can proceed even if external resources are
  unavailable else: *True*

* **xlink:href** -- `string`

  A IRI reference to an element whose character data content shall be used
  as character data for this **TRef** element.

* **startOffset** -- `<length>`

  An offset from the start of the **path** for
  the initial current text position, calculated using the user agent's
  distance along the path algorithm. Value as percentage or distance along
  the path measured in the current user coordinate system.

* **method** -- ``'align | stretch'``

  Indicates the method by which text should be rendered along the path.

* **spacing** -- ``'auto | exact'``

  Indicates how the user agent should determine the spacing between glyphs
  that are to be rendered along a path.

Standard SVG Attributes
-----------------------

* :doc:`Core Attributes </attributes/core>`
* :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
* :doc:`Graphical Event Attributes </attributes/graphical_event>`
* :doc:`Presentation Attributes </attributes/presentation>`

TextArea
========

.. autoclass:: svgwrite.text.TextArea

.. seealso:: http://www.w3.org/TR/SVGMobile12/text.html#TextAreaElement

Methods
-------

.. automethod:: svgwrite.text.TextArea.write

Parent Classes
--------------

* :class:`svgwrite.base.BaseElement`
* :class:`svgwrite.mixins.Transform`
* :class:`svgwrite.mixins.Presentation`

SVG Attributes
--------------

* **x** -- *<coordinate>*

   The x-axis coordinate of one corner of the rectangular region into which
   the text content will be placed. The lacuna value is ``'0'``.

* **y** -- *<coordinate>*

   The y-axis coordinate of one corner of the rectangular region into which
   the text content will be placed. The lacuna value is ``'0'``.

* **width** -- ``'auto'`` | *<coordinate>*

   The width of the rectangular region into which the text content will be
   placed. A value of ``'auto'`` indicates that the width of the rectangular
   region is infinite. The lacuna value is ``'auto'``.

* **height** -- ``'auto'`` | *<coordinate>*

   The height of the rectangular region into which the text content will be
   placed. A value of ``'auto'`` indicates that the height of the rectangular
   region is infinite. The lacuna value is ``'auto'``.

* **editable** -- ``'auto`| simple'``

   This attribute indicates whether the text can be edited. See the definition
   of the 'editable' attribute.

* **focusable** -- ``'true | false | auto'``

   ===========  =============================================================
   Value        Description
   ===========  =============================================================
   ``'true'``   The element is keyboard-aware and must be treated as any
                other UI component that can get focus.
   ``'false'``  The element is not focusable.
   ``'auto'``   The lacuna value. Equivalent to ``'false'``
   ===========  =============================================================

   Exception: see http://www.w3.org/TR/SVGMobile12/interact.html#focusable-attr

* **line-increment** -- ``'auto | inherit'`` | `<number>`

   The **line-increment** property provides limited control over the size of
   each line in the block-progression-direction. This property applies to the
   **textArea** element, and to child elements of the **textArea** element.
   The **line-increment** property must not have any effect when used on an
   element which is not, or does not have as an ancestor, a **textArea**
   element.

* **text-align** -- ``'start | end | center | inherit'``

   Alignment in the inline progression direction in flowing text is provided
   by the text-align property.

* **display-align** -- ``'auto | before | center | after | inherit'``

   The **display-align** property specifies the alignment, in the
   block-progression-direction, of the text content of the **textArea** element.

   =============  ===========================================================
   Value          Description
   =============  ===========================================================
   ``'auto'``     For SVG, auto is equivalent to before.
   ``'before'``   The before-edge of the first line is aligned with the
                  before-edge of the first region.
   ``'center'``   The lines are centered in the block-progression-direction.
   ``'after'``    The after-edge of the last line is aligned with the
                  after-edge of the last region.
   =============  ===========================================================

   Layout rules: see http://www.w3.org/TR/SVGMobile12/text.html#TextAreaElement
