N = int(input())
M = int(input())

A = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

def search(m, n):
    global visited

    visited[m][n] = True
    ret = 0

    for dm, dn in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        toM, toN = m + dm, n + dn
        if 0 <= toM < M and 0 <= toN < N and A[toM][toN] == 1 and not visited[toM][toN]:
            ret = max(ret, search(toM, toN) + 1)

    visited[m][n] = False
    return ret

ans = 0
for m in range(M):
    for n in range(N):
        ans = max(ans, search(m, n))

print(ans)
