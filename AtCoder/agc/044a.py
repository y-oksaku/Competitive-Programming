from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

T = int(input())
INF = 10**18

for _ in range(T):
    N, A, B, C, D = map(int, input().split())
    DC = tuple(zip((2, 3, 5), (A, B, C)))

    @lru_cache(maxsize=None)
    def search(now):
        if now == 0:
            return 0

        ret = now * D
        for div, cost in DC:
            q, r = divmod(now, div)
            ret = min(
                ret,
                search(q) + cost + r * D,
                search(q + 1) + cost + (div - r) * D if q + 1 < now else INF,
            )
        return ret

    print(search(N))
