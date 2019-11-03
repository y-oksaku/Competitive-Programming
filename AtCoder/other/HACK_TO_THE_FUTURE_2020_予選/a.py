N, M, B = map(int, input().split())
Gy, Gx = map(int, input().split())

chart = [[0] * N for _ in range(N)]
canGo = [False] * N

robots = []
for _ in range(M):
    y, x, c = input().split()
    robots.append((int(y), int(x), c))

blocks = [tuple(map(int, input().split())) for _ in range(B)]
for y, x in blocks:
    chart[y][x] = 'b'

def search(y, x, fy, fx):
    s = ''

    if y < 0:
        y = N - 1
        s = 'D'
    if y == N:
        y = 0
        s = 'U'
    if x < 0:
        x = N - 1
        s = 'R'
    if x == N:
        x = 0
        s = 'L'

    if chart[y][x] != 0:
        return

    if s != '':
        pass
    elif y > fy:
        s = 'U'
    elif y < fy:
        s = 'D'
    elif x < fx:
        s = 'R'
    elif x > fx:
        s = 'L'
    chart[y][x] = s

    search(y + 1, x, y, x)
    search(y - 1, x, y, x)
    search(y, x + 1, y, x)
    search(y, x - 1, y, x)

search(Gy - 1, Gx, Gy, Gx)
search(Gy + 1, Gx, Gy, Gx)
search(Gy, Gx - 1, Gy, Gx)
search(Gy, Gx + 1, Gy, Gx)

isChanged = [[False] * N for _ in range(N)]

for y, x, c in robots:
    visited = [[False] * N for _ in range(N)]
    while True:
        if c == 'U':
            y -= 1
            if y == -1:
                y = N - 1
        elif c == 'D':
            y += 1
            if y == N:
                y = 0
        elif c == 'R':
            x += 1
            if x == N:
                x = 0
        elif c == 'L':
            x -= 1
            if x == -1:
                x = N - 1
        if y == Gy and x == Gx or visited[y][x]:
            break
        visited[y][x] = True
        if chart[y][x] != c:
            isChanged[y][x] = True
            c = chart[y][x]

ans = []
for y in range(N):
    for x in range(N):
        if isChanged[y][x]:
            ans.append((y, x, chart[y][x]))

print(len(ans))
for y, x, c in ans:
    print(y, x, c)

with open('out.txt', mode='w') as f:
    ans = ['{}\n'.format(len(ans))] + ['{} {} {}\n'.format(y, x, c) for y, x, c in ans]
    s = ''.join(ans)
    f.write(s)
