def sol():
    N, _ = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    def dfs(index, val):
        if index == N:
            if val == 0:
                return False
            else:
                return True
        ret = True
        for t in T[index]:
            ret &= dfs(index + 1, val ^ t)
        return ret

    ans = dfs(0, 0)
    if ans:
        print('Nothing')
    else:
        print('Found')

sol()