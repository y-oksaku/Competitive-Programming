N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def sol():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = A[i][k] + A[k][j]
                if d < A[i][j]:
                    return - 1

    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                if k == i or k == j:
                    continue
                if A[i][k] + A[k][j] == A[i][j]:
                    break
            else:
                ret += A[i][j]

    return ret

print(sol())
