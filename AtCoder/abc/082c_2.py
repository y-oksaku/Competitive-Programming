from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))

ans = 0
for a, c in A.items():
    if a < c:
        ans += c - a
    elif a > c:
        ans += c
print(ans)
