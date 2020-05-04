N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for l in range(N + 1):
    for r in range(N + 1):
        if l + r > N:
            continue
        k = K - (l + r)
        if k < 0:
            continue

        A = V[:l] + V[N - r:]
        A.sort(reverse=True)
        while k > 0 and A and A[-1] < 0:
            A.pop()
            k -= 1
        ans = max(ans, sum(A))
print(ans)
