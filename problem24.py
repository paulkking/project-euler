from itertools import permutations

l = list(permutations(range(0,10)))
l.sort()
print("".join(str(x) for x in l[999999]))