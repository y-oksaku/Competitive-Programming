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
    N, L = map(int, input().split())
    S = input()

    now = 1
    ans = 0
    for s in S:
        if s == '+':
            now += 1
            if now > L:
                ans += 1
                now = 1
        else:
            now -= 1

    print(ans)

sol()