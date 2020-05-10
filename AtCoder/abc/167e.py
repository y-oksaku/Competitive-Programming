MOD = 998244353

class Combination:
    def __init__(self, size):
        self.size = size + 2
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % MOD
            self.inv[i] = -self.inv[MOD % i] * (MOD // i) % MOD
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % MOD

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % MOD) % MOD

    def nhr(self, n, r):  # 重複組合せ: x_1 + ... + x_n = r
        return self.ncr(n + r - 1, n - 1)

N, M, K = map(int, input().split())
comb = Combination(N + K)

ans = 0
for k in range(K + 1):
    L = N - k
    ans += M * pow(M - 1, L - 1, MOD) * comb.nhr(L, k)
    ans %= MOD
print(ans)