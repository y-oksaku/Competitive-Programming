N, K = map(int, input().split())
MOD = 10**9 + 7

ans = 0
for k in range(K, N + 2):
    base = k * (k - 1) // 2
    mx = base + k + (N - k) * k
    ans += mx - base + 1
    ans %= MOD

print(ans)
