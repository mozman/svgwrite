@ECHO OFF
ECHO TEST TEST TEST - upload to TestPyPI - TEST TEST TEST
twine upload --repository testpypi dist/svgwrite*
mv -f dist/svgwrite* dist/archiv