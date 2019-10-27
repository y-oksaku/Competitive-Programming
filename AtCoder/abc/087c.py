N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = [0 for _ in range(N + 1)]
sumB = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    sumA[i] = sumA[i - 1] + A[i - 1]
    sumB[i] = sumB[i - 1] + B[i - 1]

ans = 0
for middle in range(1, N + 1):
    sub = sumA[middle] + (sumB[N] - sumB[middle - 1])
    ans = max(ans, sub)

print(ans)