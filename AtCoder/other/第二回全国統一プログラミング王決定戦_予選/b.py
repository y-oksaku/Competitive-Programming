from collections import Counter

N = int(input())
D = list(map(int, input().split()))
R = max(D)
MOD = 998244353

cntD = Counter(D)
ans = 1
for i in range(1, R + 1):
    ans *= pow(cntD[i - 1], cntD[i], MOD)
    ans %= MOD

if D[0] == 0 and cntD[0] == 1 and all(cntD[i] >= 1 for i in range(R + 1)):
    print(ans)
else:
    print(0)