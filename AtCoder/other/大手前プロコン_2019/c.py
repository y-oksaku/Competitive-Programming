from collections import Counter, defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cntB = Counter(B)
V = defaultdict(int)
now = float('inf')

for a in A:
    V[a] += 1
    now = min(now, cntB[a] // V[a])
    print(now)
