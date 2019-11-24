from collections import defaultdict

N, L = map(int, input().split())
INF = float('inf')

carPoint = set([L])

Vs, Ds = map(int, input().split())
cars = [(0, Ds, Vs)]
for _ in range(N):
    left, speed, dist = map(int, input().split())
    cars.append((left, min(L, left + dist), speed))
    carPoint.add(left)

cars.sort()
carPoint = list(carPoint)
carPoint.sort()
pIndex = 0

minTime = defaultdict(lambda : INF)
minTime[0] = 0

for left, right, speed in cars:
    while carPoint[pIndex] < left:
        pIndex += 1

    now = minTime[left]
    for to in carPoint[pIndex:]:
        if to > right:
            break
        minTime[to] = min(minTime[to], (to - left) / speed + now)

ans = minTime[L]
if ans == INF:
    print('impossible')
else:
    print('%.10f' % ans)