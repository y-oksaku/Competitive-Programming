import numpy as np

R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(R)], dtype=np.bool)
I = np.array([list(range(R)) for _ in range(C)]).T

ans = 0
for state in range(1 << R):
    B = (A ^ (((1 << I) & state) > 0)).sum(axis=0)
    ans = max(ans, np.sum(np.maximum(B, R - B)))

print(ans)