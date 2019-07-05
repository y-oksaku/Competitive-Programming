H , W = map(int,input().split())

s = [0] * H

for i in range(H) :
    s[i] = list(input())

# 端をゼロパディング
L = [[0 for _ in range(W+2)] for _ in range(H+2)]
R = [[0 for _ in range(W+2)] for _ in range(H+2)]
U = [[0 for _ in range(W+2)] for _ in range(H+2)]
D = [[0 for _ in range(W+2)] for _ in range(H+2)]

for i in range(1,H+1) :
    for j in range(1,W+1) :
        # 左上から
        if s[i-1][j-1] == '#' :
            L[i][j] = 0
            U[i][j] = 0
        else :
            L[i][j] = L[i][j-1] + 1
            U[i][j] = U[i-1][j] + 1
        # 右下から
        if s[-i][-j] == '#' :
            R[-i-1][-j-1] = 0
            D[-i-1][-j-1] = 0
        else :
            R[-i-1][-j-1] = R[-i-1][-j] + 1
            D[-i-1][-j-1] = D[-i][-j-1] + 1

ans = 0

for i in range(1,H+1) :
    for j in range(1,W+1) :
        point = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
        if ans < point :
            ans = point

print(ans)