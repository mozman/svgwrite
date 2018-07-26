import svgwrite

dwg = svgwrite.Drawing ("duplicated_file.svg")

svgwrite.OpenSVGFile ("input_file.svg", dwg)

dwg.save ()
