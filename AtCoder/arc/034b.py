import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def f(n):
    return sum(map(int, str(n)))

def sol():
    N = int(input())

    ans = []
    for n in range(max(0, N - 1000), min(N, N + 1000) + 1):
        if f(n) + n == N:
            ans.append(n)

    print(len(ans))
    if ans:
        print(*ans, sep='\n')

sol()