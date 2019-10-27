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
    N, K = map(int, input().split())

    def gcd(i):
        a, b = max(i, K), min(i, K)
        while b > 0:
            a, b = b, a % b
        return a

    ans = 0
    for i in range(1, K + 1):
        minI = i
        maxI = (N // K) * K + i

        if maxI > N:
            maxI -= K
        if minI > maxI:
            continue
        if minI == maxI:
            ans += (minI * K) // gcd(minI)
            ans %= MOD
        else:
            count = (maxI - minI) // K + 1
            ans += (maxI + minI) * count // 2 * K // gcd(minI)
            ans %= MOD

    print(ans)

sol()