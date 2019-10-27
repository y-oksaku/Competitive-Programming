N , K = map(int,input().split())

sushi = []

for _ in range(N) :
    t, d = map(int,input().split())
    sushi.append((t,d))

sushi.sort(key=lambda A : A[1], reverse=True)

# 美味しいものから順にK個選ぶ
nowSushi = []
sumTaste = 0
numKind = 0
take = [0] * N  # 種類は高々N

for i in range(K) :
    t, d = sushi[i]
    nowSushi.append((t,d))
    sumTaste += d
    if take[t-1] == 0 :
        numKind += 1
    take[t-1] += 1

addSushi = []  # 種類を増やせる寿司
for i in range(K,N) :
    t, d = sushi[i]
    if take[t-1] > 0 :  # すでに選択済み
        continue
    addSushi.append((t,d))
    take[t-1] += 1

ans = sumTaste + numKind**2
L = len(addSushi)
changeCount = 0

while nowSushi :
    removeSushiT, removeSushiD = nowSushi.pop()
    if take[removeSushiT-1] <= 1 :
        continue
    if changeCount >= L :
        break

    addSushiT, addSushiD = addSushi[changeCount]
    changeCount += 1

    sumTaste = sumTaste - removeSushiD + addSushiD
    numKind = numKind + 1

    if (sumTaste + numKind**2) > ans :
        ans = sumTaste + numKind**2

print(ans)