from collections import defaultdict

N, X = map(int, input().split())
W = [int(input()) for _ in range(N)]

W1 = W[:N // 2]
W2 = W[N // 2:]

dp1 = defaultdict(int)
dp2 = defaultdict(int)
dp1[0] = 1
dp2[0] = 1

for w in W1:
    for a, c in tuple(dp1.items()):
        if a + w <= X:
            dp1[a + w] += c
for w in W2:
    for a, c in tuple(dp2.items()):
        if a + w <= X:
            dp2[a + w] += c

ans = 0
for a, c in dp1.items():
    ans += c * dp2[X - a]
print(ans)
