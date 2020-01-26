H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

dp = [10**10] * (H + 1)
dp[H] = 0

for a, b in AB:
    for h in range(H + 1)[:: -1]:
        dp[h] = min(dp[h], dp[min(H, h + a)] + b)

print(dp[0])