from functools import lru_cache

N, X = map(int, input().split())

@lru_cache(maxsize=None)
def length(level):
    if level <= 0:
        return 1
    return length(level - 1) * 2 + 3

@lru_cache(maxsize=None)
def search(level, right):
    if level == 0:
        return 1

    ret = 0
    right -= 1
    if length(level - 1) <= right:
        ret += search(level - 1, length(level - 1))
        right -= length(level - 1)

        if right > 0:
            ret += 1
        right -= 1

    if 0 < right:
        ret += search(level - 1, right)
    return ret

print(search(N, X))
