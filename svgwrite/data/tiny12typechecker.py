from full11typechecker import Full11TypeChecker

FOCUS_CONST = frozenset(['nav-next', 'nav-prev', 'nav-up', 'nav-down', 'nav-left',
                         'nav-right', 'nav-up-left', 'nav-up-right', 'nav-down-left',
                         'nav-down-right'])

class Tiny12TypeChecker(Full11TypeChecker):
    def get_version(self):
        return ('1.2', 'tiny')

    def is_boolean(self, value):
        if isinstance(value, bool):
            return True
        if isinstance(value, basestring):
            return value.strip().lower() in ('true', 'false')
        return False

    def is_number(self, value):
        try:
            number = float(value)
            if (-32767.9999 <= number <= 32767.9999):
                return True
            else:
                return False
        except:
            return False

    def is_focus(self, value):
        return str(value).strip() in FOCUS_CONST
