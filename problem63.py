# Bases greater than 9 will always result in more digits than the power
# For bases 9 and lower, digits will not keep pace with powers.
# Therefore, we can search bases 1 - 9 and stop looking once power > digit length

out = 0

for i in range(1,10):
    a = i
    n = 1
    while n <= len(str(a)):
        if n == len(str(a)):
            out += 1
        n += 1
        a *= i

print(out)