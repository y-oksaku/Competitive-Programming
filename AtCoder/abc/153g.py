import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)

N, A = map(int, input().split())
HD = [tuple(map(int, input().split())) for _ in range(N)]

accHD = [(0, 0)] * (N + 1)
for i, (h, d) in enumerate(HD, start=1):
    accHD[i] = (accHD[i - 1][0] + h, accHD[i - 1][1] + d)

@lru_cache(maxsize=None)
def sol(left, right):
    if left == right:
        return 0
    ret = 10**10
    accD = accHD[right][1] - accHD[left][1]
    for mid in range(left, right):
        cost = -(-HD[mid][0] // A) * accD - HD[mid][1]
        ret = min(ret, cost + sol(left, mid) + sol(mid + 1, right))
    return ret

print(sol(0, N))
