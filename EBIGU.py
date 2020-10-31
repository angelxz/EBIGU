import sys
import traceback
from translatorche import translate
from parserche import parse

# TODO print doesn't work when you have initiated pygame in EBIGU (and you don't have errors)...

# Importing some modules so that when the interpreter is compiled to exe
# they are packed as well
import pygame
import pygame.locals
import random
import os
import re

if __name__ == '__main__':
    # Spit an error if no EBIGU scrupt is supplied
    if len(sys.argv) < 2:
        print('Please suppy an EBIGU script to interpret!')
        input()
    else:
        # Opening the file from the argument supplied
        with open(sys.argv[1], 'r') as f:
            # Save the source code as string
            source = f.read()

        # Parse the source code
        source, funcs_found = parse(source)

        # Translate the source code
        source = translate(source)

        if len(sys.argv) > 2:
            # Write the python code to file if such file is specified
            with open(sys.argv[2], 'w') as f:
                f.write(source)
                os._exit(1)
        else:
            # Execute the result
            try:
                exec(source)
            except:
                print('------------ FUNCS FOUND --------------')
                print(funcs_found)
                print('------------ TRANSLATION --------------')
                source_lines = source.splitlines()
                for line in range(len(source_lines)):
                    print(f'{line + 1}: {source_lines[line]}')
                print('------------ END --------------')
                print(traceback.format_exc())

        # Keep console open if no pygame or error
        input()
