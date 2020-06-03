from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

H, W, D = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
aToHW = {}
for h, row in enumerate(A):
    for w, a in enumerate(row):
        aToHW[a] = (h, w)

Q = int(input())

@lru_cache(maxsize=None)
def search(now):
    if not now + D in aToHW:
        return 0

    l, r = aToHW[now], aToHW[now + D]
    return abs(l[0] - r[0]) + abs(l[1] - r[1]) + search(now + D)

ans = []
for _ in range(Q):
    l, r = map(int, input().split())

    ans.append(search(l) - search(r))

print(*ans, sep='\n')
