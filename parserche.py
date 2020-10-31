'''
Parsing the EBIGU code
aka replacing the EBIGU actions
with python code
'''

import re
from func_list import get_func_list

FUNC_LIST = get_func_list()


def parse(source):
    funcs_found = ''

    # Removing all comments
    source = re.sub(r'(?<=\n)\s*#.*\n', '', source)

    # Going through all the EBIGU action patterns
    # and replacing them with python equivalents
    for func in FUNC_LIST:
        '''
        Checking if run twice is needed for the function
        This is because when a function has to get the tabs before
        it also gets the \n and so if there is the same EBIGU action
        doesn't have a \n in the front and it does not recongnize it
        tried to fix it with regex look-before and look-ahead
        but it didn't work, so this is my temporary solution
        '''
        run_times = 1
        if 'run_twice' in func.keys():
            run_times = 2
        for i in range(run_times):
            for func_found in re.finditer(func['pattern'], source):
                args = func_found.groupdict()
                # XXX for debugging purposes
                funcs_found += f'EBIGU function found: {func_found.group()} (args: {args})\n'
                py_code = func['func'](**args)
                source = re.sub(re.escape(func_found.group()), py_code, source)

    return source, funcs_found
