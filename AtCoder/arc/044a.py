import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    strN = input().strip()
    N = int(strN)

    if N == 1:
        print('Not Prime')
        return

    for p in range(2, int(N**0.5) + 1):
        if N % p == 0:
            break
    else:
        print('Prime')
        return

    if (N % 10) % 5 == 0 or (N % 10) % 2 == 0:
        print('Not Prime')
        return

    digitSum = 0
    for s in strN:
        digitSum += int(s)

    if digitSum % 3 == 0:
        print('Not Prime')
    else:
        print('Prime')


sol()