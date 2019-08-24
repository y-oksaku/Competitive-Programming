import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    H, W = map(int, input().split())

    if H % 3 == 0 or W % 3 == 0:
        print(0)
        return

    ans = min(H, W)

    for w in [W // 3, W // 3 + 1]:
        A = w * H
        for h in [H // 2, H // 2 + 1]:
            B = (W - w) * h
            C = H * W - B - A

            Smax = max(A, B, C)
            Smin = min(A, B, C)
            ans = min(ans, abs(Smax - Smin))

    for h in [H // 3, H // 3 + 1]:
        A = h * W
        for w in [W // 2, W // 2 + 1]:
            B = (H - h) * w
            C = H * W - B - A

            Smax = max(A, B, C)
            Smin = min(A, B, C)
            ans = min(ans, abs(Smax - Smin))

    print(ans)

sol()