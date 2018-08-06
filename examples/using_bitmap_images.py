# example by https://github.com/stevenj to include bitmapgraphic by using the wand and base64 libraries
# getting wand at: https://pypi.org/project/Wand/
# requirements and installation: http://docs.wand-py.org/en/0.4.4/#
# not tested by myself (mozman)

import svgwrite
import base64
from wand.image import Image

# Load PNG Image
dwg = svgwrite.Drawing()
img = Image(filename="my.png")

# Then get raw PNG data and encode DIRECTLY into the SVG file.
image_data = img.make_blob(format='png')
encoded = base64.b64encode(image_data).decode()
pngdata = 'data:image/png;base64,{}'.format(encoded)

image = dwg.add(dwg.image(href=(pngdata)))

# Bonus, the wand library lets you use ANY format image and encode it as a PNG
# You can also do cropping, transforms, etc on the image before encoding it.
# You can also embed an SVG inside an SVG the same way:

# Load SVG Image
img = Image(filename="my.svg")

# Then get raw SVG data and encode DIRECTLY into the SVG file.
image_data = img.make_blob()  # Don't change its format, just use it as an SVG
encoded = base64.b64encode(image_data).decode()
svgdata = 'data:image/svg+xml;base64,{}'.format(encoded)

image = dwg.add(dwg.image(href=(svgdata)))
