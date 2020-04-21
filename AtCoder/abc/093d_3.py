Q = int(input())

ans = []
for _ in range(Q):
    A, B = map(int, input().split())

    if A == B:
        ans.append(2 * A - 2)
        continue

    C = (A * B)**0.5
    D = int(C)

    if C.is_integer():
        D -= 1

    F = 2 * D - 1
    if D * (D + 1) >= A * B:
        F -= 1

    ans.append(F)

print(*ans, sep='\n')