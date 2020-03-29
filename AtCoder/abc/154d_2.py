N, K = map(int, input().split())
P = list(map(int, input().split()))

Q = [(p + 1) / 2 for p in P]
now = sum(Q[:K])
ans = now
for i in range(N - K):
    now -= Q[i]
    now += Q[i + K]
    ans = max(ans, now)
print(ans)
