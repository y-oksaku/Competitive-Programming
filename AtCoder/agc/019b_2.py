from collections import Counter
A = input()
N = len(A)

ans = N * (N - 1) // 2
cnt = Counter(list(A))

for c in cnt.values():
    ans -= c * (c - 1) // 2

print(ans + 1)
