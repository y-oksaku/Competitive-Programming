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
    N = int(input())
    A, B = map(int, input().split())

    if N <= A:
        print('Takahashi')
        return

    if A == B:
        r = N % (A + 1)
        if r == 0:
            print('Aoki')
        else:
            print('Takahashi')
        return

    if A > B:
        print('Takahashi')
    else:
        print('Aoki')


sol()