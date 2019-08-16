from collections import deque

H, W, T = map(int, input().split())

chart = [['W' for _ in range(W + 2)] for _ in range(H + 2)]
start = (0, 0)
end = (0, 0)

for h in range(1, H + 1):
    line = input()
    for w in range(1, W + 1):
        if line[w - 1] == '.':
            chart[h][w] = True
        elif line[w - 1] == 'S':
            chart[h][w] = True
            start = (h, w)
        elif line[w - 1] == 'G':
            chart[h][w] = True
            end = (h, w)
        else:
            chart[h][w] = False

def search(n):
    que = deque([])
    que.append((start[0], start[1], 0))

    minDist = [[float('inf') for _ in range(W + 2)] for _ in range(H + 2)]
    minDist[start[0]][start[1]] = 0

    while que:
        h, w, dist = que.popleft()

        if minDist[h][w] < dist:
            continue

        minDist[h][w] = dist

        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if a * b != 0 or a == b == 0:
                    continue
                if chart[h + a][w + b] == 'W':
                    continue
                if chart[h + a][w + b]:
                    que.append((h + a, w + b, dist + 1))
                else:
                    que.append((h + a, w + b, dist + n))

    return minDist[end[0]][end[1]]

dist = search(10**5)
blackCount = dist // 10**5
whiteCount = dist % 10**5

def isOkBig(n):
    if blackCount * n + whiteCount <= T:
        return True
    else:
        return False

def isOkSmall(n):
    if search(n) <= T:
        return True
    else:
        return False

bigLeft = 1
bigRight = 10**9

while bigRight - bigLeft > 1:
    mid = (bigLeft + bigRight) // 2
    if isOkBig(mid):
        bigLeft = mid
    else:
        bigRight = mid

smallLeft = 1
smallRight = 10**2 + 10

while smallRight - smallLeft > 1:
    mid = (smallLeft + smallRight) // 2
    if isOkSmall(mid):
        smallLeft = mid
    else:
        smallRight = mid

ans = max(bigLeft, smallLeft)
print(ans)
