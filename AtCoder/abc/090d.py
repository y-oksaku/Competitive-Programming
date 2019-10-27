N, K = map(int, input().split())

if K == 0 :
    ans = N**2
else :
    ans = 0
    for b in range(K+1, N+1) :
        maxQ = N // b
        ans += (b - K) * maxQ
        ans += max(N - K - (maxQ * b) + 1, 0)

print(ans)