from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

for a in A:
    cnt[a] = 1 if cnt[a] % 2 else 2

ans = len(cnt.keys()) - len([c for c in cnt.values() if c == 2]) % 2
print(ans)
