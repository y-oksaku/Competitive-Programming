A, K = map(int, input().split())
B = 2 * 10**12

if K == 0:
    ans = B - A
else:
    now = A
    ans = 0
    while now < B:
        now *= (1 + K)
        now += 1
        ans += 1

print(ans)
