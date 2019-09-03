A = [[-1] * 6 for _ in range(6)]

for i in range(1, 5):
    for j, a in enumerate(map(int, input().split()), start=1):
        A[i][j] = a

for i in range(1, 5):
    for j in range(1, 5):
        if A[i][j] == A[i - 1][j] or A[i][j] == A[i + 1][j] or A[i][j] == A[i][j - 1] or A[i][j] == A[i][j + 1]:
            print('CONTINUE')
            exit()

print('GAMEOVER')