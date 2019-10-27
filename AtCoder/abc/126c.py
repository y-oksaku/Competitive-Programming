import math

N , K = map(int,input().split())

count = 0
now = K

# 必要なトスの回数と残りの数
while now > N :
    count += 1
    now = now / 2.

prob = 0

for i in range(1,N+1) :
    if i < now : # 残りの数未満の場合
        for k in range(N) : # 残りの数を超えるまでトス
            if i * 2**k >= now :
                break
        prob += 2**(-(count + k )) / N
    else :
        prob += 2**(-count) / N

print(prob)
