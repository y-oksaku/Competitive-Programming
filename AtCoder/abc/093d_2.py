Q = int(input())
AB = [tuple(map(int, input().split())) for _ in range(Q)]
for A, B in AB:
    C = (A * B)**0.5

    if A == B:
        print(A * 2 - 2)
    else:
        if C.is_integer():
            C -= 1

        C = int(C)

        if C * (C + 1) >= A * B:
            print(C * 2 - 2)
        else:
            print(C * 2 - 1)