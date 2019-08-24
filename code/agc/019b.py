import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    A = input().strip()

    cnt = Counter(A)

    sameCount = 0
    for _, c in cnt.items():
        sameCount += c * (c - 1) // 2

    N = len(A)
    ans = N * (N - 1) // 2 - sameCount + 1
    print(ans)


sol()