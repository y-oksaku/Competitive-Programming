N , K = map(int,input().split())
D = list(map(int,input().split()))

maxValue = 0

for i in range(min(N,K)+1):
    for j in range(min(N,K)-i+1):
        left = D[:i]
        right = D[N-j:]
        merge = (left + right + [0])
        merge.sort()

        index = 0

        for k in range(K-i-j):
            if (merge[index] < 0):
                index += 1
            else:
                break

        val = sum(merge[index:])
        if(maxValue < val):
            maxValue = val

print(maxValue)