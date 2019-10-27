N = int(input())

sumCost = 0
for _ in range(N):
    a, b = map(int, input().split())
    sumCost += a * b

sumCost = int(sumCost * 1.05)
print(sumCost)