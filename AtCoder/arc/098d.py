N = int(input())
A = list(map(int, input().split()))

right = 0
xor = 0
S = 0
ans = 0
for left, a in enumerate(A):
    while right < N and (xor ^ A[right]) == (S + A[right]):
        xor ^= A[right]
        S += A[right]
        right += 1
    S -= a
    xor ^= a
    ans += right - left

print(ans)
