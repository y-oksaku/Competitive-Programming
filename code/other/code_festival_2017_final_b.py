import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    S = input().strip()
    cnt = Counter(S)

    A = cnt['a']
    B = cnt['b']
    C = cnt['c']

    if abs(A - B) <= 1 and abs(B - C) <= 1 and abs(C - A) <= 1:
        print('YES')
    else:
        print('NO')


sol()