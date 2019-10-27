N = int(input())

# 初期状態
l = [[0,0,0]]

for i in range(N) :
    l.append(list(map(int,input().split())))

flag = True

for i in range(N) :
    # マンハッタン距離(L1)
    dist = abs(l[i+1][1] - l[i][1]) + abs(l[i+1][2] - l[i][2])

    # 残り時刻
    time = l[i+1][0] - l[i][0]

    # 間に合わない場合
    if dist > time :
        flag = False
        break

    # 時刻と距離の偶数奇数が一致しなければならない
    if (dist + time) % 2 == 1 :
        flag = False
        break

if flag :
    print('Yes')
else :
    print('No')

