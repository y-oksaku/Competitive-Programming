N = int(input())
A = [0] + list(map(int, input().split())) + [0]

distSum = [0 for _ in range(N + 3)]

for i in range(1, N + 2):
    distSum[i] = distSum[i - 1] + abs(A[i - 1] - A[i])

for j in range(1, N + 1):
    ans = distSum[j - 1] + abs(A[j - 1] - A[j + 1]) + (distSum[-2] - distSum[j + 1])
    print(ans)