import svgwrite

size_drawing_h = 297
size_drawing_w = 210

dwg = svgwrite.Drawing('test.svg',
                       size=(size_drawing_w, size_drawing_h),
                       profile='tiny',
                       debug=True,
                       viewBox=('%f %f %f %f' % (-size_drawing_w/2, -size_drawing_h/2, size_drawing_w, size_drawing_h)))

dwg.add(dwg.textArea(text='Modena City Ramblers', insert=(0, 0), size=(50, 50)))

dwg.save()
