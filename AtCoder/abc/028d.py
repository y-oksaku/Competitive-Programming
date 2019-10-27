import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, K = map(int, input().split())

    ans = (N - K) * (K - 1) * 6 + (N - 1) * 3 + 1
    print(ans / (N**3))

sol()