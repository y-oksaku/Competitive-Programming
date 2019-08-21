N, M = map(int, input().split())

cake = []

for _ in range(N) :
    x, y, z = map(int, input().split())
    cake.append((x, y, z))


ans = 0

for i in [0, 1] :
    for j in [0, 1] :
        for k in [0, 1] :
            sgn = ((-1)**i, (-1)**j, (-1)**k)  # 符号
            val = lambda A : sum([ A[i] * sgn[i] for i in range(3)])
            sortedCake = sorted(cake, key=val, reverse=True)
            xSum, ySum, zSum = 0, 0, 0
            for x, y, z in sortedCake[:M] :
                xSum += x
                ySum += y
                zSum += z
            sumCakeVal = abs(xSum) + abs(ySum) + abs(zSum)
            ans = max(ans, sumCakeVal)

print(ans)