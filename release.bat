@ECHO OFF
ECHO Upload to PyPI - NO TEST
PAUSE
twine upload --repository pypi dist/svgwrite*
mv -f dist/svgwrite* dist/archiv