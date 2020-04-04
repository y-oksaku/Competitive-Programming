N = int(input())
A = list(map(int, input().split()))

S = 0
for i, a in enumerate(A):
    S += (-1)**i * a

ans = [0] * N
ans[0] = S
for i, a in enumerate(A[:-1], start=1):
    S *= -1
    S += 2 * a
    ans[i] = S

print(*ans)