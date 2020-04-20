N, K = map(int, input().split())
MOD = 10**9 + 7
S = N * (N + 1) // 2

ans = 1
for d in range(N + 1):
    if N - d < K:
        break
    mx = S - (d * (d + 1) // 2)
    mi = max(0, (N - d - 1) * ((N - d - 1) + 1) // 2)
    ans += (mx - mi + 1) % MOD
    ans %= MOD
print(ans)
