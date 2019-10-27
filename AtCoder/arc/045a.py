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
    S = input().split()
    ans = []

    for s in S:
        if s == 'Left':
            ans.append('<')
        elif s == 'Right':
            ans.append('>')
        elif s == 'AtCoder':
            ans.append('A')

    print(*ans)

sol()