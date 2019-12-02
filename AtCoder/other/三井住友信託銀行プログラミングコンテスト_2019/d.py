from bisect import bisect_right
from collections import defaultdict

N = int(input())
S = input()
INF = float('inf')

nToD = defaultdict(list)
for d, s in enumerate(S):
    nToD[s].append(d)
for d in range(10):
    nToD[str(d)].append(INF)

ans = 0
for i in range(1000):
    P = '%03d' % i
    prev = nToD[P[0]][0]

    if prev == INF:
        continue

    for p in P[1:]:
        prev = nToD[p][bisect_right(nToD[p], prev)]
        if prev == INF:
            break
    else:
        ans += 1

print(ans)