#!/usr/bin/env python
#coding:utf-8
# Author:  kneasle --<kneasle@gmail.com>
# Purpose: allow svgwrite to read .svg files
# Created: 29.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

import xml.dom.minidom as minidom
from .drawing import *
from .validator2 import *

def GetAttributeDictionary (node):
    attrs = node.attributes
    
    attributes = {}
    for i in range (attrs.length):
        attribute = attrs.item (i)
        if ":" not in attribute.name:
            attributes [attribute.name] = attribute.value

    return attributes

def GetChildNodesByLocalName (node, local_name):
    """
    :param Node node: node whose children to search
    :param string local_name: the local_name to search for
    :returns list: list of nodes
    """
    children = []
    for n in node.childNodes:
        if n.localName == local_name:
            children.append (n)
    
    return children

def GetFirstChildNodeByLocalName (node, local_name):
    """
    :param Node node: node whose children to search
    :param string local_name: the local_name to search for
    """
    for n in node.childNodes:
        if n.localName == local_name:
            return n
    
    return None

def GetDrawingFromString (string, dwg, overwrite_dwg_properties = True,
                          parent = None, unpack_style = False):
    """
    :param string string: file string in xml
    :param Drawing dwg: drawing to add elements to
    :param 2-tuple offset: translation to be applied to all elements (dx, dy)
    :param SVG parent: SVG element to add all elements to (if None, will default to the drawing)
    """
    if parent is None:
        parent = dwg

    xml_tree = minidom.parseString (string)

    svg_node = GetFirstChildNodeByLocalName (xml_tree, "svg")
    
    if overwrite_dwg_properties:
        attr_dict = GetAttributeDictionary (svg_node)

        dwg ["width"] = float (attr_dict ["width"])
        dwg ["height"] = float (attr_dict ["height"])
        dwg ["viewBox"] = attr_dict ["viewBox"]

    element_to_function = {
        "line": dwg.line, "rect": dwg.rect, "circle": dwg.text,
        "ellipse": dwg.ellipse, "polyline": dwg.polyline,
        "polygon": dwg.polygon, "text": dwg.text, "tspan": dwg.tspan,
        "tref": dwg.tref, "textPath": dwg.textPath, "textArea": dwg.textArea,
        "path": dwg.path, "image": dwg.path, "g": dwg.g, "symbol": dwg.symbol,
        "svg": dwg.svg, "use": dwg.use, "a": dwg.a, "marker": dwg.marker,
        "script": dwg.script, "style": dwg.style,
        "linearGradient": dwg.linearGradient,
        "radialGradient": dwg.radialGradient,
        "mask": dwg.mask, "clipPath": dwg.clipPath, "set": dwg.set,
        "animate": dwg.animate, "animateColor": dwg.animateColor,
        "animateMotion": dwg.animateMotion,
        "animateTransform": dwg.animateTransform, "filter": dwg.filter
    }

    text_elements = ["text", "tspan", "textPath", "textArea"]

    # Set up recursive function
    def AddNodeFromXMLNode (node, parent):
        # Ignore text nodes (they break everything)
        if type (node) == minidom.Text:
            return

        # Reject extra / meta nodes
        if node.nodeName not in element_to_function.keys ():
            return
        
        attributes = GetAttributeDictionary (node)

        # add text attribute if necessary
        if node.nodeName in text_elements:
            text = ""
            for n in node.childNodes:
                if type (n) is minidom.Text:
                    text = n.nodeValue
            
            attributes ["text"] = text

        # unpack style attributes
        if unpack_style and "style" in attributes.keys ():
            validator = Full11Validator ()
            
            for i in attributes ["style"].split (";"):
                i = i.strip ()

                name, value = i.split (":")

                name = name.strip ()
                value = value.strip ()

                if validator.is_valid_svg_attribute (node.nodeName, name):
                    attributes [name] = value

            del attributes ["style"]

        # correct for "insert" arguments
        if node.nodeName in ["text", "tspan"]:
            attributes ["insert"] = (
                float (attributes ["x"]),
                float (attributes ["y"])
            )

            del attributes ["x"]
            del attributes ["y"]
        
        # create and add element
        element = element_to_function [node.nodeName] (**attributes)
        
        parent.add (element)

        # recur through children
        for n in node.childNodes:
            AddNodeFromXMLNode (n, element)

    for n in svg_node.childNodes:
        AddNodeFromXMLNode (n, parent)

def OpenSVGFile (file_path, dwg, offset = (0, 0), parent = None):
    """
    :param string file_path: file path to open
    :param Drawing dwg: drawing to add elements to
    :param 2-tuple offset: translation to be applied to all elements (dx, dy)
    :param SVG parent: SVG element to add all elements to (if None, will default to the drawing)
    
    """
    return GetDrawingFromString (open (file_path, "r").read (), dwg)
