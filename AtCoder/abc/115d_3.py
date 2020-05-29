from functools import lru_cache

N, X = map(int, input().split())

@lru_cache(maxsize=None)
def size(level):
    return 1 if level == 0 else size(level - 1) * 2 + 3

@lru_cache(maxsize=None)
def calc(level, N):
    if level == 0:
        return 1 if N > 0 else 0

    N = min(N, size(level))

    ret = 0
    N -= 1

    if N >= size(level - 1):
        ret += calc(level - 1, size(level - 1))
        N -= size(level - 1)

        if N >= 1:
            ret += 1
            N -= 1

    return ret + calc(level - 1, N)

print(calc(N, X))
