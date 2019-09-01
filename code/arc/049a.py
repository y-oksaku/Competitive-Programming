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
    A, B, C, D = map(int, input().split())

    ans = []
    for i, s in enumerate(S + '\0'):
        if i in [A, B, C, D]:
            ans.append('"')
        if s == '\0':
            break
        ans.append(s)

    print(''.join(ans))


sol()