'''
 What does the parser do?
'''

import re
# import functions
from func_dict import get_funcs_list

FUNCS_LIST = get_funcs_list()


def parse(source):
    # !The context though...
    for func in FUNCS_LIST:
        for func_found in re.finditer(func['pattern'], source):
            args = func_found.groupdict()
            # XXX for debugging purposes
            print(f'EBIGU function found: {func_found.group()} (args: {args})')
            py_code = func['func'](**args)
            source = re.sub(re.escape(func_found.group()), py_code, source)

    return source
