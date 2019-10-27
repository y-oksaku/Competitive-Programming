N = int(input())

nowT, nowX, nowY = 0, 0, 0

ans = True

for _ in range(N):
    nextT, nextX, nextY = map(int, input().split())
    dist = abs(nextX - nowX) + abs(nextY - nowY)
    time = nextT - nowT
    if dist > time:
        ans = False
    if (dist % 2) != (time % 2):
        ans = False
    nowT, nowX, nowY = nextT, nextX, nextY

if ans:
    print('Yes')
else:
    print('No')