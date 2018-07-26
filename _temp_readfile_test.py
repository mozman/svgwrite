import svgwrite.readfile as rf
import svgwrite

dwg = svgwrite.Drawing ("file.svg")

rf.OpenSVGFile ("test_file.svg", dwg)

dwg.save ()
