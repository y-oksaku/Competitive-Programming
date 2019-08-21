import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    A = [0] * N
    B = [0] * N

    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    nowSum = 0
    for a, b in zip(A[:: -1], B[:: -1]):
        r = (a + nowSum) % b
        if (r + a + nowSum) % b != 0:
            r = b - r
        if r == 0:
            continue
        nowSum += r

    print(nowSum)

sol()