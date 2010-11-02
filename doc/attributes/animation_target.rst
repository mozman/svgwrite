Animation Target Attributes
===========================

.. _attributeType:

attributeType
-------------

Specifies the namespace in which the target attribute and its associated
values are defined. The attribute value is one of the following (values are
case-sensitive):

=========== =================================================================
value       description
=========== =================================================================
``CSS``     This specifies that the value of **attributeName** is the name
            of a CSS property defined as animatable in this specification.
``XML``     This specifies that the value of **attributeName** is the name
            of an XML attribute defined in the default XML namespace for the
            target element. If the value for **attributeName** has an XMLNS
            prefix, the implementation must use the associated namespace as
            defined in the scope of the target element. The attribute must
            be defined as animatable in this specification.
``auto``    The implementation should match the **attributeName** to an
            attribute for the target element. The implementation must first
            search through the list of CSS properties for a matching property
            name, and if none is found, search the default XML namespace for
            the element.
=========== =================================================================

The default value is ``'auto'``.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AttributeTypeAttribute

.. _attributeName:

attributeName
-------------

attributeName = `<attributeName>`

Specifies the name of the target attribute. An XMLNS prefix may be used to
indicate the XML namespace for the attribute. The prefix will be interpreted
in the scope of the current (i.e., the referencing) animation element.

.. seealso:: http://www.w3.org/TR/SVG11/animate.html#AttributeNameAttribute
