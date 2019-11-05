N, K = map(int, input().split())

if N + 1 <= K:
    if K == 0:
        print(1)
    else:
        print("INF")
else:
    ans = 0
    for y in range(N * (K + 1) + 1):
        if (y & N) != N:
            continue
        for x in range(max(0, y - K), y + 1)[:: -1]:
            if (y & x) == N:
                ans += 1

    print(ans)