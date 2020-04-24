from itertools import product

N, M = map(int, input().split())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]

ans = -10**18
for sign in product((1, -1), repeat=3):
    S = [0, 0, 0]
    for xyz in sorted(XYZ, key=lambda xyz: sum(a * s for a, s in zip(xyz, sign)), reverse=True)[:M]:
        for i, (a, s) in enumerate(zip(xyz, sign)):
            S[i] += a * s
    ans = max(ans, sum(abs(a) for a in S))
print(ans)
