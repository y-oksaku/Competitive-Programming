from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
MOD = 10**9 + 7

def isOk(T):
    for i in range(4):
        t = list(T)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if 'AGC' in ''.join(t):
            return False
    return True

@lru_cache(maxsize=None)
def search(n, prev):
    if n == 0:
        return 1

    ret = 0
    for s in ['A', 'G', 'C', 'T']:
        t = (prev + s)[1:]
        if isOk(t):
            ret += search(n - 1, t)
            ret %= MOD

    return ret

print(search(N, 'ZZZZ'))