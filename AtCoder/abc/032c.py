N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
    exit()
if min(S) > K:
    print(0)
    exit()

ans = 0
right = 0
prod = 1

for left in range(N):
    while right < N and prod * S[right] <= K:
        prod *= S[right]
        right += 1

    ans = max(ans, right - left)
    prod //= S[left]

print(ans)
