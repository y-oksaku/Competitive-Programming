from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

N = int(input())
MOD = 10**9 + 7
S = ['A', 'G', 'C', 'T']
M = set(['AGC', 'GAC', 'ACG'])

for s in S:
    M.add(s + 'AGC')
    M.add(s + 'GAC')
    M.add(s + 'ACG')
    M.add('A' + s + 'GC')
    M.add('AG' + s + 'C')

@lru_cache(maxsize=None)
def search(prev, length):
    if length >= N:
        return 1

    ret = 0

    for s in S:
        T = prev + s
        if not T in M:
            T = T[:: -1][: 3][:: -1]
            ret += search(T, length + 1)
    return ret % MOD

ans = search('', 0)
print(ans)
