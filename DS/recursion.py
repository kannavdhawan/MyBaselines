
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

def add_number(n):

    if n/10 == 0:
        return n

    else:
        return n % 10 + add_number(n//10)     ## 12345 % 10 = 5, 12345 / 10 = 1234

print(add_number(123145))

def reverse_string(inp):
    if len(inp) <= 1:
        return inp
    else:
        return inp[-1] + reverse_string(inp[:-1])

print(reverse_string('hello world'))

# Create cache for known results

def factorial(k):
    factorial_memo = {}

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k - 1)

    return factorial_memo[k]

def cum_sum(n):
  # Base case
  if n == 1:
    return 1
  else:
    return n + cum_sum(n-1)

print(cum_sum((5)))


def word_split(phrase, list_of_words, output=None):

    if output is None:
        output = []
    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)
    return output


print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))




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

