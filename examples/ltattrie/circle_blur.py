import sys
import svgwrite

PROGNAME = sys.argv[0].rstrip('.py')

def create_svg(name):
    SVG_SIZE = 900
    FONT_SIZE = 20

    title = name + ': Test to see if feGaussianBlur filter can be used.'
    dwg = svgwrite.Drawing(name, (SVG_SIZE, SVG_SIZE), debug=True)

    #myfilter = dwg.defs.add(dwg.filter(id="myfilter", filterUnits="userSpaceOnUse"))
    myfilter = dwg.defs.add(dwg.filter()) # the short way, using auto ids
    myfilter.feGaussianBlur(in_='SourceGraphic', stdDeviation=2)

    defs_g_text = dwg.defs.add(dwg.g(id='defs_g_text'))
    defs_g_text.add(dwg.text("SVGWRITE", insert=(0, 0), font_family="serif", font_size=FONT_SIZE))

    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))

    # give the name of the example and a title.
    y = FONT_SIZE + 5
    dwg.add(dwg.text(title, insert=(0, y),
            font_family="serif", font_size=FONT_SIZE, fill='black'))

    y += 50
    circle_1 = dwg.circle(center=(100, y), r=30)
    circle_1.fill('green', opacity=0.5).stroke('black', width=5).scale([2,2])
    dwg.add(circle_1)

    # setting the filter attribute
    # at the constructor by filter=myfilter.get_funciri()
    # get_funciri() returns the string 'url(#myfilter)' for id='myfilter'
    y += 30
    circle_2 = dwg.circle(center=(100, y), r=30, filter=myfilter.get_funciri())
    circle_2.fill('green', opacity=0.5).stroke('black', width=5).scale([2,2])

    # or by setting the 'filter' attribute of the circle_2 object
    # HINT: all svg attributes can be set by this way, but you have to use
    # the REAL svg-attribute-name like: 'font-size' or 'class'
    circle_2['filter'] = myfilter.get_funciri()
    dwg.add(circle_2)
    dwg.save()

if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
