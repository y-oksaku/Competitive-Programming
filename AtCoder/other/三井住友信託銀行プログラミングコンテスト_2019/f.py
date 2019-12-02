T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

SA = T1 * A1 + T2 * A2
SB = T1 * B1 + T2 * B2

if SA == SB or A1 == B1:
    print('infinity')
    exit()

if SA > SB and A1 < B1:
    M = (B1 - A1) * T1
    d = SA - SB
    cnt = M // d
    ans = cnt * 2
    if M % d != 0:
        ans += 1
    print(max(0, ans))
elif SB > SA and B1 < A1:
    M = (A1 - B1) * T1
    d = SB - SA
    cnt = M // d
    ans = cnt * 2
    if M % d != 0:
        ans += 1
    print(max(0, ans))
else:
    print(0)
