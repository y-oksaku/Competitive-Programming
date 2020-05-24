from math import pi

N, Q = map(int, input().split())

XRH = [tuple(map(int, input().split())) for _ in range(N)]
AB = [tuple(map(int, input().split())) for _ in range(Q)]

for A, B in AB:
    a = A
    b = B
    ans = 0
    for x, r, h in XRH:
        a = A
        b = B

        if x + h <= a or x >= b:
            continue

        a = max(a - x, 0)
        b = min(b - x, h)

        a = h - a
        b = h - b
        ans += (pi * r**2) * (a**3 - b**3) / (h**2)
    print(ans / 3)
