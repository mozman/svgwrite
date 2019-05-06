# Copyright (c) 2018 Manfred Moitzi
# Copyright (c) 2019 Christof Hanke
# License: MIT License
import pytest

import svgwrite
from svgwrite.extensions.shapes import *

@pytest.fixture
def dwg():
    return svgwrite.Drawing('test-regular-polygon-extension.svg', profile='full', size=(640, 480))

@pytest.fixture
def heptagon():
    return  ngon(7, 10)

def test_regular_polygon(dwg, heptagon):
    # round the vertices so that the numbers don't get too ugly
    rounded_heptagon = [(round(x, 5), round(y, 5)) for x,y in  heptagon]
    assert(dwg.polygon(rounded_heptagon).tostring() == '<polygon points="5.0,-10.38261 11.2349,-2.56429 9.00969,7.18499 0.0,11.52382 -9.00969,7.18499 -11.2349,-2.56429 -5.0,-10.38261" />')

def test_rotate(dwg, heptagon):
    heptagon = rotate(heptagon, math.pi)
    # round the vertices so that the numbers don't get too ugly
    rounded_heptagon = [(round(x, 5), round(y, 5)) for x,y in heptagon]
    assert(dwg.polygon(rounded_heptagon).tostring() == '<polygon points="-5.0,10.38261 -11.2349,2.56429 -9.00969,-7.18499 -0.0,-11.52382 9.00969,-7.18499 11.2349,2.56429 5.0,10.38261" />')

def test_scale(dwg, heptagon):
    heptagon = scale(heptagon, 2, 2)
    # round the vertices so that the numbers don't get too ugly
    rounded_heptagon = [(round(x, 5), round(y, 5)) for x,y in heptagon]
    assert(dwg.polygon(rounded_heptagon).tostring() == '<polygon points="10.0,-20.76521 22.4698,-5.12858 18.01938,14.36997 0.0,23.04765 -18.01938,14.36997 -22.4698,-5.12858 -10.0,-20.76521" />')

def test_translate(dwg, heptagon):
    heptagon = translate(heptagon, 2, 2)
    # round the vertices so that the numbers don't get too ugly
    rounded_heptagon = [(round(x, 5), round(y, 5)) for x,y in heptagon]
    assert(dwg.polygon(rounded_heptagon).tostring() == '<polygon points="7.0,-8.38261 13.2349,-0.56429 11.00969,9.18499 2.0,13.52382 -7.00969,9.18499 -9.2349,-0.56429 -3.0,-8.38261" />')

def test_centroid(dwg, heptagon):
    c_x, c_y = centroid(heptagon)
    # round the vertices so that the numbers don't get too ugly
    c_x = round(c_x, 5)
    c_y = round(c_y, 5)
    assert((c_x, c_y) == (0,0))
