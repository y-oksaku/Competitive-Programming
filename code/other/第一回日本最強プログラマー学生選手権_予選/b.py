import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    front = 0
    back = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                front += 1
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                back += 1

    ans = (((front * K * (K + 1) // 2) % MOD) + ((back * (K - 1) * K // 2) % MOD)) % MOD
    print(ans)


sol()