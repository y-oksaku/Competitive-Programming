import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())

    H = [0] * N
    S = [0] * N
    for i in range(N):
        h, s = map(int, input().split())
        H[i] = h
        S[i] = s

    ok = max(H) + max(S) * N
    ng = 0

    def isOk(height):
        B = [((height - h) // s) for h, s in zip(H, S)]
        B.sort()
        for i, b in enumerate(B):
            if b < i:
                return False
        return True

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if isOk(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

sol()