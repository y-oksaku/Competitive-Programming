from heapq import heappush, heappop
from collections import defaultdict

N, V, X, Y = map(int, input().split())
X -= 1
Y -= 1

L = [list(map(int, input().split())) for _ in range(N)]

que = [(-V, 0, 0, False)]  # life, x, y, usedO
maxLife = defaultdict(lambda : -float('inf'))

while que:
    life, x, y, usedO = heappop(que)
    life *= -1

    if x == X and y == Y and not usedO:
        life *= 2
        usedO = True

    if life <= 0:
        continue

    if x == y == N - 1:
        print('YES')
        exit()

    if maxLife[(x, y, usedO)] >= life:
        continue
    maxLife[(x, y, usedO)] = life

    for nx in [x - 1, x + 1]:
        if 0 <= nx < N and life - L[y][nx] > 0:
            heappush(que, (-(life - L[y][nx]), nx, y, usedO))

    for ny in [y - 1, y + 1]:
        if 0 <= ny < N and life - L[ny][x] > 0:
            heappush(que, (-(life - L[ny][x]), x, ny, usedO))

print('NO')