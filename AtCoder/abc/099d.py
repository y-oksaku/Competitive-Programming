N, C = map(int, input().split())

weight = []
color = []
colorCount = [[0 for _ in range(C)] for _ in range(3)]

for _ in range(C) :
    line = list(map(int, input().split()))
    weight.append(line)

for i in range(N) :
    line = list(map(int, input().split()))
    color.append(line)
    for j, c in enumerate(line) :
        colorCount[(i + j + 2) % 3][c - 1] += 1

ans = float('inf')

for firstColor in range(C) :
    for secondColor in range(C) :
        for thirdColor in range(C) :
            if firstColor == secondColor or secondColor == thirdColor or thirdColor == firstColor :
                continue
            cost = 0
            for i, newColor in enumerate([firstColor, secondColor, thirdColor]) :
                for oldColor in range(C) :
                    cost += colorCount[i][oldColor] * weight[oldColor][newColor]
            ans = min(ans, cost)

print(ans)
