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
    S = input().rstrip()

    for i in range(len(S)):
        if S[i] == '*' or S[len(S) - i - 1] == '*':
            continue
        if S[i] != S[len(S) - i - 1]:
            print('NO')
            return

    print('YES')

sol()