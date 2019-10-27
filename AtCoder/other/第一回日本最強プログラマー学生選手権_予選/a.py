import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    M, D = map(int, input().split())

    ans = 0
    for month in range(1, M + 1):
        for day in range(1, D + 1):
            d1 = day % 10
            d2 = day // 10
            if d1 >= 2 and d2 >= 2 and d1 * d2 == month:
                ans += 1

    print(ans)


sol()