from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cntA = Counter(A)

S = 0
for c in cntA.values():
    S += c * (c - 1) // 2

ans = []
for a in A:
    ans.append(S - (cntA[a] - 1))

print(*ans, sep='\n')