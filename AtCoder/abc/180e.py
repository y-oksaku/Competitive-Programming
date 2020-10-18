N = int(input())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]
INF = 10**18

dp = [[INF] * N for _ in range(1 << N)]
dp[0][0] = 0

def dist(fr, to):
    x, y, z = XYZ[fr]
    u, v, w = XYZ[to]
    return abs(x - u) + abs(y - v) + max(0, w - z)

for state in range(1 << N):
    for fr in range(N):
        for to in range(N):
            dp[state | (1 << to)][to] = min(dp[state | (1 << to)][to], dp[state][fr] + dist(fr, to))
print(dp[(1 << N) - 1][0])
