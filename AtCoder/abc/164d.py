from collections import defaultdict
S = input()
MOD = 2019

cnt = [0] * MOD
cnt[0] = 1

now = 0
ans = 0
for d, n in enumerate(map(int, S[::-1])):
    now = (n * pow(10, d, MOD) + now) % MOD
    ans += cnt[now]
    cnt[now] += 1

print(ans)
