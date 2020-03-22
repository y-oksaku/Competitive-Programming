from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

que = deque([(0, 0)])
while que:
    h, w = que.popleft()

    A[h][w] = '?'

    if h == H - 1 and w == W - 1:
        break

    if h + 1 < H and A[h + 1][w] == '#':
        que.append((h + 1, w))
        continue

    if w + 1 < W and A[h][w + 1] == '#':
        que.append((h, w + 1))
        continue

cnt = sum([a.count('#') for a in A])
print('Possible' if cnt == 0 else 'Impossible')
