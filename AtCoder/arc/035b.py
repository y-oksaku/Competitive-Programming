import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

# modなしの場合は，mod=1にする

class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

def sol():
    N = int(input())
    T = []

    for _ in range(N):
        t = int(input())
        T.append(t)

    T.sort()

    minTime = 0
    now = 0
    for t in T:
        now += t
        minTime += now

    cntT = Counter(T)
    comb = Combination(10100)
    ans = 1

    for _, c in cntT.items():
        ans = (ans * comb.npr(c, c)) % MOD

    print(minTime)
    print(ans)

sol()