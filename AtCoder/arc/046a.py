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

    ans = 1
    N -= 1
    while N > 0:
        ans += 1
        if len(set(str(ans))) == 1:
            N -= 1

    print(ans)


sol()