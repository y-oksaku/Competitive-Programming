N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

A.sort()

if N % 2 == 1:
    check = [0]
    for i in range(2, N + 1, 2):
        check.append(i)
        check.append(i)
    if A != check:
        print(0)
        exit(0)
else:
    check = []
    for i in range(1, N + 1, 2):
        check.append(i)
        check.append(i)
    if A != check:
        print(0)
        exit(0)

ans = 1
for _ in range(N // 2):
    ans *= 2
    ans %= MOD

print(ans)