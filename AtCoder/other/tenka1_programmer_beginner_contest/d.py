N = int(input())

# Nが三角数の場合はYes
M = (8 * N + 1)**0.5

if M.is_integer():
    M = (int(M) - 1) // 2
    print('Yes')
    print(M + 1)
    setNum = [[] for _ in range(N + 1)]
    for s in range(1, M + 2):
        ans = [M]
        V = set()
        for i in range(1, N + 1):
            if len(ans) > M:
                break
            if len(setNum[i]) >= 2:
                continue
            elif len(setNum[i]) == 0:
                ans.append(i)
                setNum[i].append(s)
            elif not setNum[i][0] in V:
                ans.append(i)
                setNum[i].append(s)
                V.add(setNum[i][0])
        print(*ans)
else:
    print('No')
