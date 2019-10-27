N = int(input())

if N == 3:
    print('2 5 63')
else:
    A2 = [a for a in range(2, 30001, 2) if a % 6 != 0]
    A3 = [a for a in range(3, 30001, 6)]
    A6 = [a for a in range(6, 30001, 6)]

    a2 = min(10000, (N - 2) // 2 * 2)  # 偶数個あればよい 2k + 4k = 6k
    N -= a2
    a3 = min(5000, N // 2 * 2)  # 偶数個あればよい 3k + 6k = 9k
    a6 = N - a3

    ans = A2[: a2] + A3[: a3] + A6[: a6]
    print(sum(ans))
    # print(*ans)