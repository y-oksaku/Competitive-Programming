N, M = map(int, input().split())
MOD = 10**9 + 7

if abs(N - M) >= 2:
    print(0)
    exit(0)

fact = [1 for _ in range(M + 100)]
for i in range(1, M + 100):
    fact[i] = (fact[i - 1] * i) % MOD

if N == M:
    ans = fact[N] * fact[N] % MOD * 2 % MOD
else:
    ans = fact[N] * fact[M] % MOD

print(ans)