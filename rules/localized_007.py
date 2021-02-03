from vsg import token
from vsg.rules import remove_spaces_before_token_rule

class rule_007(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the interface / parameter signal declaration and :
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '007', token.interface_signal_declaration.colon)
        self.solution = 'Ensure no space exists between interface / parameter signal declaration and :'
