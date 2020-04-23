N = int(input())
A = list(map(int, input().split()))

left = 0
right = sum(A)

ans = float('inf')

for a in A[: -1]:
    left += a
    right -= a
    ans = min(ans, abs(left - right))

print(ans)