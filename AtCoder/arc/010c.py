N, M, Y, Z = map(int, input().split())
cToI = dict()

colorPoint = [0] * M

for i in range(M):
    c, p = input().split()
    cToI[c] = i
    colorPoint[i] = int(p)

B = list(map(lambda a: cToI[a], input()))

dp = [[[-10**18] * (M + 1) for _ in range(1 << M)] for _ in range(N + 1)]  # dp[index][state][lastColor]
dp[0][0][M] = 0

for i in range(N):
    nxColor = B[i]
    for state in range(1 << M):
        for color in range(M + 1):
            nxPoint = dp[i][state][color]

            if dp[i + 1][state][color] < nxPoint:  # 使わない
                dp[i + 1][state][color] = nxPoint

            nxPoint += colorPoint[nxColor]
            nxState = state | (1 << nxColor)
            if color == nxColor:
                nxPoint += Y

            if dp[i + 1][nxState][nxColor] < nxPoint:
                dp[i + 1][nxState][nxColor] = nxPoint

ans = 0
dp = dp[N]
for end in range(M + 1):
    for state in range(1 << M):
        point = dp[state][end]
        if state == (1 << M) - 1:
            point += Z
        ans = max(ans, point)
print(ans)
