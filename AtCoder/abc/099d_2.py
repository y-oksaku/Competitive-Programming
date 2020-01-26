from collections import defaultdict
from itertools import product

N, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]

colors = defaultdict(lambda : defaultdict(int))

for h in range(1, N + 1):
    for w, c in enumerate(map(int, input().split()), start=1):
        colors[(h + w) % 3][c] += 1

cost = [[None] * C for _ in range(3)]

for i in range(3):
    for color in range(1, C + 1):
        cnt = 0
        for c, k in colors[i].items():
            cnt += D[c - 1][color - 1] * k
        cost[i][color - 1] = cnt

ans = 10**10
for cs in product(range(C), repeat=3):
    if len(set(cs)) == 3:
        cnt = 0
        for i, c in enumerate(cs):
            cnt += cost[i][c]
        ans = min(ans, cnt)

print(ans)
