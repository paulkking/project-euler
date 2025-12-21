# !9 = 362880
# !9 ** 7 = 2640160 ; this is the upper bound to search

def checkFact(n):
    d = {"0":1,"1":1,"2":2,"3":6,"4":24,"5":120,"6":720,"7":5040,"8":40320,"9":362880} # Calculate ahead of time to save time
    # !0 = 1. What a world!
    res = sum([d[c] for c in str(n)])
    return n == res

print(sum([n for n in range(3,2640161) if checkFact(n)]))