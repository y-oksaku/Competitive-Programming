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

    X = [(x, i + 1) for i, x in enumerate(map(int, input().split()))]
    Y = X[:]

    Y.sort()

    pos = K - 1
    ans = [Y[K - 1][1]]
    for x, _ in X[K:][:: -1]:
        left = bisect_left(Y, (x, 0))
        Y[left] = (Y[left][0], -1)
        if left <= pos:
            pos += 1
            while Y[pos][1] == -1:
                pos += 1
        ans.append(Y[pos][1])

    print(*ans[:: -1], sep='\n')

sol()