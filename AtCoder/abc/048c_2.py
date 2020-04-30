N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    j = i + 1
    if A[i] + A[j] > X:
        d = min(A[j], (A[i] + A[j]) - X)
        ans += d
        A[j] -= d
    if A[i] + A[j] > X:
        d = min(A[i], (A[i] + A[j]) - X)
        ans += d
        A[i] -= d

print(ans)