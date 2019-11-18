import numpy as np

N, M, K = map(int, input().split())

LR = np.zeros(shape=(N + 1, N + 1), dtype=np.int32)
L, R = np.array([input().split() for _ in range(M)], dtype=np.int32).T
np.add.at(LR, (L, R), 1)

np.cumsum(LR, axis=0, out=LR)
np.cumsum(LR, axis=1, out=LR)

P, Q = np.array([input().split() for _ in range(K)], dtype=np.int32).T

P -= 1
ans = LR[Q, Q] - LR[P, Q] - LR[Q, P] + LR[P, P]
print(*ans, sep='\n')
