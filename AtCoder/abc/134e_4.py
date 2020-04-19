from bisect import bisect_right

N = int(input())
A = [int(input()) for _ in range(N)]
INF = 10**18

dp = [INF] * N
for a in A:
    dp[bisect_right(dp, -a)] = -a
ans = N - dp.count(INF)
print(ans)
