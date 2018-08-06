#!/usr/bin/env python
#coding:utf-8
# Author:  ao2
# Purpose: create Inkscape layers with svgwrite
# Created: 26.01.2018
# License: MIT License
# Copyright (C) 2018  Antonio Ospite <ao2@ao2.it>

import svgwrite
from svgwrite.data.types import SVGAttribute


class InkscapeDrawing(svgwrite.Drawing):
    """An svgwrite.Drawing subclass which supports Inkscape layers"""
    INKSCAPE_NAMESPACE = 'http://www.inkscape.org/namespaces/inkscape'
    SODIPODI_NAMESPACE = 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'

    def __init__(self, *args, **kwargs):
        super(InkscapeDrawing, self).__init__(*args, **kwargs)

        inkscape_attributes = {
            'xmlns:inkscape': SVGAttribute('xmlns:inkscape',
                                           anim=False,
                                           types=[],
                                           const=frozenset([self.INKSCAPE_NAMESPACE])),
            'xmlns:sodipodi': SVGAttribute('xmlns:sodipodi',
                                           anim=False,
                                           types=[],
                                           const=frozenset([self.SODIPODI_NAMESPACE])),
            'inkscape:groupmode': SVGAttribute('inkscape:groupmode',
                                               anim=False,
                                               types=[],
                                               const=frozenset(['layer'])),
            'inkscape:label': SVGAttribute('inkscape:label',
                                           anim=False,
                                           types=frozenset(['string']),
                                           const=[]),
            'sodipodi:insensitive': SVGAttribute('sodipodi:insensitive',
                                                 anim=False,
                                                 types=frozenset(['string']),
                                                 const=[])
        }

        self.validator.attributes.update(inkscape_attributes)

        elements = self.validator.elements

        svg_attributes = set(elements['svg'].valid_attributes)
        svg_attributes.add('xmlns:inkscape')
        svg_attributes.add('xmlns:sodipodi')
        elements['svg'].valid_attributes = frozenset(svg_attributes)

        g_attributes = set(elements['g'].valid_attributes)
        g_attributes.add('inkscape:groupmode')
        g_attributes.add('inkscape:label')
        g_attributes.add('sodipodi:insensitive')
        elements['g'].valid_attributes = frozenset(g_attributes)

        self['xmlns:inkscape'] = self.INKSCAPE_NAMESPACE
        self['xmlns:sodipodi'] = self.SODIPODI_NAMESPACE

    def layer(self, **kwargs):
        """Create an inkscape layer.

        An optional 'label' keyword argument can be passed to set a user
        friendly name for the layer."""
        label = kwargs.pop('label', None)

        new_layer = self.g(**kwargs)
        new_layer['inkscape:groupmode'] = 'layer'

        if label:
            new_layer['inkscape:label'] = label

        return new_layer


def main():
    svg = InkscapeDrawing('inkscape-test.svg', profile='full', size=(640, 480))

    layer = svg.layer(label="Layer one")
    layer["sodipodi:insensitive"] = "true"
    svg.add(layer)

    line = svg.line((100, 100), (300, 100),
                    stroke=svgwrite.rgb(10, 10, 16, '%'),
                    stroke_width='10')
    layer.add(line)

    text = svg.text('Test', insert=(100, 100), font_size='100', fill='red')
    layer.add(text)

    svg.save()


if __name__ == "__main__":
    main()
