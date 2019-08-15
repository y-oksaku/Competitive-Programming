N, K = map(int, input().split())
A = list(map(int, input().split()))

sumA = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    sumA[i] = sumA[i - 1] + A[i - 1]

ans = 0
for i in range(N - K + 1):
    ans += sumA[i + K] - sumA[i]

print(ans)