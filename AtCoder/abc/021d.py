import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.inv = [1, 1] + [0] * size
        self.factInv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def nprWithoutMod(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] // self.fact[n - r]

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        if n == r:
            return 1
        if r == 0:
            return 1
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def ncrWithoutMod(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        if n == r:
            return 1
        if r == 0:
            return 1
        return self.fact[n] // self.fact[r] // self.factInv[n - r]

def sol():
    N = int(input())
    K = int(input())

    ans = 0
    comb = Combination(N + K + 10)
    for k in range(1, K + 1):
        ans = (ans + comb.ncr(N, k) * comb.ncr(K - 1, K - k)) % MOD

    print(ans)

sol()