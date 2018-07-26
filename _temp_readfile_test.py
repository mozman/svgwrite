import svgwrite

dwg = svgwrite.Drawing ("file.svg")

svgwrite.OpenSVGFile ("test_file.svg", dwg)

dwg.save ()
