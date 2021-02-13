import itertools


def perms(str):
    p = list(itertools.permutations(str))
    x = []
    for each in p:
        x.append("".join(each))
    return x

print(perms('abc'))