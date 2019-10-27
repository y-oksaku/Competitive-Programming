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
    words = []

    for _ in range(N):
        s = list(input().rstrip())
        words.append(''.join(s[:: -1]))

    words.sort()

    for s in words:
        print(s[:: -1])


sol()