from bisect import bisect_right

N = int(input())
card = [-1] * N

for i in range(N):
    c = int(input())
    card[i] = c

dp = [float('inf')]

for c in card:
    i = bisect_right(dp, c)
    if i >= len(dp):
        dp.append(c)
    else:
        dp[i] = c

ans = N - len(dp)
print(ans)
