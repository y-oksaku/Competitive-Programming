N = int(input())
MOD = 10007

if N == 1 or N == 2:
    print(0)
    exit()

if N == 3:
    print(1)
    exit()

a, b, c = 0, 0, 1
for _ in range(N - 3):
    a, b, c = b, c, a + b + c
    a %= MOD
    b %= MOD
    c %= MOD

print(c)