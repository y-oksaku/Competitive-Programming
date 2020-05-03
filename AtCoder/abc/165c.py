from functools import lru_cache

N, M, Q = map(int, input().split())

BCD = [[] for _ in range(N)]
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    BCD[a - 1].append((b - a, c, d))

@lru_cache(maxsize=None)
def search(mi, A):
    if len(A) > N:
        return 0

    ret = 0
    for i in range(1, A[-1] + 1):
        ret = max(ret, search(i, A + (i,)))

    d = len(A)
    for b, c, d in BCD[N - d]:
        if A[-(b + 1)] - A[-1] == c:
            ret += d
    return ret

ans = 0
for i in range(1, M + 1):
    ans = max(ans, search(i, (i,)))
print(ans)
