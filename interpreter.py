import sys
from translatorche import translate
from parserche import parse

# Importing pygame so that when the interpreter is compiled to exe
# the pygame module is also in the package
import pygame

if __name__ == '__main__':
    if not sys.argv[1]:
        print('Please suppy an EBIGU script to interpret!')
        input()

    # Opening the file from the argument supplied
    with open(sys.argv[1], 'r') as f:
        # Save the source code as string
        source = f.read()

    # XXX for debugging purposes
    print('------------ SOURCE --------------')
    print(source)

    # Parse the source code
    source = parse(source)

    # Translate the source code
    source = translate(source)

    # XXX for debugging purposes
    print('------------ TRANSLATION --------------')
    print(source)

    # XXX for debugging purposes
    print('------------ RESULT --------------')
    # Execute the result
    exec(source)

    # Keep console open (this should be true only if pygame has not been initiated) TODO
    input()
