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
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    cntA = Counter(A)

    ans = []
    for i in range(1, N + 1):
        if K - (Q - cntA[i]) > 0:
            ans.append('Yes')
        else:
            ans.append('No')

    print(*ans, sep='\n')


sol()