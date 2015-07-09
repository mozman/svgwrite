try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
dwg = svgwrite.Drawing("fePointLight.svg")

filtr = dwg.defs.add(
    dwg.filter(id="DL", start=(0, 0), size=(500, 500),
               filterUnits="userSpaceOnUse"))
diffuse_lighting = filtr.feDiffuseLighting(
    start=(0, 0), size=(500, 500),
    surfaceScale=10,
    diffuseConstant=1,
    kernelUnitLength=1,
    lighting_color="#f8f")
point_light = diffuse_lighting.fePointLight( (500, 250, 250) )
point_light.add(
    dwg.animate('x',
        values=(0,100,500,100,0),
        dur='30s',
        repeatDur='indefinite'))
point_light.add(
    dwg.animate('y',
        values=(0,500,400,-100,0),
        dur='31s',
        repeatDur='indefinite'))
point_light.add(
    dwg.animate('z',
        values=(0,1000,500,-100,0),
        dur='37s',
        repeatDur='indefinite'))
dwg.save()
