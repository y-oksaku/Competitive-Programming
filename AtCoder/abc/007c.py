from collections import deque

def sol():
    R, C = map(int, input().split())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    chart = [[False for _ in range(C + 2)] for _ in range(R + 2)]

    for r in range(1, R + 1):
        line = input()
        for c in range(1, C + 1):
            if line[c - 1] == '.':
                chart[r][c] = True

    que = deque([])
    que.append((start[0], start[1], 0))
    minDist = [[float('inf') for _ in range(C + 2)] for _ in range(R + 2)]

    while que:
        nowR, nowC, dist = que.popleft()

        if minDist[nowR][nowC] <= dist:
            continue

        minDist[nowR][nowC] = dist

        if chart[nowR + 1][nowC] and minDist[nowR + 1][nowC] == float('inf'):
            que.append((nowR + 1, nowC, dist + 1))
        if chart[nowR - 1][nowC] and minDist[nowR - 1][nowC] == float('inf'):
            que.append((nowR - 1, nowC, dist + 1))
        if chart[nowR][nowC + 1] and minDist[nowR][nowC + 1] == float('inf'):
            que.append((nowR, nowC + 1, dist + 1))
        if chart[nowR][nowC - 1] and minDist[nowR][nowC - 1] == float('inf'):
            que.append((nowR, nowC - 1, dist + 1))


    print(minDist[goal[0]][goal[1]])


sol()
