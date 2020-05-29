N = int(input())
C = [int(input()) for _ in range(N)]

A = [0] * N
for i, c in enumerate(C):
    cnt = 0
    for d in C:
        if c % d == 0:
            cnt += 1
    A[i] = cnt - 1

ans = 0
for a in A:
    ans += (-(-(a + 1) // 2)) / (a + 1)
print(ans)
