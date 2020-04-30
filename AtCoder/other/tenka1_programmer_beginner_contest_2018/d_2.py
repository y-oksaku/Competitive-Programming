def sol():
    N = int(input())
    D = 0

    for d in range(1, int((2 * N)**0.5) + 100):
        if d * (d - 1) == 2 * N:
            D = d
            break

    if D == 0:
        print('No')
        return

    print('Yes')
    mx = 1
    ans = []
    for d in range(D):
        line = []
        for _ in range(D - d - 1):
            line.append(mx)
            mx += 1
        ans.append(line)
    for i in range(D):
        line = ans[i]
        for j in range(i):
            line.append(ans[j][-i])
    print(len(ans))
    for a in ans:
        print(len(a), end=' ')
        print(*a)

sol()