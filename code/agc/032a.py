import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    B = list(map(int, input().split()))

    ans = []

    for time in range(N):
        for i in range(N - time)[:: -1]:
            if B[i] == i + 1:
                ans.append(B.pop(i))
                break

    if B:
        print(-1)
    else:
        for a in reversed(ans):
            print(a)

sol()