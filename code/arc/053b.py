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
    cntS = Counter(S)

    center = 0
    even = 0

    for _, cnt in cntS.items():
        if cnt % 2 == 0:
            even += cnt
        else:
            center += 1
            even += cnt - 1

    if center == 0:
        ans = even
    else:
        ans = even // (2 * center) * 2 + 1

    print(ans)

sol()