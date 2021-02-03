from vsg.rules import remove_spaces_before_token_rule
from vsg.token import loop_statement as token


class rule_004(remove_spaces_before_token_rule):
    '''
    Check there are no spaces betwen the for loop label and :
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'localized', '004', token.label_colon)
        self.solution = 'Ensure no space exists between for loop label and :'
