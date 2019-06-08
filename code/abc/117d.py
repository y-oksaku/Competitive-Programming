import math

N , K = map(int,input().split())
A = list(map(int,input().split()))

if K == 0 :
    ans = sum(A)
else :
    bitK = bin(K+1)[2:]
    maxBit = math.ceil(math.log2(K)) # 必要なビット数

    bitCount = [0] * maxBit # 各桁の1の数

    for i in range(0,maxBit) :
        mask = 1 << i
        for j in range(N) :
            bitCount[i] += ((mask & A[j]) >> i)

    ans = 0

    for i in range(0,maxBit) : # iビット未満のビットを自由に選べる
        if bitK[i] == '0' :
            continue
        f = 0

        for j in range(i+1,maxBit) : # 固定ビット
            if bitK[j] == '0' :
                f += bitCount[j] << j
            else :
                f += (N - bitCount[j]) << j

        f += bitCount[i] << i

        for j in range(0,i) : # 自由ビット
            count = max(N-bitCount[j],bitCount[j])
            f += count << j

        ans = max(ans,f)

print(ans)