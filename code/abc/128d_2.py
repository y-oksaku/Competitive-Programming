N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for left in range(K + 1):
    for right in range(K + 1):
        if left > N - right or left + right > K:
            continue

        G = V[:left] + V[N - right:]
        G.sort()
        dis = 0
        for i, g in enumerate(G):
            if i >= K - (left + right) or g >= 0:
                break
            dis += g

        ans = max(ans, sum(G) - dis)

print(ans)