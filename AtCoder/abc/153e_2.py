H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

dp = [10**18] * (H + 1)
dp[0] = 0
for a, b in AB:
    for h in range(H + 1):
        r = min(H, h + a)
        if dp[r] > dp[h] + b:
            dp[r] = dp[h] + b
print(dp[H])
