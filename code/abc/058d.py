N, M = map(int, input().split())
MOD = 10**9 + 7

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

sumX = 0
sumY = 0

for i, x in enumerate(X):
    sumX += -(N - (i + 1)) * x + i * x
    sumX %= MOD

for i, y in enumerate(Y):
    sumY += -(M - (i + 1)) * y + i * y
    sumX %= MOD

ans = sumX * sumY % MOD
print(ans)

