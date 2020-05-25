N = int(input())
A = list(map(int, input().split()))

ans = 0
S = A[0]
right = 1
for l, a in enumerate(A):
    while right < N and S + A[right] == S ^ A[right]:
        S += A[right]
        right += 1
    ans += right - l
    S -= a

print(ans)