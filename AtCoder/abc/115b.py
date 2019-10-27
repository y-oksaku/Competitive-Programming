N = int(input())

pMax = 0
sumP = 0
for _ in range(N) :
    p = int(input())
    pMax = max(pMax, p)
    sumP += p

print(sumP - pMax // 2)


