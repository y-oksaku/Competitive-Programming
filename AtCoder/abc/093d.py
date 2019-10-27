import math

Q = int(input())

AB = []
for _ in range(Q) :
    a, b = map(int, input().split())
    if a > b :
        a, b = b, a
    AB.append((a, b))

for a, b in AB :
    if a == b :
        print(2 * a - 2)
        continue

    C = int(math.sqrt(a * b))
    if C * C == a * b :
        C -= 1

    if C * (C + 1) >= a * b :
        print(2 * C - 2)
    else :
        print(2 * C - 1)
