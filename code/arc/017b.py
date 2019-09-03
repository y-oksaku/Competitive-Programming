N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

left = 0
right = 0
ans = 0
while left < N:
    right = max(right, left)
    while right < N - 1 and A[right + 1] > A[right]:
        right += 1
    ans += max(0, right - left + 1 - (K - 1))
    left = right + 1

print(ans)
