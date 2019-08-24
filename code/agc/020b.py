import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    K = int(input())
    A = list(map(int, input().split()))

    maxAns = 2
    minAns = 2

    for a in reversed(A):
        maxAns = maxAns // a * a + a - 1
        minAns = -(-minAns // a) * a

    resMax = maxAns
    resMin = minAns

    for a in A:
        resMax = resMax // a * a
        resMin = resMin // a * a

    if resMax == resMin == 2:
        print(minAns, maxAns)
    else:
        print(-1)

sol()