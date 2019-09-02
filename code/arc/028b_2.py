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

    que = []

    for x, i in X[:K]:
        heappush(que, (-x, i))

    ans = [que[0][1]]
    for x, i in X[K:]:
        heappush(que, (-x, i))
        heappop(que)
        ans.append(que[0][1])

    print(*ans, sep='\n')

sol()