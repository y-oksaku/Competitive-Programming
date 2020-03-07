from itertools import product

N = int(input())
R = 10**9
AB = []
S = []

for _ in range(N):
    a, b = map(int, input().split())
    S.append(a)
    S.append(b)
    AB.append((a, b))

def calc(s, g):
    ret = 0
    for a, b in AB:
        ret += min(
            abs(s - a) + abs(a - b) + abs(b - g),
            abs(s - b) + abs(b - a) + abs(a - g),
        )
    return ret

ans = 10**20
for s in S:
    for g in S:
        ans = min(ans, calc(s, g))

print(ans)