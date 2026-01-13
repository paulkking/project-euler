out = 0

tris = {0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210} # Highest value is 192

with open("Project-Euler\\0042_words.txt") as f:
    l = f.read().split(',')
    for word in l:
        s = sum(ord(c)-64 for c in word[1:-1])
        if s in tris: out+=1


print(out)