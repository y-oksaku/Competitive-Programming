N, W = map(int, input().split())

items = [[] for _ in range(4)]
w0, v0 = map(int, input().split())
items[0].append(v0)

for _ in range(N - 1):
    w, v = map(int, input().split())
    items[w - w0].append(v)

for i in range(4):
    items[i].sort(reverse=True)

sumItems = [[0 for _ in range(len(items[i]) + 1)] for i in range(4)]

for i in range(4):
    for j, v in enumerate(items[i]):
        sumItems[i][j + 1] = sumItems[i][j] + v

ans = 0
for firstCount in range(len(items[0]) + 1):
    for secondCount in range(len(items[1]) + 1):
        for thirdCount in range(len(items[2]) + 1):
            for forthCount in range(len(items[3]) + 1):
                sumWeight = w0 * firstCount + (w0 + 1) * secondCount + (w0 + 2) * thirdCount + (w0 + 3) * forthCount
                if sumWeight > W:
                    break
                sumV = 0
                for i, count in enumerate([firstCount, secondCount, thirdCount, forthCount]):
                    sumV += sumItems[i][count]
                ans = max(ans, sumV)

print(ans)