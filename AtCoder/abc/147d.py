N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ans = 0
for d in range(60):
    zero = 0
    one = 0
    for a in A:
        if ((1 << d) & a) != 0:
            one += 1
        else:
            zero += 1

    ans += one * zero * (1 << d)
    ans %= MOD

print(ans)
