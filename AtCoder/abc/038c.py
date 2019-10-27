N = int(input())
A = list(map(int, input().split()))

ans = N
right = 1
left = 0

while right < N:
    while right < N and A[right - 1] < A[right]:
        right += 1
        ans += right - left - 1
    left = right
    right += 1

print(ans)
