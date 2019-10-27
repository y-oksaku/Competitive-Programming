import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    S = input().rstrip()

    isLeft = [(i % 2 == 0) ^ (s == 'W') for i, s in enumerate(S)]

    ans = 1
    left = 0
    for black in isLeft:
        if black:
            left += 1
        else:
            ans = (ans * left) % MOD
            left -= 1

    if left != 0:
        ans = 0

    for i in range(1, N + 1):
        ans = (ans * i) % MOD

    print(ans)

sol()