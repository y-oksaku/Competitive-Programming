N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1) :
    if A[i] + A[i + 1] > X :
        if A[i] > X :
            ans += A[i] - X
            A[i] = X
        if A[i + 1] > X - A[i] :
            dis = A[i + 1] - (X - A[i])
            ans += dis
            A[i + 1] -= dis

print(ans)