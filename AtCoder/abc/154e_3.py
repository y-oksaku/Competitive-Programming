from functools import lru_cache

N = input()
K = int(input())

@lru_cache(maxsize=None)
def search(d, cnt, isEq):
    if d == len(N):
        return 1 if cnt == K else 0

    n = int(N[d])

    if isEq and n == 0:
        return search(d + 1, cnt, isEq)

    if isEq:
        ret = 0
        ret += search(d + 1, cnt, False)
        for _ in range(1, n):
            ret += search(d + 1, cnt + 1, False)
        ret += search(d + 1, cnt + 1, True)
        return ret

    return search(d + 1, cnt, False) + search(d + 1, cnt + 1, False) * 9

print(search(0, 0, True))
