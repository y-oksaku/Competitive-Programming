import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, a = map(int, input().split())
    K = int(input())

    B = [int(b) - 1 for b in input().split()]

    pos = [a - 1]
    visited = [False] * N
    visited[a - 1] = True

    while not visited[B[pos[-1]]]:
        visited[B[pos[-1]]] = True
        pos.append(B[pos[-1]])

    roopStart = B[pos[-1]]

    for i, p in enumerate(pos):
        if K == 0:
            print(p + 1)
            return

        if roopStart == p:
            K %= (len(pos) - i)
            print(pos[i + K] + 1)
            return
        else:
            K -= 1

sol()