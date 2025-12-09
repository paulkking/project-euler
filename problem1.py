# Multiples of 3 or 5

out = 0
target = 1000

add = 3
while add < target:
    out += add
    add += 3

add = 5
while add < target:
    if add % 3 != 0:
        out += add
    add += 5

print(out)