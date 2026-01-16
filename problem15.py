n = 20
memo = dict()

def solve(x,y,n):
    if x == n and y == n:
        return 1
    if x > n or y > n:
        return 0
    solution = 0
    if (x,y) in memo:
        solution = memo[(x,y)]
    else:
        solution = solve(x+1,y,n) + solve(x,y+1,n)
        memo[(x,y)] = solution
    return solution

print(solve(0,0,n))