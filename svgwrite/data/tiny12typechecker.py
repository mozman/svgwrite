from full11typechecker import Full11TypeChecker

FOCUS_CONST = frozenset(['nav-next', 'nav-prev', 'nav-up', 'nav-down', 'nav-left',
                         'nav-right', 'nav-up-left', 'nav-up-right', 'nav-down-left',
                         'nav-down-right'])
class Tiny12TypeChecker(Full11TypeChecker):
    @staticmethod
    def is_boolean(value):
        if isinstance(value, bool):
            return True
        if isinstance(value, basestring):
            return value in ('true','false')
        return False

    @staticmethod
    def is_number(value):
        try:
            number = float(value)
            if not (-32767.9999 <= number <= 32767.9999):
                return False
        except ValueError:
            pass
        return True

    @staticmethod
    def is_focus(value):
        return value in FOCUS_CONST
