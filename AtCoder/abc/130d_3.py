N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
S = 0
right = 0

for a in A:
    while right < N and S < K:
        S += A[right]
        right += 1
    if S >= K:
        ans += N - right + 1
    S -= a

print(ans)