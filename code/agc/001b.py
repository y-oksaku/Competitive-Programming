import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, X = map(int, input().split())

    ans = N
    A = max(N - X, X)
    B = min(N - X, X)

    while B:
        q = A // B
        r = A % B

        ans += B * 2 * q
        if r == 0:
            ans -= B

        A = B
        B = r

    print(ans)

sol()