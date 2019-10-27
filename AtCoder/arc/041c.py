def sol():
    N, L = map(int, input().split())
    point = []
    direct = []
    for _ in range(N):
        x, d = input().split()
        point.append(int(x))
        direct.append(d)

    rabbitGroup = [[(point[0], direct[0])]]

    for i in range(1, N):
        if direct[i - 1] == 'L' and direct[i] == 'R':
            rabbitGroup.append([])
        rabbitGroup[-1].append((point[i], direct[i]))

    ans = 0
    for rabbits in rabbitGroup:
        if rabbits[0][1] == rabbits[-1][1]:
            if rabbits[0][1] == 'L':
                for i, (p, _) in enumerate(rabbits):
                    ans += p - 1 - i
            else:
                for i, (p, _) in enumerate(rabbits[:: -1]):
                    ans += L - p - i
        else:
            rLeft = 0
            while rabbits[rLeft][1] == 'R':
                rLeft += 1

            # 右寄せ
            rightSum = sum([rabbits[rLeft][0] - r - (i + 1) for i, (r, _) in enumerate(rabbits[: rLeft])])
            rightSum += sum([l - rabbits[rLeft][0] - (i + 1) for i, (l, _) in enumerate(rabbits[rLeft + 1:])])

            # 左寄せ
            leftSum = sum([l - rabbits[rLeft - 1][0] - (i + 1) for i, (l, _) in enumerate(rabbits[rLeft:])])
            leftSum += sum([rabbits[rLeft - 1][0] - r - (i + 1) for i, (r, _) in enumerate(rabbits[:rLeft - 1])])

            ans += max(leftSum, rightSum)

    print(ans)

sol()
