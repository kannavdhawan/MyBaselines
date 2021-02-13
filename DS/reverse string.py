def reverse_string(str):

    x = []
    for i in str:

        x.insert(0, i)

    return "".join(x)

print(reverse_string('Hello World'))

def reverse_string_recursion(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + reverse_string_recursion(str[:-1])
print(reverse_string_recursion('Hello World'))
