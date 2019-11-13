N, K = map(int, input().split())
maxSum = N * (N + 1) // 2
minSum = (N - K) * (N - K + 1) - maxSum
ans = (maxSum - minSum) // 2 + 1
print(ans)