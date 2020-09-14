N = int(input())

def dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

XY = [tuple(map(int, input().split())) for _ in range(N)]
INF = -10**10

ans = 0
for O in [(INF, INF), (-INF, INF), (INF, -INF), (-INF, -INF)]:
    S = XY[0]
    for xy in XY:
        if dist(O, S) < dist(O, xy):
            S = xy
    O = S
    for xy in XY:
        if dist(O, S) < dist(O, xy):
            S = xy
    ans = max(ans, dist(O, S))
print(ans)
