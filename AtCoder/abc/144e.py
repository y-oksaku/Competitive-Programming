import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))

    A.sort()
    F.sort(reverse=True)

    def isOk(t):
        cnt = 0
        for a, f in zip(A, F):
            ness = t // f
            if a <= ness:
                continue
            cnt += a - ness

        if cnt > K:
            return False
        else:
            return True

    ng = -1
    ok = max(A) * max(F) + 10

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if isOk(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


sol()