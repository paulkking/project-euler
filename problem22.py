out = 0

with open('Project-Euler\\0022_names.txt') as f:
    l = sorted(f.read().split(','))
    for i in range(len(l)):
        name = l[i][1:-1]
        score = sum(ord(c)-64 for c in name)
        out += score * (i + 1)

print(out)