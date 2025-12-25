sumsq = sum(x ** 2 for x in range(1,101))
sqsum = sum(range(1,101)) ** 2

print(sqsum-sumsq)