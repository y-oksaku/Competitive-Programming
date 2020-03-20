from collections import Counter

N, M = map(int, input().split())
ims = [0] * (N + 1)

for _ in range(M):
    a, b = map(lambda a: int(a) - 1, input().split())
    if a > b:
        a, b = b, a
    ims[a] += 1
    ims[b] -= 1

for i in range(1, N + 1):
    ims[i] += ims[i - 1]

print('YES' if all(c % 2 == 0 for c in ims) else 'NO')
