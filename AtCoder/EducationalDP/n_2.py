import numpy as np

N = int(input())
A = np.array(input().split(), np.int64)

Acum = np.zeros((N, N + 1), dtype=np.int64)
for i in range(N):
    Acum[i, i + 1:] = A[i:].cumsum()

dp = np.zeros((N, N + 1), dtype=np.int64)

for length in range(2, N + 1):
    for left in range(N - length + 1):
        right = left + length
        dp[left, right] = (dp[left, left + 1: right] + dp[left + 1: right, right]).min() + Acum[left, right]

print(dp[0, N])