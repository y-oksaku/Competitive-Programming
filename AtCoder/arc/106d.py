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

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % MOD

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % MOD) % MOD

    def nhr(self, n, r):  # 重複組合せ: x_1 + ... + x_n = r
        return self.ncr(n + r - 1, n - 1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
comb = Combination(K + 100)

B = A[::]
S = [0] * (K + 1)
S[0] = N
for i in range(1, K + 1):
    s = 0
    for j in range(N):
        s += A[j]
        A[j] = A[j] * B[j] % MOD
        s %= MOD
    S[i] = s

for x in range(1, K + 1):
    ans = 0
    for i in range(x + 1):
        ans += (S[x - i] * S[i] - S[x]) * comb.ncr(x, i) % MOD
        ans %= MOD

    print(ans * pow(2, MOD - 2, MOD) % MOD)
