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

from base import BaseElement
from interface import ITransform, IXLink
from utils import iterflatlist, strlist

class TSpan(BaseElement):
    """ Within a :class:`~svgwrite.Text` element, text and font properties
    and the current text position can be adjusted with absolute or relative
    coordinate values by using the :class:`~svgwrite.TSpan` element.
    The characters to be drawn are expressed as XML character data inside the
    <tspan> element.

    :param 2-tuple insert: The *insert* parameter is the absolute insert point
        of the text, don't use this parameter in combination with the *x* or the
        *y* parameter.

    **Attributes**

    .. attribute:: text

       stores the text value.

    **SVG Attributes**

    .. attribute:: x

       *<coordinate+>*

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

       *<coordinate+>*

       The corresponding list of absolute Y coordinates for the glyphs
       corresponding to the characters within this element. The processing
       rules for the :attr:`y` attribute parallel the processing rules for
       the :attr:`x` attribute.

    .. attribute:: dx

       *<length+>*

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

       *<length+>*

       The corresponding list of relative Y coordinates for the characters
       within the ‘tspan’ element. The processing rules for the :attr:`dy` attribute
       parallel the processing rules for the :attr:`dx` attribute.

    .. attribute:: rotate

       *<angle+>*

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

    **Methods**

    .. automethod:: svgwrite.TSpan.__init__(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, **extra)

    .. automethod:: svgwrite.TSpan.tspan(text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, **extra)

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

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    elementname = 'tspan'

    def __init__(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[],
                 attribs=None, **extra):
        """
        :param string text: <tspan> content
        :param 2-tuple insert: insert pos (x, y)
        :param list x: list of absolute x-axis values for characters
        :param list y: list of absolute y-axis values for characters
        :param list dx: list of relative x-axis values for characters
        :param list dy: list of relative y-axis values for characters
        :param list rotate: list of rotation-values for characters (in degrees)

        """
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

        if x: self['x'] = strlist(list(iterflatlist(x)), ' ')
        if y: self['y'] = strlist(list(iterflatlist(y)), ' ')
        if dx: self['dx'] = strlist(list(iterflatlist(dx)), ' ')
        if dy: self['dy'] = strlist(list(iterflatlist(dy)), ' ')
        if rotate: self['rotate'] = strlist(list(iterflatlist(rotate)), ' ')

    def tspan(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[],
              attribs=None, **extra):
        """
        Add a <TSpan> object as subelement. Same params as :meth:`__init__`.

        """
        txt = TSpan(text, insert, x, y, dx, dy, rotate, attribs=None, **extra)
        self.add(txt)
        return txt

    def get_xml(self):
        xml = super(TSpan, self).get_xml()
        xml.text = unicode(self.text)
        return xml

class Text(TSpan, ITransform):
    """
    The *Text* element defines a graphics element consisting of text.
    The characters to be drawn are expressed as XML character data inside the
    <text> element.

    Refer to :ref:`TSpan SVG Attributes <TSpan-SVG-Attributes>`

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

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

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

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

    **Methods**

    .. automethod:: svgwrite.TextPath.__init__(path, text, startOffset=None, method='align', spacing='exact', attribs=None, **extra)

    .. automethod:: svgwrite.TextPath.tspan(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[], attribs=None, **extra)

    **SVG Attributes**

    * **class** -- `string` assigns one or more css-class-names to an element
    * **style** -- `string` allows per-element css-style rules to be specified
      directly on a given element
    * **externalResourcesRequired** -- `bool` *False*: if document rendering
      can proceed even if external resources are unavailable else: *True*
    * **xlink:href** -- `string` A IRI reference to an element whose
      character data content shall be used as character data for this <tref>
      element.
    * **startOffset** -- `length` An offset from the start of the *path* for
      the initial current text position, calculated using the user agent's
      distance along the path algorithm. Value as percentage or distance along
      the path measured in the current user coordinate system.
    * **method** -- ``align|stretch`` Indicates the method by which text
      should be rendered along the path.
    * **spacing** -- ``auto|exact`` Indicates how the user agent should
      determine the spacing between glyphs that are to be rendered along a path.

    **Standard SVG Attributes**

    * :doc:`Core Attributes </attributes/core>`
    * :doc:`Conditional Processing Attributes </attributes/conditional_processing>`
    * :doc:`Graphical Event Attributes </attributes/graphical_event>`
    * :doc:`Presentation Attributes </attributes/presentation>`

    """
    elementname = 'textPath'
    def __init__(self, path, text, startOffset=None, method='align', spacing='exact',
                 attribs=None, **extra):
        """
        :param path: link to <path>, *id-string* or <Path> object
        :param string text: <textPath> content
        :param number startOffset: text starts with offset from begin of path.
        :param string method: ``align|stretch``
        :param string spacing: ``exact|auto``

        """
        super(TextPath, self).__init__(attribs=attribs, **extra)
        self.text = text
        if method == 'stretch':
            self['method'] = method
        if spacing == 'auto':
            self['spacing'] = spacing
        if startOffset:
            self['startOffset'] = startOffset
        self.set_href(path)

    def tspan(self, text, insert=None, x=[], y=[], dx=[], dy=[], rotate=[],
              attribs=None, **extra):
        """
        Add a <TSpan> object as subelement.

        :param string text: <tspan> content
        :param 2-tuple insert: insert pos (x, y)
        :param list x: list of absolute x-axis values for characters
        :param list y: list of absolute y-axis values for characters
        :param list dx: list of relative x-axis values for characters
        :param list dy: list of relative y-axis values for characters
        :param list rotate: list of rotation-values for characters (in degrees)

        """
        txt = TSpan(text, insert, x, y, dx, dy, rotate, attribs=None, **extra)
        self.add(txt)
        return txt

    def get_xml(self):
        self.update_id() # if href is an object - 'id' - attribute may be changed!
        xml = super(TextPath, self).get_xml()
        xml.text = unicode(self.text)
        return xml

class TBreak(BaseElement):
    elementname = 'tbreak'
    def __init__(self):
        super (TBreak, self).__init__()
    def __getitem__(self, key):
        raise NotImplementedError("__getitem__() not supported by TBreak class.")
    def __setitem__(self, key, value):
        raise NotImplementedError("__setitem__() not supported by TBreak class.")
    def add(self, element):
        raise NotImplementedError("add() not supported by TBreak class.")

class TextArea(BaseElement, ITransform):
    #TODO: testing for TestArea
    """
    At this time <textArea> is only available for SVG 1.2 Tiny profile.

    The <textArea>  element allows simplistic wrapping of text content within a
    given region. The 'tiny' profile of SVG specifies a single rectangular region.
    Other profiles may allow a sequence of arbitrary shapes.

    Text wrapping via the 'textArea' element is available as a lightweight and
    convenient facility for simple text wrapping where a complete box model layout
    engine is not required.

    The layout of wrapped text is user agent dependent; thus, content developers
    need to be aware that there might be different results, particularly with
    regard to where line breaks occur.

    The TextArea class wraps every text added by write() or writeline() as
    <tspan> element.

    **Methods**

    .. automethod:: svgwrite.TextArea.write(text, \*\*extra)

    **SVG Attributes**

    .. attribute:: x

       *<coordinate>*

       The x-axis coordinate of one corner of the rectangular region into which
       the text content will be placed. The lacuna value is '0'.

    .. attribute:: y

       *<coordinate>*

       The y-axis coordinate of one corner of the rectangular region into which
       the text content will be placed. The lacuna value is '0'.

    .. attribute:: width

       ``'auto'`` | *<coordinate>*

       The width of the rectangular region into which the text content will be
       placed. A value of 'auto' indicates that the width of the rectangular
       region is infinite. The lacuna value is 'auto'.

    .. attribute:: height

       ``'auto'`` | *<coordinate>*

       The height of the rectangular region into which the text content will be
       placed. A value of 'auto' indicates that the height of the rectangular
       region is infinite. The lacuna value is 'auto'.

    .. attribute:: editable

       ``'auto|simple'``

       This attribute indicates whether the text can be edited. See the definition
       of the 'editable' attribute.

    .. attribute:: focusable

       ``'true|false|auto'``

       - **true:** The element is keyboard-aware and must be treated as any other
         UI component that can get focus.
       - **false:** The element is not focusable.
       - **auto:** The lacuna value. Equivalent to 'false'
         Exception: see http://www.w3.org/TR/SVGMobile12/interact.html#focusable-attr

    .. attribute:: line-increment

       ``'auto|inherit'`` | *<number>*

       The 'line-increment' property provides limited control over the size of
       each line in the block-progression-direction. This property applies to the
       'textArea' element, and to child elements of the 'textArea' element.
       The 'line-increment' property must not have any effect when used on an
       element which is not, or does not have as an ancestor, a 'textArea' element.

    .. attribute:: text-align

       ``'start|end|center|inherit'``

       Alignment in the inline progression direction in flowing text is provided
       by the text-align property.

    .. attribute:: display-align

       ``'auto|before|center|after|inherit'``

       The 'display-align' property specifies the alignment, in the
       block-progression-direction, of the text content of the 'textArea' element.

       - **auto:** For SVG, auto is equivalent to before.
       - **before:** The before-edge of the first line is aligned with the before-edge
         of the first region.
       - **center:** The lines are centered in the block-progression-direction.
       - **after:** The after-edge of the last line is aligned with the after-edge
         of the last region.

       Layout rules: see http://www.w3.org/TR/SVGMobile12/text.html#TextAreaElement

    **Supported Interfaces**

    :class:`svgwrite.interface.ITransform`
        :meth:`translate`, :meth:`rotate`, :meth:`scale`, :meth:`skewX`,
        :meth:`skewY`, :meth:`matrix`, :meth:`rev`, :meth:`del_transform`

    """
    elementname = 'textArea'
    def __init__(self, text=None, insert=None, size=None, attribs={}, **extra):
        super(TextArea, self).__init__(attribs, **extra)
        if text:
            self.write(text)
        if insert:
            self['x'] = insert[0]
            self['y'] = insert[1]
        if size:
            self['width'] = size[0]
            self['height'] = size[1]

    def line_increment(self, value):
        """ Set the line-spacing to *value*. """
        self['line-increment'] = value

    def write(self, text, **extra):
        """
        Add *text* as <tspan> elements, with extra-params for the <tspan> element.

        Use the '\n' character for line breaks.
        """
        if '\n' not in text:
            self.add(TSpan(text, **extra))
        else:
            lines= text.split('\n')
            for line in lines[:-1]:
                if line: # no text between '\n'+
                    self.add(TSpan(line, **extra))
                self.add(TBreak())
            # case "text\n" : last element is ''
            # case "texta\ntextb : last element is 'textb'
            if lines[-1]:
                self.add(TSpan(lines[-1], **extra))

