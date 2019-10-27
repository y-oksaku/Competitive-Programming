N , K = map(int,input().split())

A = list(map(int,input().split()))


maxDigit = max(K,A[-1]).bit_length()

# 前計算
maxVal = [0] * maxDigit
for i in range(maxDigit) :
    count = 0
    mask = 2**i
    for a in A :
        count += (a & mask) // mask
    count = max(N - count, count)
    if i == 0 :
        maxVal[0] = count
    else :
        maxVal[i] = count * mask + maxVal[i-1]

valK = [0] * (maxDigit + 1)
for i in range(maxDigit-1, -1, -1) :
    mask = 2**i
    maskK = K & mask
    sumK = 0
    for a in A :
        val = a & mask
        if maskK != val :
            sumK += mask
    valK[i] = sumK + valK[i+1]

ans = valK[0]  # X = K
for i in range(maxDigit-1, -1, -1) :  # 上からi+1桁まではKと同じ
    if not K & (2**i) > 0  :  # i桁目が0の場合
        continue

    sumXor = valK[i+1]

    # i桁目 0にする
    mask = 2**i
    for n in range(N) :
        if A[n] & mask > 0 :
            sumXor += mask

    if i > 0 :
        sumXor += maxVal[i-1]

    ans = max(ans, sumXor)

print(ans)
