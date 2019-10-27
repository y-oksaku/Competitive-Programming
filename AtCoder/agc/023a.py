from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cumA = [0] * (N + 1)

for i in range(N):
    cumA[i + 1] += cumA[i] + A[i]

cntA = Counter(cumA)

ans = sum([c * (c - 1) // 2 for c in cntA.values()])

print(ans)