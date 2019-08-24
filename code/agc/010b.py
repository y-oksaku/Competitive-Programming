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
    A = list(map(int, input().split()))

    S = sum(A)

    if S % (N * (N + 1) // 2) != 0:
        print('NO')
        return

    K = S // (N * (N + 1) // 2)
    for diff in [A[i] - A[i - 1] for i in range(N)]:
        if K - diff < 0 or (K - diff) % N != 0:
            print('NO')
            return

    print('YES')


sol()