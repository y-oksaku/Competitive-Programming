from functools import lru_cache

N = input()
K = int(input())

@lru_cache(maxsize=None)
def search(d, k, isLess):
    if k == K:
        return 1
    if d == len(N):
        return 0

    n = int(N[d])

    if isLess:
        return search(d + 1, k, isLess) + search(d + 1, k + 1, isLess) * 9

    ret = 0
    for i in range(n + 1):
        ret += search(d + 1, k + (1 if i > 0 else 0) , isLess or (i < n))
    return ret

print(search(0, 0, False))
