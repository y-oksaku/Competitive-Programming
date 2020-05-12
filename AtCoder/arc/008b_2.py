from collections import Counter

N, M = map(int, input().split())
S = Counter(list(input()))
T = Counter(list(input()))

ans = 0
for s, c in S.items():
    if T[s] == 0:
        print(-1)
        exit()
    ans = max(ans, -(-c // T[s]))
print(ans)
