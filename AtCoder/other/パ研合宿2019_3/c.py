N, M = map(int, input().split())

A = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(M):
    for j in range(i + 1, M):
        cnt = 0
        for n in range(N):
            cnt += max(A[n][i], A[n][j])
        ans = max(ans, cnt)

print(ans)
