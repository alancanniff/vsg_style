from vsg.rules import remove_spaces_before_token_rule
from vsg.token import function_specification as token


class rule_005(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the function name and the (
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '005', token.open_parenthesis)
        self.solution = 'Ensure no space exists between function name and the ('
