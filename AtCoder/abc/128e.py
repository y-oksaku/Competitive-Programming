N , Q = map(int,input().split())

D = [0]*Q
Input = []
length = [-1]*Q

for i in range(N):
    Input.append(list(map(int,input().split())))

# 距離順でソート
dist = lambda A : A[2]
Input.sort(key=dist)

for i in range(Q):
    D[i] = int(input())

# i番目の人の座標を計算
for i in range(Q):
    for j in range(N):
        if(Input[j][1] <= D[i]): # 工事終了時刻 <= 出発時刻
            continue

        stopTime = Input[j][2] + D[i] # 出発時刻 + 距離/速度

        if(stopTime >= Input[j][0] - 0.5 and stopTime <= Input[j][1] - 0.5): # 工事期間内
            length[i] = Input[j][2]
            break

for l in length:
    print(l)
