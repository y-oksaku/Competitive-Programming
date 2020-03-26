N = int(input())
A = list(map(int, input().split()))

left = [10**18] * (N + 1)
right = [10**18] * (N + 1)

now = 0
left[0] = 0
for i, a in enumerate(A, start=1):
    now += a
    left[i] = left[i - 1] + now
    now += 1

now = 0
right[0] = 0
for i, a in enumerate(A[:: -1], start=1):
    now += a
    right[i] = right[i - 1] + now
    now += 1
right = right[::-1]

ans = min(left[-1], right[0])
for mid in range(N + 1):
    if mid % 2 == 1:
        ans = min(ans, left[mid - 1] + right[mid])
print(ans)
