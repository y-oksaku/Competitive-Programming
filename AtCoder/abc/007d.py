import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def f(n):
    if n == 0:
        return 0

    q, r = divmod(n, 10)
    x = f(q) * 8

    if str(q).count('4') > 0 or str(q).count('9') > 0:
        return x

    if r <= 4:
        return x + r
    if r <= 9:
        return x + r - 1


def sol():
    A, B = map(int, input().split())

    ans = (B - A) - (f(B + 1) - f(A)) + 1
    print(ans)


sol()