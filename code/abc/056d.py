N, K = map(int, input().split())
_A = list(map(int, input().split()))
A = []
ans = 0
for a in _A:
    if a >= K:  # 一つで良い集合
        ans += 1
    else:
        A.append(a)

M = len(A)
A.sort(reverse=True)
confilm = [0 for _ in range(N)]

sumA = [0 for _ in range(M + 1)]
for i in range(1, M + 1):
    sumA[i] = sumA[i - 1] + A[i - 1]

left = 0
right = 1
while right < M:
    while sumA[right] - sumA[left] >= K:
        left += 1
    for check in range(right, M):
        if (sumA[right] - sumA[left]) + A[check] >= K:
            confilm[check] = 1
            for i in range(left, right):
                confilm[i] = 1
    right += 1

ans += sum(confilm)
print(N - ans)