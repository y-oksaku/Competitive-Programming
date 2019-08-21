import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    sumPlus = [0] * (N + 1)
    sumA = [0] * (N + 1)

    for i, a in enumerate(A):
        sumA[i + 1] = sumA[i] + a
        if a > 0:
            sumPlus[i + 1] = sumPlus[i] + a
        else:
            sumPlus[i + 1] = sumPlus[i]

    ans = 0
    for left in range(N - K + 1):  # []left - left + K) を捨てる or 加える
        leftSum = sumPlus[left]
        rightSum = sumPlus[N] - sumPlus[left + K]
        midSum = sumA[left + K] - sumA[left]

        if midSum > 0:
            ans = max(ans, leftSum + rightSum + midSum)
        else:
            ans = max(ans, leftSum + rightSum)

    print(ans)

sol()