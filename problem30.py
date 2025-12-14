# 9 ** 5 * 7 = 413343
# The max number of digits should be 6; no way to scale faster than this

powers = [x ** 5 for x in range(0,10)]

def sfp(n):
    a = str(n)
    sum = 0
    for c in a:
        sum += powers[int(c)]
    return sum

out = 0

for i in range(2,1000000): # Do not include 1
    if i == sfp(i):
        out += i

print(out)