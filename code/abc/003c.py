def sol():
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()

    ans = 0
    for s in score[N - K:]:
        ans = (ans + s) / 2

    print(ans)


sol()