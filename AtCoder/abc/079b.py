from functools import lru_cache

N = int(input())

@lru_cache(maxsize=None)
def luca(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    return luca(n - 1) + luca(n - 2)

print(luca(N))
