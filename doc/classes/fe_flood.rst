.. _feFlood:

feFlood Filter Element
======================

.. seealso:: http://www.w3.org/TR/SVG11/filters.html#feFloodElement

This filter primitive creates a rectangle filled with the color and opacity
values from properties **flood-color** and **flood-opacity**. The rectangle is
as large as the filter primitive subregion established by the **x**, **y**,
**width** and **height** attributes on the **feFlood** element.

For common properties see: :ref:`filter_primitive`

SVG Attributes
--------------

* **flood-color** -- ``'currentColor'`` | `<color>` [`<icccolor>`] | ``' inherit'``

  initial value is ``'black'``

* **flood-opacity** -- 	`<opacity-value>` | ``'inherit'``

  initial value is ``'1'``