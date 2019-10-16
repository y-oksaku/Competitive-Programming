N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10**9 + 7

YArea = 0
for i in range(M - 1):
    YArea += (Y[i + 1] - Y[i]) * (i + 1) * (M - 1 - i)
    YArea %= MOD

ans = 0
for i in range(N - 1):
    ans += YArea * (X[i + 1] - X[i]) * (i + 1) * (N - 1 - i)
    ans %= MOD

print(ans)