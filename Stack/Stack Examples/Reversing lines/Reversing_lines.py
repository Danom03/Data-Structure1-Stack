from Stack.Stack_Class import *


def reverse_lines(filename):
    """Reverses file line by line"""
    S = Stack()                             # Creating Empty Stack
    original = open(filename, 'r')          # Opening file in read only mode
    for line in original:
        S.push(line.rstrip('\n'))           # New line is added later
    original.close()

    reverse = open('reverse', 'w')          # Opening reverse file in write only mode
    while not S.is_empty():
        reverse.write(S.pop() + '\n')       # Adding new line
    reverse.close()


reverse_lines('All I want')
