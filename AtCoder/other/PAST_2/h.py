N, L = map(int, input().split())
X = set(map(int, input().split()))
T1, T2, T3 = map(int, input().split())
INF = 10**18

dp = [INF] * (L + 10)
dp[0] = 0

D = [(1, T1), (2, T1 + T2), (4, T1 + T2 * 3)]

for l in range(L):
    for d, t in D:
        to = l + d
        if to in X:
            t += T3
        if to > L:
            diff = to - L - 1
            t -= T1 // 2 + T2 // 2
            t -= diff * T2
            to = L

        dp[to] = min(dp[to], dp[l] + t)

print(dp[L])