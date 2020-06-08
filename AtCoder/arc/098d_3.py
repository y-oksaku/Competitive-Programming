N = int(input())
A = list(map(int, input().split()))

S = 0
r = 0
ans = 0
for l, a in enumerate(A):
    while r < N and S + A[r] == S ^ A[r]:
        S += A[r]
        r += 1
    ans += r - l
    S -= a
print(ans)
