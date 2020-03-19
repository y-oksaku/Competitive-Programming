N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
for i in range(N)[:: -1]:
    a = A[i]
    cnt = 0
    for j in range(i, N, (i + 1)):
        cnt += ans[j]
    if cnt % 2 != a % 2:
        ans[i] = 1

M = sum(ans)
print(M)
if M > 0:
    print(*[i for i, a in enumerate(ans, start=1) if a > 0])
