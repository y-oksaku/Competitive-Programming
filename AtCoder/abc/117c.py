N , M = map(int,input().split())

X = list(map(int,input().split()))

X.sort()

# 隣接点の間の距離が長い順で分割する
# おけるコマの個数-1だけ辺を取り除ける

maxDist = X[-1] - X[0]

dist = [0] * (M-1)

# 間の距離を計算
for i in range(M-1) :
    dist[i] = X[i+1] - X[i]

dist.sort(reverse=True)

for i in range(min(N-1,M-1)) :
    maxDist -= dist[i]

print(maxDist)