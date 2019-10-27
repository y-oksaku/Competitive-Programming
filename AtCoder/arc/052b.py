import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
import math

def sol():
    N, Q = map(int, input().split())
    M = 10**5

    cumV = [0] * M

    for _ in range(N):
        X, R, H = map(int, input().split())
        V = R**2 * H  # × pi / 3
        disSum = 0
        for h in range(H)[:: -1]:
            sub = V * ((H - h) / H)**3 - disSum
            cumV[X + h] += sub
            disSum += sub

    for i in range(M - 1)[:: -1]:
        cumV[i] += cumV[i + 1]

    ans = []
    for _ in range(Q):
        A, B = map(int, input().split())
        ans.append(cumV[A] - cumV[B])

    print(*[a * math.pi / 3 for a in ans], sep='\n')

sol()