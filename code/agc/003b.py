import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    A = [int(input()) for _ in range(N)] + [0]

    partialSum = 0
    ans = 0
    for a in A:
        if a == 0:
            ans += partialSum // 2
            partialSum = 0
        else:
            partialSum += a

    print(ans)

sol()