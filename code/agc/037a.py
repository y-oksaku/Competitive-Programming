def sol():
    S = input()
    N = len(S)

    prev = ''
    left = 0
    right = 1
    ans = 0
    while right <= N:
        while right <= N and S[left: right] == prev:
            right += 1

        if right >= N:
            if S[left: right] == prev:
                break
            else:
                ans += 1
                break

        prev = S[left: right]
        left = right
        right += 1
        ans += 1

    print(ans)


sol()