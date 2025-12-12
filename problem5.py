def check20(n):
    vals = [20,19,18,17,16,15,14,13,12,11,7]
    for i in vals:
        if n % i > 0:
            return False
    return True
    
out = 1
while check20(out) == False:
    out += 1
print(out)