import sys
sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())

if X < N :
    print(0)
else :
    pat = [0] * (N + 1)  # パティ数
    ban = [0] * (N + 1)  # バンズ数
    pat[0] = 1
    for i in range(1, N + 1) :
        pat[i] = 2 * pat[i - 1] + 1
        ban[i] = 2 * ban[i - 1] + 2
    def sol(level, height) :
        if height <= 0 :
            return 0
        if level == 0 :
            return 1
        if height <= 1 :
            return 0
        if height < pat[level - 1] + ban[level - 1] :
            return sol(level - 1, height - 1)
        if height == pat[level - 1] + ban[level - 1] + 1 :
            return pat[level - 1]
        if height == pat[level - 1] + ban[level - 1] + 2 :
            return pat[level - 1] + 1
        return pat[level - 1] + 1 + sol(level - 1, height - (pat[level - 1] + ban[level - 1] + 2))

    ans = sol(N, X)
    print(ans)