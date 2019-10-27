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
    A, B = map(int, input().split())

    if A * B < 0:
        print(B - A - 1)
    else:
        print(B - A)


sol()