import sys
input = sys.stdin.buffer.readline

D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = [tuple(map(int, input().split())) for _ in range(N)]
INF = 10**10

dp = [[0] * N for _ in range(D + 1)]

for i, (a, b, c) in enumerate(ABC):
    if not (a <= T[0] <= b):
        dp[1][i] = -INF

for d, t in enumerate(T[1:], start=2):
    for i, (a, b, c) in enumerate(ABC):
        if not (a <= t <= b):
            continue
        Z = 0
        for j, (_, _, e) in enumerate(ABC):
            Z = max(Z, dp[d - 1][j] + abs(c - e))
        dp[d][i] = Z

ans = max(dp[D])
print(ans)