from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cntA = Counter(A)
B = []
for a, c in cntA.items():
    if c // 2 == 0:
        continue
    for _ in range(c // 2):
        B.append(a)

B.sort(reverse=True)
ans = B[0] * B[1] if len(B) >= 2 else 0

print(ans)