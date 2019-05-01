# Copyright (c) 2018 Manfred Moitzi
# Copyright (c) 2019 Christof Hanke
# License: MIT License
import pytest

import svgwrite
from svgwrite.extensions import RegularPolygonFactory

@pytest.fixture
def dwg():
    return svgwrite.Drawing('test-regular-polygon-extension.svg', profile='full', size=(640, 480))

def test_regular_polygon(dwg):
    regular_polygon_factory = RegularPolygonFactory(dwg)
    pentagon = regular_polygon_factory.get(5, 10, center=(100,100), fill="none", stroke_width="1mm", stroke="black")
    dwg.add(pentagon)
