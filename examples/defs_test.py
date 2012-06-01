import svgwrite

PROGNAME = 'defs_test'
STYLESHEET = PROGNAME + '.css'

STYLES = """.red { fill: red; stroke=none; }
.green { fill: green; stroke: none; }
.blue { fill: blue; stroke: yellow; stroke-width: 5; }
.yellow { fill: yellow; stroke: none; }
.text { font-family: serif; fill: white; }
"""

def create_svg(name):
    svg_size_width = 900
    svg_size_height = 900
    font_size = 20
    triangle_size = 50
    title1 = name + ': Example of creating your own colors and defs/use.'
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)
    # To separate structure from visual presentation, better use stylesheets
    # inline stylesheets requires svgwrite version >= 1.0.1
    # available at http://bitbucket.org/mozman/svgwrite
    if svgwrite.version >= (1, 0, 1):
        dwg.defs.add(dwg.style(STYLES))
    else: # or use an external stylesheet
        with open(STYLESHEET, 'w') as f:
            f.write(STYLES)
        dwg.add_stylesheet(STYLESHEET, 'noname')

    # Background will be dark but not black so the background does not overwhelm the colors.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='grey'))

    # http://www.w3.org/TR/SVG11/struct.html#Head
    # "sometimes it is desired to define a graphical object and prevent it from being directly
    # rendered. it is only there to be referenced elsewhere. To do this, and to allow convenient
    # grouping defined content, SVG provides the 'defs' element."

    # 1. create template polygons
    half_size = triangle_size / 2
    points = [
        (-half_size, -half_size),
        (half_size, -half_size),
        (0, triangle_size * 0.433013)
    ]

    # 2. create the symbol
    symbol_without_fill = dwg.symbol(id='symbol_without_fill')

    # 3. add symbols to the defs section
    dwg.defs.add(symbol_without_fill)

    # 4. important: define viewbox of the symbol!
    symbol_without_fill.viewbox(-half_size, -half_size, triangle_size, triangle_size)

    # and define how the symbol should behave on resizing by <use>
    # default parameters for fit(horiz="center", vert="middle", scale="meet")
    # seems not necessary
    # symbol_without_fill.fit()

    # 5. add triangles to the symbol containers
    symbol_without_fill.add(dwg.polygon(points))

    # 6. use symbols - param size is necessary - and only unset params can be overwritten
    dwg.add(dwg.use(symbol_without_fill, insert=(200, 200), size=(triangle_size, triangle_size), class_='yellow'))
    dwg.add(dwg.use(symbol_without_fill, insert=(300, 300), size=(triangle_size*1.2, triangle_size*1.2), class_ ='red'))
    dwg.add(dwg.use(symbol_without_fill, insert=(400, 400), size=(triangle_size*0.5, triangle_size*0.5), class_ ='blue'))

    # Give the name of the example and a title.
    y = font_size + 5
    dwg.add(dwg.text(title1, insert=(0, y), class_='text', font_size=font_size))
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99


