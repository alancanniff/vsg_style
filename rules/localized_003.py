from vsg import token
from vsg.rules import remove_spaces_before_token_rule


class rule_003(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the constant declaration and :
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '003', token.constant_declaration.colon)
        self.solution = 'Ensure no space exists between constant declaration and :'
