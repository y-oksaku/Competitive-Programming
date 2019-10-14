N, K = map(int, input().split())
_A = list(map(int, input().split()))
ans = 0

A = []
for a in _A:
    if a >= K:
        ans += 1
    else:
        A.append(a)

A.sort(reverse=True)
M = len(A)
isNess = [False] * M

accA = [0] * (M + 1)
for i in range(1, M + 1):
    accA[i] = accA[i - 1] + A[i - 1]

left = 0
for right in range(1, M):
    while accA[right] - accA[left] >= K:
        left += 1

    for i in range(right, M)[:: -1]:
        if (accA[right] - accA[left]) + A[i] >= K:
            isNess[i] = True
            for j in range(left, i):
                isNess[j] = True
            break

ans += sum(isNess)
print(N - ans)