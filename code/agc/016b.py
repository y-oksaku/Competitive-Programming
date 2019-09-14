N = int(input())
A = list(map(int, input().split()))

minColor = min(A)
maxColor = max(A)

if minColor == maxColor:
    if minColor == N - 1:  # 各色の猫が1匹ずつ
        print('Yes')
    elif minColor * 2 <= N:  # 各色の猫が2匹以上
        print('Yes')
    else:
        print('No')
    exit()

if minColor + 1 != maxColor:
    print('No')
    exit()

minCnt = 0
maxCnt = 0

for a in A:
    if a == minColor:
        minCnt += 1
    elif a == maxColor:
        maxCnt += 1
    else:
        print('No')
        exit()

# minCnt : 1匹だけの色
# maxCnt : 2匹以上の色
# 全体でmaxColor個の色

if (maxColor - minCnt) * 2 <= maxCnt and maxColor >= minCnt + 1:
    print('Yes')
else:
    print('No')
