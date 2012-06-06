import svgwrite
#
#
progname = 'test_circle_blur'


def create_svg(name):
    svg_size = 900
    font_size = 20
    y = 0
    title = name + ': Test to see if feGaussianBlur filter can be used.'
    dwg = svgwrite.Drawing(name, (svg_size, svg_size), debug=True)
    myfilter = dwg.defs.add( dwg.filter(id="myfilter", filterUnits="userSpaceOnUse"))
    newfilter = myfilter.feGaussianBlur(
        in_='SourceGraphic',
        stdDeviation =2)
    defs_g_text = dwg.defs.add(dwg.g(id='defs_g_text'))
    defs_g_text.add(dwg.text("SVGWRITE", insert=(0, 0), font_family="serif", font_size=font_size))
    # background will be white.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='white'))
    # give the name of the example and a title.
    y = font_size + 5
    dwg.add(dwg.text(title, insert=(0, y),
            font_family="serif", font_size=font_size, fill='black'))
    y = y +50
    circle_1 = dwg.circle(center=(100, y), r=30)
    circle_1.fill('green', opacity=0.5).stroke('black', width=5).scale([2,2])
    dwg.add(circle_1)
    y = y + 30
    circle_2 = dwg.circle(center=(100, y), r=30)
    circle_2.fill('green', opacity=0.5).stroke('black', width=5).scale([2,2])
    circle_2.filter('url(#myfilter)')
    dwg.add(circle_2)
    dwg.save()

if __name__ == '__main__':
    create_svg(progname + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
