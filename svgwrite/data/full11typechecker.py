from svgwrite import pattern

INVALID_NAME_CHARS = frozenset([' ', '\t', '\r', '\n', ',', '(', ')'])
WHITESPACE = frozenset([' ', '\t', '\r', '\n'])

class Full11TypeChecker(object):
    @staticmethod
    def is_angle(value):
        #angle ::= number (~"deg" | ~"grad" | ~"rad")?
        return True

    @staticmethod
    def is_anything(value):
        #anything ::= Char*
        return True

    @staticmethod
    def is_color(value):
        #color    ::= "#" hexdigit hexdigit hexdigit (hexdigit hexdigit hexdigit)?
        #             | "rgb(" wsp* integer comma integer comma integer wsp* ")"
        #             | "rgb(" wsp* integer "%" comma integer "%" comma integer "%" wsp* ")"
        #             | color-keyword
        #hexdigit ::= [0-9A-Fa-f]
        #comma    ::= wsp* "," wsp*
        return True

    @staticmethod
    def is_frequency(value):
        #frequency ::= number (~"Hz" | ~"kHz")
        return True

    @staticmethod
    def is_FuncIRI(value):
        #FuncIRI ::= "url(" <IRI> ")"
        return True
    @staticmethod
    def is_icccolor(value):
        #icccolor ::= "icc-color(" name (comma-wsp number)+ ")"
        return True
    @staticmethod
    def is_integer(value):
        #integer ::= [+-]? [0-9]+
        return True

    @staticmethod
    def is_IRI(value):
        #Internationalized Resource Identifiers
        #a more generalized complement to Uniform Resource Identifiers (URIs)
        return True

    @staticmethod
    def is_length(value):
        #length ::= number ("em" | "ex" | "px" | "in" | "cm" | "mm" | "pt" | "pc" | "%")?
        return True
    is_coordinate = is_length

    @staticmethod
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

    @staticmethod
    def is_semicolon_list(value):
        #a semicolon-separated list of values
        #               | value comma-wsp list-of-values
        #comma-wsp  ::= (wsp+ ";" wsp*) | ("," wsp*)
        #wsp        ::= (#x20 | #x9 | #xD | #xA)
        return True

    @staticmethod
    def is_name(value):
        #name  ::= [^,()#x20#x9#xD#xA] /* any char except ",", "(", ")" or wsp */
        if not isinstance(value, basestring):
            return False
        name = frozenset(value)
        if name.isdisjoint(INVALID_NAME_CHARS):
            return True
        return False

    @staticmethod
    def is_number(value):
        try:
            number = float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_number_optional_number(value):
        #number-optional-number ::= number
        #                           | number comma-wsp number
        return True

    @staticmethod
    def is_paint(value):
        #paint ::=	"none" |
        #           "currentColor" |
        #           <color> [<icccolor>] |
        #           <funciri> [ "none" | "currentColor" | <color> [<icccolor>] |
        #           "inherit"
        return True

    @staticmethod
    def is_percentage(value):
        #percentage ::= number "%"
        return True

    @staticmethod
    def is_time(value):
        #time ::= <number> (~"ms" | ~"s")?
        return True

    @staticmethod
    def is_transform_list(value):
        return True

    @staticmethod
    def is_XML_Name(value):
        return True

    is_string = is_anything
    @staticmethod
    def is_shape(value):
        #shape ::= (<top> <right> <bottom> <left>)
        # where <top>, <bottom> <right>, and <left> specify offsets from the
        # respective sides of the box.
        # <top>, <right>, <bottom>, and <left> are <length> values
        # i.e. 'rect(5px, 10px, 10px, 5px)'
        return True

    def get_func_by_name(self, funcname):
        return getattr(self, funcname, self.is_anything)
