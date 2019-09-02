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
    _, _ = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    ans = len(A & B) / len(A | B)

    print(ans)


sol()