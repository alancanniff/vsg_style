from vsg import token
from vsg.rules import remove_spaces_before_token_rule


class rule_006(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the variable declaration and :
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '006', token.variable_declaration.colon)
        self.solution = 'Ensure no space exists between variable declaration and :'
