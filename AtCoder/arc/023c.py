N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

def ncr(n, r):
    if r > n:
        return 1
    ret = 1
    for i in range(r):
        ret *= (n - i)
    for i in range(r):
        ret //= (r - i)
    return ret

ans = 1
cnt = 0
prev = 0
for a in A:
    if a == -1:
        cnt += 1
    else:
        m = a - prev
        ans *= ncr(m + cnt, cnt)
        cnt = 0
        prev = a
    ans %= MOD
print(ans)
