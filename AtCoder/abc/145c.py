from itertools import permutations

N = int(input())

def length(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

XY = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for x, y in XY:
    for u, v in XY:
        ans += length(x, y, u, v)

print(ans / N)