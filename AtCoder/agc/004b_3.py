N, X = map(int, input().split())
A = list(map(int, input().split()))
B = A[:]

ans = sum(A)
for x in range(1, N + 1):
    for i in range(N)[::-1]:
        if B[i] > A[i - x]:
            B[i] = A[i - x]
    ans = min(ans, sum(B) + x * X)
print(ans)
