N, K = map(int, input().split())
MOD = 10**9 + 7

ans = 0
for k in range(K, N + 2):
    S = k * (k - 1) // 2
    mx = N * k - S
    mi = S
    ans += mx - mi + 1
    ans %= MOD
print(ans)
