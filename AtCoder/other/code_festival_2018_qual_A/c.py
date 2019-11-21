import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

B = [a.bit_length() for a in A]
M = 4000

nonZero = np.zeros(M, dtype=np.int64)
hasZero = np.zeros(M, dtype=np.int64)

nonZero[0] = 1

for b in B:
    np.cumsum(hasZero, out=hasZero)
    hasZero[b + 1:] -= hasZero.copy()[: M - (b + 1)]
    hasZero[b:] += nonZero[: M - b]

    np.cumsum(nonZero, out=nonZero)
    nonZero[b:] -= nonZero.copy()[: M - b]

    nonZero %= MOD
    hasZero %= MOD

if K < M:
    ans = nonZero[K] + hasZero[: K + 1].sum()
else:
    ans = hasZero.sum()

print(ans % MOD)
