N , M = map(int,input().split())

S = list(map(int,input().split()))
T = list(map(int,input().split()))

# 累積和参照のために0の行，列を追加
sm = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1) :
    for j in range(1,M+1) :
        new = sm[i-1][j] + sm[i][j-1]
        if S[i-1] == T[j-1] :
            new += 1  # dp = sm[i-1][j-1] + 1
        else :
            new -= sm[i-1][j-1] # dp = 0
        sm[i][j] = new

ans = (sm[-1][-1] + 1) % (10**9 + 7)

print(ans)