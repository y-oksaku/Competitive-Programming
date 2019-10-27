def sol():
    S = input()
    N = len(S)

    if N == 2:
        if S[0] == S[1]:
            print(1, 2)
            return
        else:
            print(-1, -1)
            return

    for i in range(N - 3):
        sub = set(S[i: i + 3])
        if len(sub) <= 2:
            print(i + 1, i + 3)
            return

    print(-1, -1)
    return


sol()