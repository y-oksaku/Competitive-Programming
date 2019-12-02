N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

dp = [0] * (N + 1)
dp[0] = 3

ans = 1
for a in A:
    ans *= dp[a]
    ans %= MOD
    dp[a] -= 1
    dp[a + 1] += 1

print(ans)