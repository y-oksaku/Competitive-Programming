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
    S = [0] * N

    for i in range(N):
        S[i] = input().rstrip()

    def isSame(a):
        for i in range(N):
            for j in range(N):
                if S[(i + a) % N][j] != S[(j + a) % N][i]:
                    return False
        return True

    ans = 0
    for a in range(N):
        if isSame(a):
            ans += N

    print(ans)

sol()