import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    left = 0
    for i in range(N - 1):
        if A[i] + A[i + 1] >= L:
            print('Possible')
            left = i
            break
    else:
        print('Impossible')
        return

    for i in range(left):
        print(i + 1)
    for j in range(left, N - 1)[:: -1]:
        print(j + 1)


sol()