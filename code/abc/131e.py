N , K = map(int,input().split())

minus = (N - 1) * (N - 2) // 2 - K  # 減らす回数

if minus < 0 :
    print('-1')
else :
    print(N - 1 + minus)
    # 1を中心とするスターを作成する
    for i in range(2,N+1) :
        print('1 {}'.format(i))

    if minus > 0 :
        # 辺の数を減らす
        for i in range(2,N+1) :
            for j in range(i+1,N+1) :
                if minus <= 0 :
                    break
                print('{} {}'.format(i,j))
                minus -= 1
            else :
                continue
            break
