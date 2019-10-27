import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    A = [int(x) for x in input().split()]

    oddCount = 0
    for a in A:
        if a % 2 == 1:
            oddCount += 1

    if oddCount % 2 == 0:
        print('YES')
    else:
        print('NO')


sol()