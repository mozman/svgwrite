#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: reproducing marker examples from http://vanseodesign.com/web-design/svg-markers/
# Created: 27.02.2017
# Copyright (C) 2017, Manfred Moitzi
# License: MIT License
import svgwrite


def create_arrow_marker(dwg):
    #   <defs>
    #     <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
    #       <path d="M0,0 L0,6 L9,3 z" fill="#f00" />
    #     </marker>
    #   </defs>
    arrow = dwg.marker(id='arrow', insert=(0, 3), size=(10, 10), orient='auto', markerUnits='strokeWidth')
    arrow.add(dwg.path(d='M0,0 L0,6 L9,3 z', fill='#f00'))
    dwg.defs.add(arrow)
    return arrow


def create_arrow_marker_sumner(dwg):
    #   <defs>
    #     <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
    #       <path d="M0,0 L0,6 L9,3 z" fill="#f00" />
    #     </marker>
    #   </defs>
    # your drawing area is 20, 10, the tip of the arrow is at 20, 5 and the end of the arrow is at (3.128, 5)
    # L x, y uses absolute coords, l dx, dy uses relative coords
    arrow = dwg.marker(id='arrow', insert=(3.128, 5), size=(20, 10), orient='auto', markerUnits='strokeWidth')
    arrow.add(dwg.path(d='M0,10 l3.128,-5 l-3.128,-5 l20,5 Z', fill='#f00'))
    dwg.defs.add(arrow)
    return arrow


def marker01(name):
    # example http://vanseodesign.com/web-design/svg-markers/
    # <svg width="600px" height="100px">
    #   <defs>
    #     <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
    #       <path d="M0,0 L0,6 L9,3 z" fill="#f00" />
    #     </marker>
    #   </defs>
    #
    #   <line x1="50" y1="50" x2="250" y2="50" stroke="#000" stroke-width="5" marker-end="url(#arrow)" />
    # </svg>

    dwg = svgwrite.Drawing(name, size=('600px', '100px'), profile='full', debug=True)
    arrow = create_arrow_marker_sumner(dwg)
    # set marker attributes without marker-mixin works
    line = dwg.line(start=(50, 50), end=(250, 50), stroke='#000', stroke_width=5,
                    marker_end=arrow.get_funciri())
    # marker-mixin does not work line.set_markers(('', '', arrow))
    # not useful here: line.set_markers(arrow) sets start and mid and end maker at once to the same maker
    # not useful here: line.set_markers(start_arrow, mid_maker, end_arrow) sets start and mid and end maker at once
    # NEW in v1.1.11 line.set_markers((None, None, arrow)) works to just set the end marker
    dwg.add(line)
    dwg.save(pretty=True)


def marker02(name):
    # example http://vanseodesign.com/web-design/svg-markers/
    # <svg width="600px" height="100px">
    #   <defs>
    #     <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
    #       <path d="M0,0 L0,6 L9,3 z" fill="#f00" />
    #     </marker>
    #   </defs>
    #
    #   <line x1="295" y1="50" x2="95" y2="75" stroke="#000" stroke-width="5" marker-end="url(#arrow)" />
    # </svg>

    dwg = svgwrite.Drawing(name, size=('600px', '100px'), profile='full', debug=True)
    arrow = create_arrow_marker(dwg)
    line = dwg.line(start=(295, 50), end=(95, 75), stroke='#000', stroke_width=5,
                    marker_end=arrow.get_funciri())
    dwg.add(line)
    dwg.save(pretty=True)


def marker03(name):
    # example http://vanseodesign.com/web-design/svg-markers/
    # <svg width="600px" height="400px" class="example">
    #     <defs>
    #         <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth" viewBox="0 0 20 20">
    #           <path d="M0,0 L0,6 L9,3 z" fill="#f00" />
    #         </marker>
    #     </defs>
    #
    #     <marker id="circle" markerWidth="4" markerHeight="4" refX="2" refY="2">
    #         <circle cx="2" cy="2" r="2" stroke="none" fill="#f00"/>
    #     </marker>
    #
    #     <polyline points="50,100 250,100 250,200 350,200" fill="none" stroke="#000" stroke-width="10" marker-end="url(#arrow)" marker-start="url(#circle)" marker-mid="url(#circle)" />
    #     <path d="M50,100 l0,200 l50,0" stroke="#000" fill="none" stroke-width="10"  marker-end="url(#arrow)" marker-start="url(#circle)" marker-mid="url(#circle)" />
    #     <line x1="50" y1="100" x2="220" y2="270" stroke="#000" stroke-width="10" marker-end="url(#arrow)" marker-start="url(#circle)" marker-mid="url(#circle)"/>
    # </svg>

    dwg = svgwrite.Drawing(name, size=('600px', '400px'), profile='full', debug=True)
    arrow = create_arrow_marker(dwg)

    circle_marker = dwg.marker(id='circle', insert=(2, 2), size=(4, 4))
    circle_marker.add(dwg.circle(center=(2, 2), r=2, stroke='none', fill='#f00'))
    dwg.add(circle_marker)

    polyline = dwg.polyline(points=[(50, 100), (250, 100), (250, 200), (350, 200)], fill='none', stroke='#000', stroke_width=10)
    polyline.set_markers((circle_marker, circle_marker, arrow))  # start, mid, end
    dwg.add(polyline)

    path = dwg.path(d="M50,100 l0,200 l50,0", stroke="#000", fill="none", stroke_width=10)
    path.set_markers((circle_marker, circle_marker, arrow))  # start, mid, end
    dwg.add(path)

    line = dwg.line(start=(50, 100), end=(220, 270), stroke="#000", stroke_width=10)
    line.set_markers((circle_marker, circle_marker, arrow))  # start, mid, end
    dwg.add(line)

    dwg.save(pretty=True)


if __name__ == '__main__':
    marker01("marker01.svg")
    marker02("marker02.svg")
    marker03("marker03.svg")  # uses set_markers()
