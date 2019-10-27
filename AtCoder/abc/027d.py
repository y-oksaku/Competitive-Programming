import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    S = input().rstrip()
    N = len(S)

    A = []
    plus = 0
    minus = 0

    for i in range(N)[:: -1]:
        if S[i] == 'M':
            A.append(plus - minus)
        elif S[i] == '+':
            plus += 1
        elif S[i] == '-':
            minus += 1

    A.sort(reverse=True)
    ans = sum(A[: len(A) // 2]) - sum(A[len(A) // 2:])
    print(ans)

sol()