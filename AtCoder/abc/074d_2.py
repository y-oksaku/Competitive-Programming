N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

ans = sum(sum(a) for a in A) // 2
removeable = set()

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = A[i][k] + A[k][j]
            if A[i][j] > d:
                print(-1)
                exit()
            if A[i][j] == d and i != k and j != k:
                removeable.add((i, j))

for i in range(N):
    for j in range(i + 1, N):
        if (i, j) in removeable:
            ans -= A[i][j]

print(ans)
