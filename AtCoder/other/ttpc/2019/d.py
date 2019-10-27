import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())
    A = list(map(int, input().split()))
    M = max(A)

    if N == 1:
        print('An')
        return

    isPrime = [True] * (M + 1)
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, M + 1):
        if isPrime[i]:
            for j in range(2 * i, M + 1, i):
                isPrime[j] = False

    onePrime = 0  # 1回しか引けない
    doublePrime = 0  # 2回引ける
    seven = 0  # 3回引ける

    for a in A:
        if a == 7:
            seven += 1
        elif isPrime[a - 2]:
            doublePrime += 1
        else:
            onePrime += 1

    nim = 0
    for _ in range(onePrime):
        nim ^= 1
    for _ in range(doublePrime):
        nim ^= 2
    for _ in range(seven):
        nim ^= 3

    if nim == 0:  # 必勝
        print('Ai')
    else:
        print('An')

sol()