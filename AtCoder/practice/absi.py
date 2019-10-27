N , Y = map(int,input().split())

# 最大
yukichi = int(Y / 10000)
higuchi = int(Y / 5000)

ans = '-1 -1 -1'

for i in range(yukichi+1) :
    for j in range(higuchi+1) :
        if i + j > N :
            break

        k = N - i - j # 1000円札

        if 10000 * i + 5000 * j + 1000 * k == Y :
            ans = '{} {} {}'.format(i,j,k)
            break
    if ans != '-1 -1 -1' :
        break

print(ans)

