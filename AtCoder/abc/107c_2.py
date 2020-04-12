N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10**18
for l in range(N - K + 1):
    D = X[l + K - 1] - X[l]
    if X[l] <= 0 <= X[l + K - 1]:
        D += min(-X[l], X[l + K - 1])
    elif X[l + K - 1] <= 0:
        D += -X[l + K - 1]
    elif X[l] >= 0:
        D += X[l]
    ans = min(ans, D)
print(ans)
