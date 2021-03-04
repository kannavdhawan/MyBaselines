import itertools


# permuations

from itertools import permutations
perms = [''.join(p) for p in permutations('stack')]   ## p = ('s','t','a','c','k')
print(perms)

def permute(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[0:i] + s[i+1:]):

                out += [let + perm]

    return out

print(permute('abc'))






def perms(str):
    p = list(itertools.permutations(str))
    print(p)
    x = []
    for each in p:
        x.append("".join(each))
    return x

print(perms('abc'))
