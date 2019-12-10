from itertools import product
N, M = map(int, input().split())

cakes = [tuple(map(int, input().split())) for _ in range(N)]

# 8通り?
ans = 0
for mask in product([1, -1], repeat=3):
    S = []
    for cake in cakes:
        s = 0
        for a, b in zip(mask, cake):
            s += a * b
        S.append((s, cake))
    S.sort(reverse=True)

    a, b, c = 0, 0, 0
    for _, (x, y, z) in S[:M]:
        a += x
        b += y
        c += z

    ans = max(ans, abs(a) + abs(b) + abs(c))

print(ans)