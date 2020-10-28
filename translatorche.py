'''
 Translates the EBIGU tokens into Python tokens
 using the token dictionary
'''

import re
from token_dict import get_token_dict

DICTIONARY = get_token_dict()


def translate(source):
    # Substitute the EBIGU tokens with the python tokens
    for token, pattern in DICTIONARY.items():
        source = re.sub(pattern, token, source)

    return source
