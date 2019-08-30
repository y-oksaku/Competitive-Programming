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
    N, D = map(int, input().split())
    X, Y = map(int, input().split())

    if abs(X) % D != 0 or abs(Y) % D != 0 or (abs(X) + abs(Y)) > N * D:
        print(0)
        return

    nessX = abs(X) // D
    nessY = abs(Y) // D

    R = N - nessX - nessY
    if R % 2 == 1:
        print(0)
        return

    count = 0
    fact = [1] * (N + 10)
    for i in range(1, N + 10):
        fact[i] = fact[i - 1] * i

    for x in range(0, R + 1, 2):
        for y in range(0, R + 1, 2):
            if x + y == R:
                count += fact[N] // fact[nessX + x // 2] // fact[nessY + y // 2] // fact[x // 2] // fact[y // 2]

    print(count / pow(4, N))

sol()