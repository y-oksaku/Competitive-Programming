A, B, C, D, E, F = map(int, input().split())

maxVal = 0
ans = (100 * A, 0)
for aWater in range(0, F + 1, A * 100):
    for bWater in range(0, F + 1, B * 100):
        sumWater = aWater + bWater
        if sumWater == 0 or sumWater > F:
            continue
        maxSuger = sumWater * E // 100
        for cSuger in range(0, maxSuger + 1, C):
            for dSuger in range(0, maxSuger + 1, D):
                sumSuger = cSuger + dSuger
                if sumSuger + sumWater > F or sumSuger > maxSuger:
                    break
                if maxVal < sumSuger / (sumSuger + sumWater):
                    maxVal = sumSuger / (sumSuger + sumWater)
                    ans = (sumSuger + sumWater, sumSuger)

print(*ans)