from collections import deque

N = 10
A = [list(input()) for _ in range(N)]

sh, sw = 0, 0
for h in range(N):
    for w in range(N):
        if A[h][w] == 'o':
            sh = h
            sw = w
            break
    else:
        continue
    break

def isOk(h, w):
    org = A[h][w]
    A[h][w] = 'o'
    d = maxDist()
    A[h][w] = org
    return d == 0

def maxDist():
    dist = [[10**10] * N for _ in range(N)]
    que = deque([(sh, sw, 0)])
    while que:
        h, w, d = que.popleft()

        if dist[h][w] <= d:
            continue
        dist[h][w] = d

        if h > 0:
            if A[h - 1][w] == 'o':
                que.appendleft((h - 1, w, d))
            else:
                que.append((h - 1, w, d + 1))
        if h < N - 1:
            if A[h + 1][w] == 'o':
                que.appendleft((h + 1, w, d))
            else:
                que.append((h + 1, w, d + 1))
        if w > 0:
            if A[h][w - 1] == 'o':
                que.appendleft((h, w - 1, d))
            else:
                que.append((h, w - 1, d + 1))
        if w < N - 1:
            if A[h][w + 1] == 'o':
                que.appendleft((h, w + 1, d))
            else:
                que.append((h, w + 1, d + 1))
    ret = 0
    for h in range(N):
        for w in range(N):
            if A[h][w] == 'o':
                ret = max(ret, dist[h][w])
    return ret

for h in range(N):
    for w in range(N):
        if A[h][w] == 'x' and isOk(h, w):
            print('YES')
            exit()
print('NO')
