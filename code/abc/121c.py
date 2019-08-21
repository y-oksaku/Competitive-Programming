N , M = map(int,input().split())
drink = [0] * N

for i in range(N) :
    a , b = map(int,input().split())
    drink[i] = [a,b] # 価格 , 本数

drink.sort(key=(lambda A : A[0])) # 安いもの順

now = 0
ans = 0

for i in range(N) :
    if drink[i][1] >= M - now :
        ans += drink[i][0] * (M - now)
        break
    ans += drink[i][1] * drink[i][0]
    now += drink[i][1]


print(ans)