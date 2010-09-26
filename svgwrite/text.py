#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: text objects
# Created: 20.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
Text that is to be rendered as part of an SVG document fragment is specified
using the <text> element. The characters to be drawn are expressed as XML
character data inside the <text> element.

"""
from svgwrite import parameter
from svgwrite.base import BaseElement
from svgwrite.interface import ITransform, IXLink
from svgwrite.utils import iterflatlist, strlist

class TSpan(BaseElement):
    """ Within a :class:`~svgwrite.Text` element, text and font properties
    and the current text position can be adjusted with absolute or relative
    coordinate values by using the :class:`~svgwrite.TSpan` element.

    :param 2-tuple insert: The *insert* parameter is the absolute insert point
        of the text, don't use this parameter in combination with the *x* or the
        *y* parameter.

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

    .. _TSpan-SVG-Attributes:

    **Supported SVG Attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering can proceed
        even if external resources are unavailable else: *True*
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

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes

    """
    elementname = 'tspan'

    def __init__(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[],
                 attribs=None, **extra):
        super(TSpan, self).__init__(attribs=attribs, **extra)
        self.text = text
        if insert is not None:
            if isinstance(insert, basestring):
                raise TypeError("'insert' should be a <tuple> or a <list>  with" \
                                " at least two elements.")
            if x or y:
                raise ValueError("Use 'insert' and 'x' or 'y' parameter not" \
                                 " at the same time!")
            x = [insert[0]]
            y = [insert[1]]

        self.x = list(iterflatlist(x))
        self.y = list(iterflatlist(y))
        self.dx = list(iterflatlist(dx))
        self.dy = list(iterflatlist(dy))
        self.rotate = list(iterflatlist(rotate))

    def tspan(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[],
              attribs=None, **extra):
        txt = TSpan(text, insert, x, y, dx, dy, rotate, attribs=None, **extra)
        self.add(txt)
        return txt

    def get_xml(self):
        self['x'] = strlist(iterflatlist(self.x), ' ')
        self['y'] = strlist(iterflatlist(self.y), ' ')
        self['dx'] = strlist(iterflatlist(self.dx), ' ')
        self['dy'] = strlist(iterflatlist(self.dy), ' ')
        self['rotate'] = strlist(iterflatlist(self.rotate), ' ')
        xml = super(TSpan, self).get_xml()
        xml.text = unicode(self.text)
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

       Refer to the description of the :attr:`~TSpan.x` attribute on the :class:`~svgwrite.TSpan`
       element.

    .. attribute:: y

       `list`

       The corresponding `list` of absolute Y *coordinates* for the glyphs
       corresponding to the characters within this element. The processing
       rules for the *y* attribute parallel the processing rules for the *x*
       attribute.

       If the attribute is not specified, the effect is as if a value of "0"
       were specified.

       Refer to the description of the :attr:`~TSpan.y` attribute on the :class:`~svgwrite.TSpan`
       element.

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

    Refer to :ref:`TSpan SVG Attributes <TSpan-SVG-Attributes>`

    """
    elementname = 'text'

class TRef(BaseElement, IXLink):
    """
    The textual content for a <text> can be either character data directly
    embedded within the <text> element or the character data content of a
    referenced element, where the referencing is specified with a <tref>
    element.

    .. automethod:: svgwrite.TRef.__init__(element, attribs=None, **extra)

    .. automethod:: svgwrite.TRef.set_href(element)

    **SVG Attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*
    * **xlink:href** -- `string` A IRI reference to an element whose
      character data content shall be used as character data for this <tref>
      element.

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes

    """
    elementname = 'tref'

    def __init__(self, element, attribs=None, **extra):
        """
        :param element: create a reference this element, if element is a
          `string` its the *id* name of the referenced element, if element
          is a :class:`~svgwrite.base.BaseElement` the *id* SVG Attribute is
          used to create the reference.
        """
        super(TRef, self).__init__(attribs=attribs, **extra)
        self.set_href(element)

    def get_xml(self):
        self.update_id() # if href is an object - 'id' - attribute may be changed!
        return super(TRef, self).get_xml()

class TextPath(BaseElement, IXLink):
    """
    In addition to text drawn in a straight line, SVG also includes the
    ability to place text along the shape of a <path> element. To specify that
    a block of text is to be rendered along the shape of a <path>, include
    the given text within a <textPath> element which includes an `xlink:href`
    attribute with a IRI reference to a <path> element.

    **Attributes**

    **Standard SVG Attributes**

    for description see :ref:`Common SVG Attributs <Common-SVG-Attributs>`

    * Core Attributes
    * Conditional Processing Attributes
    * Graphical Event Attributes
    * Presentation Attributes
    """
    elementname = 'textPath'
    def __init__(self, path, startOffset=0, method='align', spacing='exact',
                 attribs=None, **extra):
        super(TextPath, self).__init__(attribs=attribs, **extra)
        if method == 'stretch':
            self.attribs['method'] = method
        if spacing == 'auto':
            self.attribs['spacing'] = spacing
        self.attribs['startOffset'] = startOffset
        self.set_href(path)

    def get_xml(self):
        self.update_id() # if href is an object - 'id' - attribute may be changed!
        return super(TextPath, self).get_xml()

