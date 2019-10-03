N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if A[i - 1] > X:
        ans += A[i - 1] - X
        A[i - 1] = X
    if A[i - 1] + A[i] > X:
        ans += A[i] - (X - A[i - 1])
        A[i] = X - A[i - 1]

print(ans)