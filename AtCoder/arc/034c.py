from collections import Counter

A, B = map(int, input().split())
MOD = 10**9 + 7

def getPrimes(n):
    cnt = Counter()
    for p in range(2, int(n**0.5) + 100):
        while n % p == 0:
            cnt[p] += 1
            n //= p
    if n > 1:
        cnt[n] += 1
    return cnt

primeCnt = Counter()
for i in range(B + 1, A + 1):
    primeCnt += getPrimes(i)

ans = 1
for c in primeCnt.values():
    ans = (ans * (c + 1)) % MOD

print(ans)
