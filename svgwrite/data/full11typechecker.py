def is_angle(value):
    #angle ::= number (~"deg" | ~"grad" | ~"rad")?
    return True

def is_anything(value):
    #anything ::= Char*
    return True

def is_color(value):
    #color    ::= "#" hexdigit hexdigit hexdigit (hexdigit hexdigit hexdigit)?
    #             | "rgb(" wsp* integer comma integer comma integer wsp* ")"
    #             | "rgb(" wsp* integer "%" comma integer "%" comma integer "%" wsp* ")"
    #             | color-keyword
    #hexdigit ::= [0-9A-Fa-f]
    #comma    ::= wsp* "," wsp*
    return True

def is_coordinate(value):
    #coordinate ::= length
    return is_length(value)

def is_frequency(value):
    #frequency ::= number (~"Hz" | ~"kHz")
    return True

def is_FuncIRI(value):
    #FuncIRI ::= "url(" <IRI> ")"
    return True

def is_icccolor(value):
    #icccolor ::= "icc-color(" name (comma-wsp number)+ ")"
    return True

def is_integer(value):
    #integer ::= [+-]? [0-9]+
    return True

def is_IRI(value):
    #Internationalized Resource Identifiers
    #a more generalized complement to Uniform Resource Identifiers (URIs)
    return True

def is_length(value):
    #length ::= number ("em" | "ex" | "px" | "in" | "cm" | "mm" | "pt" | "pc" | "%")?
    return True

def is_list_of_T(value, t='string'):
    def split(value):
        #TODO: improve split function!!!!
        return value.split()
    #list-of-Ts ::= T
    #               | T comma-wsp list-of-Ts
    #comma-wsp  ::= (wsp+ ","? wsp*) | ("," wsp*)
    #wsp        ::= (#x20 | #x9 | #xD | #xA)
    checker = checkfuncs[t]
    for v in split(value):
        if not checker(v):
            return False
    return True

def is_semicolon_list(value):
    #a semicolon-separated list of values
    #               | value comma-wsp list-of-values
    #comma-wsp  ::= (wsp+ ";" wsp*) | ("," wsp*)
    #wsp        ::= (#x20 | #x9 | #xD | #xA)
    return True

def is_name(value):
    #name  ::= [^,()#x20#x9#xD#xA] /* any char except ",", "(", ")" or wsp */
    return True

def is_number(value):
    #number ::= integer ([Ee] integer)?
    #           | [+-]? [0-9]* "." [0-9]+ ([Ee] integer)?
    return True

def is_number_optional_number(value):
    #number-optional-number ::= number
    #                           | number comma-wsp number
    return True

def is_paint(value):
    #paint ::=	"none" |
    #           "currentColor" |
    #           <color> [<icccolor>] |
    #           <funciri> [ "none" | "currentColor" | <color> [<icccolor>] |
    #           "inherit"
    return True

def is_percentage(value):
    #percentage ::= number "%"
    return True

def is_time(value):
    #time ::= <number> (~"ms" | ~"s")
    return True

def is_transform_list(value):
    return True

def is_XML_Name(value):
    return True

is_string = is_anything

def is_shape(value):
    #shape ::= (<top> <right> <bottom> <left>)
    # where <top>, <bottom> <right>, and <left> specify offsets from the
    # respective sides of the box.
    # <top>, <right>, <bottom>, and <left> are <length> values
    # i.e. 'rect(5px, 10px, 10px, 5px)'
    return True

checkfuncs = {
    'angle': is_angle,
    'anything': is_anything,
    'color': is_color,
    'coordinate': is_coordinate,
    'frequency': is_frequency,
    'FuncIRI': is_FuncIRI,
    'icccolor': is_icccolor,
    'interger': is_interger,
    'IRI': is_IRI,
    'length': is_length,
    'list-of-T': is_list_of_T,
    'semicolon-list': is_semicolon_list,
    'name': is_name,
    'number': is_number,
    'number-optional-number': is_number_optional_number,
    'paint': is_paint,
    'percentage': is_percentage,
    'time': is_time,
    'transform-list': is_transform_list,
    'XML-Name': is_XML_Name,
    'string': is_string,
    'shape': is_shape,
}