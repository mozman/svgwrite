# Author:  mozman
# Purpose: testing area for inkscape extension
# Created: 06.08.2018
# Copyright (c) 2018 Manfred Moitzi based on ideas of Antonio Ospite <ao2@ao2.it>
# License: MIT License

import svgwrite
from svgwrite.extensions import Inkscape


dwg = svgwrite.Drawing('test-inkscape-extension.svg', profile='full', size=(640, 480))
inkscape = Inkscape(dwg)
layer = inkscape.layer(label="top LAYER 1", locked=True)
dwg.add(layer)

line = dwg.line((100, 100), (300, 100), stroke=svgwrite.rgb(10, 10, 16, '%'), stroke_width=10)
layer.add(line)

text = dwg.text('Test', insert=(100, 100), font_size=100, fill='red')
layer.add(text)

nested_layer = inkscape.layer(label="nested LAYER 2", locked=False)
layer.add(nested_layer)

text = dwg.text('Test2', insert=(100, 200), font_size=100, fill='blue')
nested_layer.add(text)

dwg.save()


