#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test Description mixin
# Created: 04.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import unittest
import xml.etree.ElementTree as etree

from svgwrite.base  import BaseElement

class Mock(BaseElement):
    elementname = 'g'

class TestDescription(unittest.TestCase):
    def test_title(self):
        m = Mock()
        m.set_desc(title="TEST")
        self.assertEqual(m.tostring(), '<g><title>TEST</title></g>')

    def test_desc(self):
        m = Mock()
        m.set_desc(desc="TEST")
        self.assertEqual(m.tostring(), '<g><desc>TEST</desc></g>')

    def test_insert(self):
        # insert 'desc# and 'title' always as first subelement
        m = Mock()
        m.add(Mock()) # inner 'g'
        m.set_desc(desc="TEST")
        self.assertEqual(m.tostring(), '<g><desc>TEST</desc><g /></g>')
        m.set_desc("TITLE")
        self.assertEqual(m.tostring(), '<g><title>TITLE</title><desc>TEST</desc><g /></g>')

def get_test_data():
    rdf = etree.Element('rdf:RDF', attrib={'xmlns:rdf': 'http://test/rdf'})
    rdf.append(etree.Element('rdf:Description'))
    return rdf

class TestMetaData(unittest.TestCase):
    def test_metadata_only(self):
        m = Mock()
        m.set_metadata(get_test_data())
        self.assertEqual(m.tostring(), '<g><metadata><rdf:RDF xmlns:rdf="http://test/rdf">' \
                         '<rdf:Description /></rdf:RDF></metadata></g>')

    def test_metadata_insert_after_title(self):
        m = Mock()
        m.set_desc('TITLE')
        m.set_metadata(get_test_data())
        self.assertEqual(m.tostring(), '<g><title>TITLE</title><metadata>'\
                         '<rdf:RDF xmlns:rdf="http://test/rdf"><rdf:Description />'\
                         '</rdf:RDF></metadata></g>')

    def test_metadata_insert_before_others(self):
        m = Mock()
        m.add(Mock())
        m.add(Mock())
        m.set_metadata(get_test_data())
        self.assertEqual(m.tostring(), '<g><metadata><rdf:RDF xmlns:rdf="http://test/rdf">'\
                         '<rdf:Description /></rdf:RDF></metadata><g /><g /></g>')

    def test_metadata_insert_between_title_and_g(self):
        m = Mock()
        m.add(Mock())
        m.add(Mock())
        m.set_desc('TITLE', 'DESC')
        m.set_metadata(get_test_data())
        self.assertEqual(m.tostring(), '<g><title>TITLE</title><desc>DESC</desc>' \
                         '<metadata><rdf:RDF xmlns:rdf="http://test/rdf"><rdf:Description /></rdf:RDF>'\
                         '</metadata><g /><g /></g>')


if __name__=='__main__':
    unittest.main()
