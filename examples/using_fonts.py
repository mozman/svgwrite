import svgwrite


def write_html_loader(name, title):
    open('{name}.html'.format(name=name), 'wt', encoding='utf-8').write("""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>title</title>
    </head>
    <body>
        <image src="{name}.svg"/>
    </body>
    </html>
    """.format(name=name, title=title))


def font_by_stylsheet(name):
    dwg = svgwrite.Drawing(name+'.svg', (800, 200), debug=True)
    # load web font by CSS @import
    dwg.embed_stylesheet("""
    @import url(http://fonts.googleapis.com/css?family=Indie+Flower);
    .flower14 {
        font-family: "Indie Flower";
        font-size: 14;
    }
    """)
    paragraph = dwg.add(dwg.g(class_="flower14", ))
    paragraph.add(dwg.text("Font 'Indie Flower' referenced by embedded CSS stylesheet.", insert=(10, 40)))
    dwg.save(pretty=True)
    # This seems easy, BUT this only works if the SVG file is opened stand alone,
    # embedded in a website, this approach does not work!
    write_html_loader(name, title="Test font for SVG by CSS reference inside of HTML")


def font_embedded(name):
    dwg = svgwrite.Drawing(name+'.svg', (800, 200), debug=True)
    # font data has to be downloaded to the local file system
    dwg.embed_font(name="Indie Flower", filename='fonts/IndieFlower.ttf')
    dwg.embed_stylesheet("""
    .flower14 {
        font-family: "Indie Flower";
        font-size: 14;
    }
    """)
    # This should work stand alone and embedded in a website!
    paragraph = dwg.add(dwg.g(class_="flower14", ))
    paragraph.add(dwg.text("Font 'Indie Flower' embedded from local file system.", insert=(10, 40)))
    dwg.save(pretty=True)
    write_html_loader(name, title="Test SVG with embedded font inside of HTML")


def web_font_embedded(name):
    dwg = svgwrite.Drawing(name+'.svg', (800, 200), debug=True)
    # font data downloaded from google fonts
    dwg.embed_google_web_font(name="Indie Flower", uri='http://fonts.googleapis.com/css?family=Indie+Flower')
    dwg.embed_stylesheet("""
    .flower14 {
        font-family: "Indie Flower";
        font-size: 14;
    }
    """)
    # This should work stand alone and embedded in a website!
    paragraph = dwg.add(dwg.g(class_="flower14", ))
    paragraph.add(dwg.text("Font 'Indie Flower' embedded from Google fonts.", insert=(10, 40)))
    dwg.save(pretty=True)
    write_html_loader(name, title="Test SVG with embedded font inside of HTML")


if __name__ == '__main__':
    font_by_stylsheet("font_by_CSS_reference")
    font_embedded("font_embedded")
    web_font_embedded("font_embedded_from_google")
