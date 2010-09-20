#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: text objects
# Created: 20.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
Description of the :mod:`text` module.

"""
from svgwrite.base import BaseElement
from svgwrite.interface import ITransform
from svgwrite.utils import iterflatlist, strlist2

class TSpan(BaseElement):
    """ Within a :class:`~svgwrite.Text` element, text and font properties
    and the current text position can be adjusted with absolute or relative
    coordinate values by using the :class:`~svgwrite.TSpan` element.

    **Attributes**

    .. attribute:: x

       `list`

       If a single <coordinate> is provided, then the value represents the new
       absolute X coordinate for the current text position for rendering the
       glyphs that correspond to the first character within this element or
       any of its descendants.

       If `list` of n <coordinate>s is provided, then the values represent
       new absolute X coordinates for the current text position for rendering
       the glyphs corresponding to each of the first n characters within this
       element or any of its descendants.

       If more <coordinate>s are provided than characters, then the extra
       <coordinate>s will have no effect on glyph positioning.

       If more characters exist than <coordinate>s, then for each of these
       extra characters:

         (a) if an ancestor :class:`~svgwrite.Text` or :class:`~svgwrite.TSpan`
             element specifies an absolute X coordinate for the given
             character via an :attr:`x` attribute, then that absolute X
             coordinate is used as the starting X coordinate for that
             character (nearest ancestor has precedence), else

         (b) the starting X coordinate for rendering the glyphs corresponding
             to the given character is the X coordinate of the resulting
             current text position from the most recently rendered glyph for
             the current :class:`~svgwrite.Text` element.

       If the attribute is not specified:

         (a) if an ancestor :class:`~svgwrite.Text` or :class:`~svgwrite.TSpan`
             element specifies an absolute X coordinate for a given character
             via an :attr:`x` attribute, then that absolute X coordinate is
             used (nearest ancestor has precedence), else

         (b) the starting X coordinate for rendering the glyphs corresponding
             to a given character is the X coordinate of the resulting current
             text position from the most recently rendered glyph for the current
             :class:`~svgwrite.Text` element.


    .. attribute:: y

       `list`

       The corresponding list of absolute Y coordinates for the glyphs
       corresponding to the characters within this element. The processing
       rules for the :attr:`y` attribute parallel the processing rules for
       the :attr:`x` attribute.

    .. attribute:: dx

       `list`

       If a single <length> is provided, this value represents the new
       relative X coordinate for the current text position for rendering
       the glyphs corresponding to the first character within this element
       or any of its descendants. The current text position is shifted
       along the x-axis of the current user coordinate system by <length>
       before the first character's glyphs are rendered.

       If a `list` of n <length>s is provided, then
       the values represent incremental shifts along the x-axis for the
       current text position before rendering the glyphs corresponding to
       the first n characters within this element or any of its descendants.
       Thus, before the glyphs are rendered corresponding to each character,
       the current text position resulting from drawing the glyphs for the
       previous character within the current :class:`~svgwrite.Text` element
       is shifted along the X axis of the current user coordinate system by
       <length>.

       If more <length>s are provided than characters, then any extra
       <length>s will have no effect on glyph positioning.

       If more characters exist than <length>s, then for each of these extra
       characters:

         (a) if an ancestor :class:`~svgwrite.Text` or :class:`~svgwrite.TSpan`
             element specifies a relative X coordinate for the given character
             via a *dx* attribute, then the current text position is shifted
             along the x-axis of the current user coordinate system by that
             amount (nearest ancestor has precedence), else

         (b) no extra shift along the x-axis occurs.

       If the attribute is not specified:

         (a) if an ancestor :class:`~svgwrite.Text` or :class:`~svgwrite.TSpan`
             element specifies a relative X coordinate for a given character
             via a :attr:`dx` attribute, then the current text position is shifted
             along the x-axis of the current user coordinate system by that
             amount (nearest ancestor has precedence), else

         (b) no extra shift along the x-axis occurs.

    .. attribute:: dy

       `list`

       The corresponding list of relative Y coordinates for the characters
       within the ‘tspan’ element. The processing rules for the :attr:`dy` attribute
       parallel the processing rules for the :attr:`dx` attribute.

    .. attribute:: rotate

       `list`

       The supplemental rotation about the current text position that will be
       applied to all of the glyphs corresponding to each character within
       this element.

       If a `list` of <number>s is provided, then the first <number> represents
       the supplemental rotation for the glyphs corresponding to the first
       character within this element or any of its descendants, the second
       <number> represents the supplemental rotation for the glyphs that
       correspond to the second character, and so on.

       If more <number>s are provided than there are characters, then the
       extra <number>s will be ignored.

       If more characters are provided than <number>s, then for each of these
       extra characters the rotation value specified by the last number must
       be used.

       If the attribute is not specified and if an ancestor :class:`~svgwrite.Text`
       or :class:`~svgwrite.TSpan` element specifies a supplemental rotation
       for a given character via a :attr:`rotate` attribute, then the given
       supplemental rotation is applied to the given character (nearest
       ancestor has precedence). If there are more characters than <number>s
       specified in the ancestor's :attr:`rotate` attribute, then for each of
       these extra characters the rotation value specified by the last number
       must be used.

       This supplemental rotation has no impact on the rules by which current
       text position is modified as glyphs get rendered and is supplemental
       to any rotation due to text on a path and to ‘glyph-orientation-horizontal’
       or ‘glyph-orientation-vertical’.

    """
    elementname = 'tspan'

    def __init__(self, text, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, **extra):
        super(TSpan, self).__init(attribs=attribs, **extra)
        self.text = text
        self.x = list(iterflatlist(x))
        self.y = list(iterflatlist(y))
        self.dx = list(iterflatlist(dx))
        self.dy = list(iterflatlist(dy))
        self.rotate = list(iterflatlist(rotate))

    def to_xml(self):
        self['x'] = strlist2(iterflatlist(self.x))
        self['y'] = strlist2(iterflatlist(self.y))
        self['dx'] = strlist2(iterflatlist(self.dx))
        self['dy'] = strlist2(iterflatlist(self.dy))
        self['rotate'] = strlist2(iterflatlist(self.rotate))
        xml = super(TSpan, self).to_xml()
        xml.text = self.text
        return xml

class Text(TSpan, ITransform):
    """ The *Text* element defines a graphics element consisting of text.

    **Attributes**

    .. attribute:: x

       `list`

       If a single *coordinate*  is provided, then the value
       represents the new absolute X coordinate for the current text position
       for rendering the glyphs that correspond to the first character within
       this element or any of its descendants.

       If a `list` of n *coordinates* is provided, then the values represent
       new absolute X *coordinates* for the current text position for rendering
       the glyphs corresponding to each of the first n characters within this
       element or any of its descendants.

       If the attribute is not specified, the effect is as if a value of "0"
       were specified.

    .. attribute:: y

       `list`

       The corresponding `list` of absolute Y *coordinates* for the glyphs
       corresponding to the characters within this element. The processing
       rules for the *y* attribute parallel the processing rules for the *x*
       attribute.

       If the attribute is not specified, the effect is as if a value of "0"
       were specified.

    .. attribute:: dx

       `list`

       Shifts in the current text position along the x-axis for
       the characters within this element or any of its descendants.

       Refer to the description of the :attr:`~TSpan.dx` attribute on the :class:`~svgwrite.TSpan`
       element.

       If the attribute is not specified on this element or any of its
       descendants, no supplemental shifts along the x-axis will occur.

    .. attribute:: dy

       `list`

       Shifts in the current text position along the y-axis for
       the characters within this element or any of its descendants.

       Refer to the description of the :attr:`~TSpan.dy` attribute on the
       :class:`~svgwrite.TSpan` element.

       If the attribute is not specified on this element or any of its
       descendants, no supplemental shifts along the y-axis will occur.

    .. attribute:: rotate

       `list`

       The supplemental rotation about the current text position
       that will be applied to all of the glyphs corresponding to each character
       within this element.

       Refer to the description of the :attr:`~TSpan.rotate` attribute on the :class:`~svgwrite.TSpan`
       element.

       If the attribute is not specified on this element or any of its
       descendants, no supplemental rotations will occur.

    **SVG Attributes**

    * **textLength** -- `length` The purpose of this attribute is to allow
      the author to achieve exact alignment, in visual rendering order after
      any bidirectional reordering, for the first and last rendered glyphs
      that correspond to this element; thus, for the last rendered character
      (in visual rendering order after any bidirectional reordering), any
      supplemental inter-character spacing beyond normal glyph advances are
      ignored (in most cases) when the user agent determines the appropriate
      amount to expand/compress the text string to fit within a length of
      *textLength*.

    * **lengthAdjust** -- ``"spacing|spacingAndGlyphs"`` Indicates the type
      of adjustments which the user agent shall make to make the rendered
      length of the text match the value specified on the *textLength*
      attribute.

      * ``"spacing"`` indicates that only the advance values are adjusted. The
        glyphs themselves are not stretched or compressed.

      * ``"spacingAndGlyphs"`` indicates that the advance values are adjusted and
        the glyphs themselves stretched or compressed in one axis (i.e., a
        direction parallel to the inline-progression-direction).

      If the attribute is not specified, the effect is as a value of *spacing*
      were specified.

    """
    elementname = 'text'

class TRef(BaseElement):
    """ The <tref> element.

    **Attributes**

    """
    elementname = 'tref'

class TextPath(BaseElement):
    """ The <textPath> element.

    **Attributes**

    """
    elementname = 'textPath'

