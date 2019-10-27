def sol():
    N, Ma, Mb = map(int, input().split())

    A = []
    B = []
    cost = []
    sumA = 0
    sumB = 0

    for _ in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        cost.append(c)
        sumA += a
        sumB += b

    dp = [[[float('inf') for _ in range(sumB * 2 + 1)] for _ in range(sumA * 2 + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for index in range(N):
        for sA in range(sumA + 1):
            for sB in range(sumB + 1):
                dp[index + 1][sA][sB] = min(
                    dp[index + 1][sA][sB],
                    dp[index][sA][sB]
                )
                dp[index + 1][sA + A[index]][sB + B[index]] = min(
                    dp[index + 1][sA + A[index]][sB + B[index]],
                    dp[index][sA][sB] + cost[index]
                )

    ans = float('inf')
    for sA in range(1, sumA):
        for sB in range(1, sumB):
            if sA * Mb == sB * Ma:
                ans = min(ans, dp[N][sA][sB])

    if ans == float('inf'):
        print('-1')
    else:
        print(ans)

sol()