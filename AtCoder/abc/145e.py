N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort()
INF = float('inf')

dp = [-INF] * (T + 1)
dp[0] = 0

for a, b in AB:
    newDp = dp[::]
    for t, d in enumerate(dp[:T]):
        newDp[min(T, t + a)] = max(newDp[min(T, t + a)], d + b)
    dp = newDp

print(max(dp))