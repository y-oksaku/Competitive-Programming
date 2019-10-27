from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

dp = [defaultdict(int) for _ in range(N)]
dp[0][A[0]] = 1

for i, a in enumerate(A[1:], start=1):
    dp[i][a] += 1
    for g, cnt in dp[i - 1].items():
        dp[i][g] += cnt
        dp[i][gcd(g, a)] += cnt

print(dp[N - 1][1])