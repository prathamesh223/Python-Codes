from itertools import permutations
def find_permutations(s):
    return [''.join(p) for p in permutations(s)]
s='abcd'
print(find_permutations(s))
