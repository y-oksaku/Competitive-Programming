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
    N = int(input())
    A = [(n, i + 1) for i, n in enumerate(map(int, input().split())) ]

    A.sort()
    ans = []
    for _, i in A:
        ans.append(i)
    print(*ans)

sol()