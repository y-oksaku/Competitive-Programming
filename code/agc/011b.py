import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    sumA = sum(A)
    ans = 0
    for i in range(N)[:: -1]:
        sumA -= A[i]
        if sumA * 2 < A[i]:
            ans = N - i
            break
    print(ans)


sol()