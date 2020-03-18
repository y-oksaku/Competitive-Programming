from bisect import bisect_left
N = int(input())
C = [int(input()) for _ in range(N)]

dp = [10**10] * N
for c in C:
    dp[bisect_left(dp, c)] = c

ans = dp.count(10**10)
print(ans)
