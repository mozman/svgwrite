def is_Clock_value(value):
    #return False if value if not valid
    return True

def is_ID(value):
    #return False if value if not valid
    return True

def is_IDREF(value):
    #return False if value if not valid
    return True

def is_IRI(value):
    #return False if value if not valid
    return True

def is_NCName(value):
    #return False if value if not valid
    return True

def is_QName(value):
    #return False if value if not valid
    return True

def is_XML_NMTOKEN(value):
    #return False if value if not valid
    return True

def is_XML_NMTOKENS(value):
    #return False if value if not valid
    return True

def is_boolean(value):
    #return False if value if not valid
    return True

def is_color(value):
    #return False if value if not valid
    return True

def is_content_type(value):
    #return False if value if not valid
    return True

def is_coordinate(value):
    #return False if value if not valid
    return True

def is_focus(value):
    #return False if value if not valid
    return True

def is_font_family_value(value):
    #return False if value if not valid
    return True

def is_font_size_value(value):
    #return False if value if not valid
    return True

def is_language_id(value):
    #return False if value if not valid
    return True

def is_length(value):
    #return False if value if not valid
    return True

def is_list_of_IRIs(value):
    #return False if value if not valid
    return True

def is_list_of_content_types(value):
    #return False if value if not valid
    return True

def is_list_of_coordinates(value):
    #return False if value if not valid
    return True

def is_list_of_family_names(value):
    #return False if value if not valid
    return True

def is_list_of_language_ids(value):
    #return False if value if not valid
    return True

def is_list_of_lengths(value):
    #return False if value if not valid
    return True

def is_list_of_numbers(value):
    #return False if value if not valid
    return True

def is_list_of_strings(value):
    #return False if value if not valid
    return True

def is_number(value):
    #return False if value if not valid
    return True

def is_paint(value):
    #return False if value if not valid
    return True

def is_path_data(value):
    #return False if value if not valid
    return True

def is_points_data(value):
    #return False if value if not valid
    return True

def is_string(value):
    #return False if value if not valid
    return True

def is_text(value):
    #return False if value if not valid
    return True

def is_transform(value):
    #return False if value if not valid
    return True

checkfuncs = {
    'Clock_value': is_Clock_value,
    'ID': is_ID,
    'IDREF': is_IDREF,
    'IRI': is_IRI,
    'NCName': is_NCName,
    'QName': is_QName,
    'XML_NMTOKEN': is_XML_NMTOKEN,
    'XML_NMTOKENS': is_XML_NMTOKENS,
    'boolean': is_boolean,
    'color': is_color,
    'content_type': is_content_type,
    'coordinate': is_coordinate,
    'focus': is_focus,
    'font_family_value': is_font_family_value,
    'font_size_value': is_font_size_value,
    'language_id': is_language_id,
    'length': is_length,
    'list_of_IRIs': is_list_of_IRIs,
    'list_of_content_types': is_list_of_content_types,
    'list_of_coordinates': is_list_of_coordinates,
    'list_of_family_names': is_list_of_family_names,
    'list_of_language_ids': is_list_of_language_ids,
    'list_of_lengths': is_list_of_lengths,
    'list_of_numbers': is_list_of_numbers,
    'list_of_strings': is_list_of_strings,
    'number': is_number,
    'paint': is_paint,
    'path_data': is_path_data,
    'points_data': is_points_data,
    'string': is_string,
    'text': is_text,
    'transform': is_transform,
}