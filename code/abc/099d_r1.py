N, C = map(int, input().split())

D = []
c = []

for i in range(C) :
    line = list(map(int, input().split()))
    D.append(line)
for i in range(N) :
    line = list(map(int, input().split()))
    c.append(line)

colorCount = [[0 for _ in range(C + 1)] for _ in range(3)]  # colorCount[index][color]
for i in range(N) :
    for j in range(N) :
        colorCount[(i + j + 2) % 3][c[i][j]] += 1

ans = float('inf')
for firstColor in range(1, C + 1) :
    for secondColor in range(1, C + 1) :
        for thirdColor in range(1, C + 1) :
            if firstColor == secondColor or secondColor == thirdColor or thirdColor == firstColor :
                continue
            cost = 0
            for dist, toColor in enumerate([secondColor, thirdColor, firstColor]) :
                for fromColor in range(1, C + 1) :
                    if toColor == fromColor :
                        continue
                    cost += colorCount[dist][fromColor] * D[fromColor - 1][toColor - 1]
            ans = min(ans, cost)

print(ans)