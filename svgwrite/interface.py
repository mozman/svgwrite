#coding:utf-8
# Author:  mozman
# Purpose: svg interface classes
# Created: 16.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

_horiz = {'center': 'xMid', 'left': 'xMin', 'right': 'xMax'}
_vert  = {'middle': 'YMid', 'top': 'YMin', 'bottom':'YMax'}

from utils import strlist

class IViewBox(object):
    """ The **IViewBox** interface provides the ability to specify that a
    given set of graphics stretch to fit a particular container element.

    The value of the **viewBox** attribute is a list of four numbers
    **min-x**, **min-y**, **width** and **height**, separated by whitespace
    and/or a comma, which specify a rectangle in **user space** which should
    be mapped to the bounds of the viewport established by the given element,
    taking into account attribute **preserveAspectRatio**.

    """
    def viewbox(self, minx=0, miny=0, width=0, height=0):
        """ Specify a rectangle in **user space** (no units allowed) which
        should be mapped to the bounds of the viewport established by the
        given element.

        :param number minx: left border of the viewBox
        :param number miny: top border of the viewBox
        :param number width: width of the viewBox
        :param number height: height of the viewBox

        """
        self['viewBox'] = strlist( [minx, miny, width, height] )

    def stretch(self):
        """ Stretch viewBox in x and y direction to fill viewport, does not
        preserve aspect ratio.
        """
        self['preserveAspectRatio'] = 'none'

    def fit(self, horiz="center", vert="middle", scale="meet"):
        """ Set the **preserveAspectRatio** attribute.

        :param string horiz: horizontal alignment ``'left | center | right'``
        :param string vert: vertical alignment ``'top | middle | bottom'``
        :param string scale: scale method ``'meet | slice'``

        ============= =======================================================
        Scale methods Description
        ============= =======================================================
        ``'meet'``    preserve aspect ration and zoom to limits of viewBox
        ``'slice'``   preserve aspect ration and viewBox touch viewport on
                      all bounds, viewBox will extend beyond the bounds of
                      the viewport
        ============= =======================================================

        """
        if self.debug and scale not in ('meet', 'slice'):
            raise ValueError("Invalid scale parameter '%s'" % scale)
        self['preserveAspectRatio'] = "%s%s %s" % (_horiz[horiz],_vert[vert], scale)

class ITransform(object):
    """ The **ITransform** interface operates on the **transform** attribute.
    The value of the **transform** attribute is a `<transform-list>`, which
    is defined as a list of transform definitions, which are applied in the
    order provided. The individual transform definitions are separated by
    whitespace and/or a comma. All coordinates are **user
    space coordinates**.

    """
    transformname = 'transform'
    def translate(self, tx, ty=None):
        """
        Specifies a translation by **tx** and **ty**. If **ty** is not provided,
        it is assumed to be zero.

        :param number tx: user coordinate - no units allowed
        :param number ty: user coordinate - no units allowed
        """
        self._add_transformation("translate(%s)" % strlist( [tx, ty] ))

    def rotate(self, angle, center=None):
        """
        Specifies a rotation by **angle** degrees about a given point.
        If optional parameter **center** are not supplied, the rotate is
        about the origin of the current user coordinate system.

        :param number angle: rotate-angle in degrees
        :param 2-tuple center: rotate-center as user coordinate - no units allowed

        """
        self._add_transformation("rotate(%s)" % strlist( [angle, center] ))

    def scale(self, sx, sy=None):
        """
        Specifies a scale operation by **sx** and **sy**. If **sy** is not
        provided, it is assumed to be equal to **sx**.

        :param number sx: scalar factor x-axis, no units allowed
        :param number sy: scalar factor y-axis, no units allowed

        """
        self._add_transformation("scale(%s)" % strlist( [sx, sy] ))

    def skewX(self, angle):
        """ Specifies a skew transformation along the x-axis.

        :param number angle: skew-angle in degrees, no units allowed

        """
        self._add_transformation("skewX(%s)" % angle)

    def skewY(self, angle):
        """ Specifies a skew transformation along the y-axis.

        :param number angle: skew-angle in degrees, no units allowed

        """
        self._add_transformation("skewY(%s)" % angle)

    def matrix(self, a, b, c, d, e, f):
        self._add_transformation("matrix(%s)" % strlist( [a, b, c, d, e, f] ))

    def _add_transformation(self, new_transform):
        old_transform = self.attribs.get(self.transformname, '')
        self[self.transformname] = ("%s %s" % (old_transform, new_transform)).strip()

class IXLink(object):
    """ XLink interface """
    def set_href(self, element):
        """
        Create a reference to **element**.

        :param element: if element is a `string` its the **id** name of the
          referenced element, if element is a **BaseElement** class the **id**
          SVG Attribute is used to create the reference.

        """
        self.href = element
        self.update_id()

    def set_xlink(self, role=None, arcrole=None, title=None, show=None,
                  actuate=None, type_=None):
        """ Set XLink attributes, except `href` (for `href` use :meth:`set_href`).
        """
        if role is not None:
            self['xlink:role'] = role
        if arcrole is not None:
            self['xlink:arcrole'] = arcrole
        if title is not None:
            self['xlink:title'] = title
        if show is not None:
            self['xlink:show'] = show
        if actuate is not None:
            self['xlink:actuate'] = actuate
        if type_ is not None:
            self['xlink:type'] = type_

    def update_id(self):
        if not hasattr(self, 'href'):
            return
        if isinstance(self.href, basestring):
            idstr = self.href
        else:
            idstr = self.href.get_iri()
        self.attribs['xlink:href'] = idstr
