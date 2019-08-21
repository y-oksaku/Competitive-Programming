import sys
sys.setrecursionlimit(10**5)

def sol():
    H, W = map(int, input().split())
    MOD = 10**9 + 7
    INF = float('inf')

    A = [[-INF for _ in range(W + 2)] for _ in range(H + 2)]

    for h in range(1, H + 1):
        line = list(map(int, input().split()))
        for w in range(1, W + 1):
            A[h][w] = line[w - 1]

    memo = [[-1 for _ in range(W + 2)] for _ in range(H + 2)]

    def search(h, w):
        ret = 1
        val = A[h][w]
        if A[h - 1][w] > val:
            if memo[h - 1][w] == -1:
                ret = (ret + search(h - 1, w)) % MOD
            else:
                ret = (ret + memo[h - 1][w]) % MOD
        if A[h + 1][w] > val:
            if memo[h + 1][w] == -1:
                ret = (ret + search(h + 1, w)) % MOD
            else:
                ret = (ret + memo[h + 1][w]) % MOD
        if A[h][w - 1] > val:
            if memo[h][w - 1] == -1:
                ret = (ret + search(h, w - 1)) % MOD
            else:
                ret = (ret + memo[h][w - 1]) % MOD
        if A[h][w + 1] > val:
            if memo[h][w + 1] == -1:
                ret = (ret + search(h, w + 1)) % MOD
            else:
                ret = (ret + memo[h][w + 1]) % MOD

        memo[h][w] = ret
        return ret

    ans = 0
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if memo[h][w] == -1:
                ans = (ans + search(h, w)) % MOD
            else:
                ans = (ans + memo[h][w]) % MOD
    print(ans)

sol()