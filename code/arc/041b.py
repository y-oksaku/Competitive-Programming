import heapq

def sol():
    N, M = map(int, input().split())
    B = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        line = input()
        for j, s in enumerate(line):
            B[i][j] = int(s)

    ans = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            while B[i - 1][j] > 0:
                B[i - 1][j] -= 1
                B[i + 1][j] -= 1
                B[i][j - 1] -= 1
                B[i][j + 1] -= 1
                ans[i][j] += 1

    for a in ans:
        print(*a, sep='')


sol()