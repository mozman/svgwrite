#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite

def marker(name):
    # Shows how to use the <marker> element.
    # W3C reference: http://www.w3.org/TR/SVG11/painting.html#MarkerElement
    #
    dwg = svgwrite.Drawing(name, size=('20cm', '15cm'), profile='full', debug=True)
    # set user coordinate space
    dwg.viewbox(width=200, height=150)

    #--start-- A red point as marker-start element
    # 'insert' represents the insertation point in user coordinate space
    # in this example its the midpoint of the circle, see below
    marker_start = dwg.marker(insert=(0, 0), size=(5, 5)) # target size of the marker

    # setting a user coordinate space for the appanded graphic elements
    # bounding coordinates for this example:
    # minx = -5, maxx = +5, miny = -5, maxy = +5
    marker_start.viewbox(minx=-5, miny=-5, width=10, height=10) # the marker user coordinate space
    marker_start.add(dwg.circle((0, 0), r=5)).fill('red', opacity=0.5)


    #--end-- A blue point as marker-end element
    # a shorter form of the code above:
    marker_end = dwg.marker(size=(5, 5)) # marker defaults: insert=(0,0)
    # set viewbox to the bounding coordinates of the circle
    marker_end.viewbox(-1, -1, 2, 2)
    marker_end.add(dwg.circle(fill='blue', fill_opacity=0.5)) # circle defaults: insert=(0,0), r=1

    #--mid-- A green point as marker-mid element
    # if you don't setup a user coordinate space, the default ucs is
    # minx = 0, miny = 0, maxx=size[0], maxy=size[1]
    # default size = (3, 3) defined by the SVG standard
    # bounding coordinates for this example:
    # minx = 0, maxx = 6, miny = 0, maxy = 6
    # => center of the viewbox = (3, 3)!
    marker_mid = dwg.marker(insert=(3, 3), size=(6, 6))
    marker_mid.add(dwg.circle((3, 3), r=3)).fill('green', opacity=0.7)

    # The drawing size of the 'start-marker' is greater than the drawing size of
    # the 'marker-mid' (r=5 > r=3), but the resulting size is defined by the
    # 'size' parameter of the marker object (size=(6,6) > size=(5,5)), so the
    # 'marker-start' is smaller than the 'marker-mid'.

    # add marker to defs section of the drawing
    dwg.defs.add(marker_start)
    dwg.defs.add(marker_mid)
    dwg.defs.add(marker_end)

    # create a new line object, fill='none' is important, because by default
    # the polyline and the polygon object is filled (tested with FF, Chrome).
    # I am not sure, if this is concurring to the SVG Standard.

    line = dwg.add(dwg.polyline(
        [(10, 10), (50, 20), (70, 50), (100, 30), (120, 140), (170, 100)],
        stroke='black', fill='none'))

    # set markers 3-tuple = ('marker-start', 'marker-mid', 'marker-end')
    line.set_markers( (marker_start, marker_mid, marker_end) )

    # or set markers direct as SVG Attributes 'marker-start', 'marker-mid',
    # 'marker-end' or 'marker' if all markers are the same.
    # line['marker'] = marker.get_funciri() # but 'marker' works only with Firefox (26.10.2010)
    dwg.save()

if __name__ == '__main__':
    marker("marker.svg")
