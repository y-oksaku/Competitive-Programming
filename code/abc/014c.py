def sol():
    N = int(input())
    ims = [0 for _ in range(10**6 + 10)]
    for _ in range(N):
        l, r = map(int, input().split())
        ims[l] += 1
        ims[r + 1] -= 1
    for i in range(1, 10**6 + 10):
        ims[i] += ims[i - 1]
    ans = 0
    for i in range(10**6 + 1):
        if ans < ims[i]:
            ans = ims[i]
    print(ans)


sol()