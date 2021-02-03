from vsg import token
from vsg.rules import remove_spaces_before_token_rule

class rule_009(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the interface / parameter constant declaration and :
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '009', token.interface_constant_declaration.colon)
        self.solution = 'Ensure no space exists between interface / parameter constant declaration and :'
