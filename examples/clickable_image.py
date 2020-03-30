#!/usr/bin/env python3

import svgwrite

MAX_PIXELS = 1000


def clickable_image(dwg, image_href, dest_href, insert=None, size=None):
    insert = insert or ("0%", "0%")
    size = size or ("100%", "100%")
    dwg.add(dwg.a(href=dest_href)).add(dwg.image(image_href, insert=insert, size=size))


def make_drawing(filename="clickable_image.svg"):
    dwg = svgwrite.Drawing(filename, size=(MAX_PIXELS, MAX_PIXELS))
    dwg.viewbox(0, 0, MAX_PIXELS, MAX_PIXELS)
    dwg.add(dwg.rect(size=('100%', '100%'), fill="lightgrey", class_='background'))

    clickable_image(dwg,
                    image_href="https://github.com/fluidicon.png",
                    dest_href="https://github.com/mozman/svgwrite",
                    insert=("25%", "25%"), size=("50%", "50%"))

    return dwg


make_drawing().save(pretty=True)
