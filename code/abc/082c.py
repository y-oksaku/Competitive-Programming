from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
ans = 0

for num, c in count.items():
    if c < num:
        ans += c
    else:
        ans += c - num

print(ans)