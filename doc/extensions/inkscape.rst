Inkscape Extension
==================

This extension adds support for layers in `inkscape`_. A layer in inkscape is an extended *group* container with
additional *label* and *locked* attributes. Inkscape supports nested layers.

First import the inkscape extension::

    import svgwrite
    from svgwrite.extensions import Inkscape


    dwg = svgwrite.Drawing('test-inkscape-extension.svg', profile='full', size=(640, 480))

You have to activate the extension for each drawing, because additional XML name spaces are required::

    inkscape = Inkscape(dwg)

Create a new layer, all attributes that are supported by the *group* container are also allowed::

    top_layer = inkscape.layer(label="Top LAYER 1", locked=True)

Add new layer as top level layer to the SVG drawing::

    dwg.add(top_layer)

Create new elements and add them to a layer::

    line = dwg.line((100, 100), (300, 100), stroke=svgwrite.rgb(10, 10, 16, '%'), stroke_width=10)
    top_layer.add(line)

    text = dwg.text('Test', insert=(100, 100), font_size=100, fill='red')
    top_layer.add(text)

Create another layer and add them as nested layer to "Top LAYER 1"::

    nested_layer = inkscape.layer(label="Nested LAYER 2", locked=False)
    top_layer.add(nested_layer)

    text = dwg.text('Test2', insert=(100, 200), font_size=100, fill='blue')
    nested_layer.add(text)

    dwg.save()



.. _inkscape: https://inkscape.org