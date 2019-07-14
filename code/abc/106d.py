N, M, Q = map(int, input().split())

train = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M) :
    L, R = map(int, input().split())
    train[L][R] += 1

que = []
for _ in range(Q) :
    p, q = map(int, input().split())
    que.append((p, q))

# 累積和
S = [[0 for _ in range(N+1)] for _ in range(N+1)]  # ゼロパディング

for l in range(1, N+1) :
    for r in range(1, N+1) :
        S[l][r] = S[l-1][r] + S[l][r-1] - S[l-1][r-1] + train[l][r]

for p, q in que :
    ans = S[q][q] - S[p-1][q] - S[q][p-1] + S[p-1][p-1]
    print(ans)