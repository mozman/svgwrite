# Copyright (c) 2018 Manfred Moitzi
# License: MIT License
import pytest

import svgwrite
from svgwrite.extensions import Inkscape
from svgwrite.extensions.inkscape import GROUP_MODE, LABEL

@pytest.fixture
def dwg():
    return svgwrite.Drawing('test-inkscape-extension.svg', profile='full', size=(640, 480))

def test_layer(dwg):
    inkscape = Inkscape(dwg)
    layer = inkscape.layer(label="Layer one", locked=True)
    dwg.add(layer)
    assert layer[GROUP_MODE] == 'layer'
    assert layer[LABEL] == 'Layer one'


def test_add_line_to_layer(dwg):
    inkscape = Inkscape(dwg)
    layer = inkscape.layer(label="Layer one", locked=True)
    dwg.add(layer)

    line = dwg.line((100, 100), (300, 100), stroke=svgwrite.rgb(10, 10, 16, '%'), stroke_width=10)
    layer.add(line)

    text = dwg.text('Test', insert=(100, 100), font_size=100, fill='red')
    layer.add(text)
