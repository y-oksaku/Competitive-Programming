from functools import lru_cache

N = input()
K = int(input())

@lru_cache(maxsize=None)
def search(d, cnt, isLess):
    if d == len(N):
        return cnt == K

    a = int(N[d])

    if isLess:
        return search(d + 1, cnt + 1, isLess) * 9 + search(d + 1, cnt, isLess)

    ret = 0
    for i in range(a + 1):
        ret += search(d + 1, cnt + (i != 0), i < a)
    return ret

print(search(0, 0, False))