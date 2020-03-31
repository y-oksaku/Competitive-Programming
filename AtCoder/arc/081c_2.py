from collections import Counter
N = int(input())
cnt = Counter(map(int, input().split()))

L = []
for a, c in cnt.items():
    if c >= 2:
        L += [a] * (c // 2)
L.sort()

ans = 0 if len(L) < 2 else L[-1] * L[-2]
print(ans)
