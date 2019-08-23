import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    canWin = [None] * (K + 1)
    canWin[0] = False

    for k in range(1, K + 1):
        for a in A:
            if k - a >= 0 and canWin[k - a] == False:
                canWin[k] = True
                break
        else:
            canWin[k] = False

    if canWin[K]:
        print('First')
    else:
        print('Second')

sol()