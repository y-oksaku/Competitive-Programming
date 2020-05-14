from itertools import product

K, N = map(int, input().split())
VW = [tuple(input().split()) for _ in range(N)]

for P in product(range(1, 4), repeat=K):
    ans = {}
    for V, W in VW:
        L = 0
        for v in map(int, V):
            T = W[L: L + P[v - 1]]
            if v in ans and ans[v] != T:
                break
            ans[v] = T
            L += P[v - 1]
        else:
            if L == len(W):
                continue
        break
    else:
        for i in range(1, K + 1):
            print(ans[i])
        exit()
