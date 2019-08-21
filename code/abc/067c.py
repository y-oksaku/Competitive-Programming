N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
left = 0
right = sum(A)

for a in A[: N - 1]:
    left += a
    right -= a
    ans = min(ans, abs(left - right))

print(ans)