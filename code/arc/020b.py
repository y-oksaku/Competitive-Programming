from collections import Counter

N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

minCost = float('inf')

colorEven = Counter(A[:: 2])
colorOdd = Counter(A[1:: 2])

for firstColor in range(1, C + 1):
    for secondColor in range(1, C + 1):
        if firstColor == secondColor:
            continue
        cost = (N + 2 - 1) // 2 - colorEven[firstColor] + N // 2 - colorOdd[secondColor]

        minCost = min(minCost, cost * C)

print(minCost)