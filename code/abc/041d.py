def sol():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)

    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1 << N):
        for digit in range(N):
            if mask & (1 << digit) != 0:
                other = mask ^ (1 << digit)
                for back in edge[digit]:
                    if other & (1 << back) != 0:
                        break
                else:
                    dp[mask] += dp[other]

    print(dp)
    print(dp[(1 << N) - 1])

sol()