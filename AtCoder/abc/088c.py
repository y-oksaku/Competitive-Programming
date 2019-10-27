import numpy as np

C = []
for _ in range(3):
    c = list(map(int, input().split()))
    C.append(c)

A = np.array([
    [1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
])

Aplus = np.array([
    [1, 0, 0, 1, 0, 0, C[0][0]],
    [0, 1, 0, 1, 0, 0, C[1][0]],
    [0, 0, 1, 1, 0, 0, C[2][0]],
    [1, 0, 0, 0, 1, 0, C[0][1]],
    [0, 1, 0, 0, 1, 0, C[1][1]],
    [0, 0, 1, 0, 1, 0, C[2][1]],
    [1, 0, 0, 0, 0, 1, C[0][2]],
    [0, 1, 0, 0, 0, 1, C[1][2]],
    [0, 0, 1, 0, 0, 1, C[2][2]],
])

rankA = np.linalg.matrix_rank(A)
rankAp = np.linalg.matrix_rank(Aplus)

if rankA == rankAp:
    print('Yes')
else:
    print('No')