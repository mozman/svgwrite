#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test style element
# Created: 27.05.2012
# Copyright (C) 2012, Manfred Moitzi
# License: MIT License

import unittest

from svgwrite.container import Style, find_first_url
from svgwrite.drawing import Drawing

TEST_URL_1 = """/* latin */
@font-face {
  font-family: 'Indie Flower';
  font-style: normal;
  font-weight: 400;
  src: local('Indie Flower'), local('IndieFlower'), url(https://fonts.gstatic.com/s/indieflower/v9/m8JVjfNVeKWVnh3QMuKkFcZVaUuH.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}"""

TEST_URL_2 = """/* latin */
@font-face {
  font-family: 'Indie Flower';
  font-style: normal;
  font-weight: 400;
  src: local('Indie Flower'), local('IndieFlower'), url(https://fonts.gstatic.com/s/indieflower/v9/m8JVjfNVeKWVnh3QMuKkFcZVaUuH.woff2) format('woff2');
  url(https://fonts.gstatic.com/s/indieflower/v9/m8JVjfNVeKWVnh3QMuKkFcZVaUuH.woff) format('woff');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}"""


class TestScript(unittest.TestCase):
    def test_content(self):
        style = Style(content='.red {fill: red};')
        result = style.tostring()
        self.assertEqual(result, '<style type="text/css"><![CDATA[.red {fill: red};]]></style>')

    def test_embed_stylesheet(self):
        dwg = Drawing()
        dwg.embed_stylesheet(content='.red {fill: red};')
        # stylesheet stored as <style> tag in first <defs> entity
        style = dwg.defs.elements[0]
        self.assertEqual(style.elementname, 'style')
        result = style.tostring()
        self.assertEqual(result, '<style type="text/css"><![CDATA[.red {fill: red};]]></style>')

    def test_find_first_url_1(self):
        result = find_first_url(TEST_URL_1)
        self.assertEqual(result, "https://fonts.gstatic.com/s/indieflower/v9/m8JVjfNVeKWVnh3QMuKkFcZVaUuH.woff2")

    def test_find_first_url_2(self):
        result = find_first_url(TEST_URL_2)
        self.assertEqual(result, "https://fonts.gstatic.com/s/indieflower/v9/m8JVjfNVeKWVnh3QMuKkFcZVaUuH.woff2")

    def test_embed_google_web_font(self):
        dwg = Drawing()
        dwg.embed_google_web_font(name="Indie Flower", uri="http://fonts.googleapis.com/css?family=Indie+Flower")
        style = dwg.defs.elements[0]
        self.assertEqual(style.elementname, 'style')
