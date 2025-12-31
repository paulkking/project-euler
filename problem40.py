stack = []
idx = 1

while len(stack) < 1000000:
    for c in str(idx):
        stack.append(int(c))
    idx += 1

print(stack[0]*stack[9]*stack[99]*stack[999]*stack[9999]*stack[99999]*stack[999999])