def Balance_check(s):
    #     Check the even number of elements
    if len(s) % 2 != 0:
        return False
    opening = set('{([')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last = stack.pop()

            if (last, paren) not in matches:
                return False

    return len(stack) == 0

print(Balance_check('[](){([[[]]])}'))
