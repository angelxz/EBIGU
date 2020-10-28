'''
The dictionary of tokens with their EBIGU equivalent regex pattern
python token -> EBIGU token in regex pattern
'''

import re


def get_token_dict():
    token_dict = {
        '==': re.compile(r'\be\b'),
        '!=': re.compile(r'\bne e\b'),
        'in': re.compile(r'\bv\b'),
        'and': re.compile(r'\bi\b'),
        'or': re.compile(r'\bili\b'),
        'if': re.compile(r'\bako\b'),
        'while': re.compile(r'\bdokato\b'),
        'for': re.compile(r'\bza\b'),
        'def': re.compile(r'\bkato izvikam\b'),
        'return': re.compile(r'\bvurni\b'),
        'break': re.compile(r'\bprekrati\b'),
        'continue': re.compile(r'\bpreskochi\b'),
        'True': re.compile(r'\bvqrno\b'),
        'False': re.compile(r'\bgreshno\b'),
        'print': re.compile(r'\bizpishi\b'),
        'range': re.compile(r'\bobseg\b'),
    }

    return token_dict
