from Stack.Stack_Class import *

def is_matched(exp):
    """Returns True if Expression have open and close brackets; False Otherwise."""
    S = Stack()
    left = '{[('
    right = '}])'

    for c in exp:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()


exp = '{[((20-10))-4]+6}(){}{}[]'

print(is_matched(exp))
