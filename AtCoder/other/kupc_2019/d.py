N = int(input())
S = input() + '2'
MOD = 998244353

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

    def invN(self, n):
        return self.inv[n]

comb = Combination(2 * N + 100, MOD)

def catalan(n):
    return comb.ncr(2 * n, n) * comb.invN(n + 1)

ans = 1
seq = 0
now = S[0]
for s in S:
    if s == now:
        seq += 1
    else:
        ans *= catalan(seq)
        ans %= MOD
        seq = 1
        now = s

print(ans % MOD)