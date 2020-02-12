N, K = map(int, input().split())
A = list(map(int, input().split()))
P = pow(1 / 6, K)

now = sum(map(lambda a: a * (a + 1) // 2 / a, A[:K - 1]))
ans = 0
for left, right in zip(A, A[K - 1:]):
    now += right * (right + 1) // 2 / right
    ans = max(ans, now)
    now -= left * (left + 1) // 2 / left

print('{:.10f}'.format(ans))
