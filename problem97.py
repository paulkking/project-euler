out = 28433

for i in range(7830457):
    out *= 2
    out %= 10000000000

out += 1

print(out)