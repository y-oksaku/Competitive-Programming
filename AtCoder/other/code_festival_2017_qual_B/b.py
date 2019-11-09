from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

cntD = Counter(D)
for t in T:
    if cntD[t] <= 0:
        print('NO')
        break
    cntD[t] -= 1
else:
    print('YES')